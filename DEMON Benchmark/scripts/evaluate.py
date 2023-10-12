import re
from rouge import Rouge
import argparse
import os
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class Eval:
    def __init__(self):
        self.periodStrip = re.compile("(?!<=\d)(\.)(?!\d)")
        self.commaStrip = re.compile("(\d)(\,)(\d)")
        self.punct = [
            ";",
            r"/",
            "[",
            "]",
            '"',
            "{",
            "}",
            "(",
            ")",
            "=",
            "+",
            "\\",
            "_",
            "-",
            ">",
            "<",
            "@",
            "`",
            ",",
            "?",
            "!",
        ]
        
    def processPunctuation(self, inText):
        outText = inText
        for p in self.punct:
            if (p + " " in inText or " " + p in inText) or (
                re.search(self.commaStrip, inText) != None
            ):
                outText = outText.replace(p, "")
            else:
                outText = outText.replace(p, " ")
        outText = self.periodStrip.sub("", outText, re.UNICODE)
        return outText
    
    def process(self, answer):
        answer = answer.replace("\n", " ")
        answer = answer.replace("\t", " ")
        answer = answer.strip()
        answer = self.processPunctuation(answer)
        answer = answer.strip('\'')
        answer = answer.strip('\"')
        answer = answer.strip().lower()
        return answer

    def evaluate_rouge(self,preds):
        rouge = Rouge()
        acc = {'f': []}
        eval_list = []
        for i, res in enumerate(preds):
            sample_id = res['sample_id']
            gt_ans = self.process(res["gt_response"])
            pred_ans = self.process(res["pred_response"])
            assert gt_ans != ''
            if pred_ans == '':
                s = 0
            else:
                s = rouge.get_scores(pred_ans, gt_ans)[0]['rouge-l']['f']
            acc['f'].append(s)
            eval_list.append({'id':str(sample_id),'score':str(round(s,3))})
        results = {'Rouge-L f': np.mean(acc['f'])}
        return results,eval_list

    def get_choice_list(self,preditions,core_json):
        assert len(preditions) == len(core_json['data'])
        new_pres = {d['sample_id']: d for d in preditions}
        for sample in core_json['data']:
            choice_list = sample['task_instance']['choice_list']
            new_pres[int(sample['sample_id'])]['choice_list'] = choice_list
            new_pres[int(sample['sample_id'])]['gt_response'] = sample['response']
        for pre in new_pres.values():
            assert 'choice_list' in pre.keys()

    def judge_multi_choice(self,sample):
        sample_id = sample['sample_id']
        gt_ans = sample["gt_response"]
        pred_ans = sample["pred_response"]
        choice_list = sample['choice_list']
        if gt_ans not in choice_list:
            print(gt_ans)
            print(choice_list)
        assert gt_ans in choice_list
        try:
            vectorizer = TfidfVectorizer()
            texts = [pred_ans] + choice_list
            tfidf_matrix = vectorizer.fit_transform(texts)
            cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
            most_similar_index = cosine_similarities.argmax()
            if choice_list[most_similar_index] == gt_ans:
                return 1
            else:
                return 0
        except:
            if pred_ans == gt_ans:
                return 1
            else:
                return 0

    def process_sample(self,sample):
        sample["gt_response"] = self.process(sample["gt_response"])
        sample["pred_response"] = self.process(sample["pred_response"])
        for i in range(len(sample['choice_list'])):
            sample["choice_list"][i] = self.process(sample["choice_list"][i])

    def evaluate_multichoice(self,preditions,core_json):
        self.get_choice_list(preditions,core_json)
        correct = 0
        eval_list = []
        for i, sample in enumerate(preditions):
            if 'choice_list' not in sample.keys():
                print(sample)
            self.process_sample(sample)
            score = self.judge_multi_choice(sample)
            sample_id = sample['sample_id']
            sample['result'] = score
            eval_list.append({'id':str(sample_id),'score':str(score)})
            correct+=score
        return {'Accuracy':correct/len(preditions)},eval_list

    def evaluate_multi_choice_image(self,preditions):
        correct = 0
        eval_list = []
        for i,sample in enumerate(preditions):
            gt_ans = self.process(sample["gt_response"])
            pred_ans = self.process(sample["pred_response"])
            sample_id = sample['sample_id']
            choice_list = ['image a','image b','image c','image d']
            if gt_ans[:7] == pred_ans[:7]:
                score = 1
            else:
                score = 0
            count = 0
            for choice in choice_list:
                if choice in pred_ans:
                    count += 1
            if count > 1:
                score = 0
            sample_id = sample['sample_id']
            sample['result'] = score
            eval_list.append({'id':str(sample_id),'score':str(score)})
            correct+=score
        return {'Accuracy':correct/len(preditions)},eval_list

parser = argparse.ArgumentParser()
parser.add_argument('--i4-dir', type=str, required=True)
parser.add_argument('--dataset', type=str, required=True)
parser.add_argument('--result-dir', type=str, required=True)
args = parser.parse_args()
i4_dir = args.i4_dir
dataset = args.dataset
result_dir = args.result_dir
model_name = result_dir.split('/')[-1]
core_annotation = json.load(open(os.path.join(i4_dir,dataset,'core','core.json'),'r'))
question_type = core_annotation['metadata']['question_type']

image_choice_dataset_list=["recipeqa-RecipeQA_VisualCloze","RecipeQA_ImageCoherence","COMICS_Panel"]
E = Eval()
output_dir = os.path.join(result_dir, dataset)
if not os.path.exists(os.path.join(output_dir,'pred.json')):
    print('%s--%s  No prediction file found'%(model_name, dataset))
    exit(0)
preds = json.load(open(os.path.join(output_dir,'pred.json'),'r'))
if question_type == 'open-ended':
    eval_result,eval_list = E.evaluate_rouge(preds)
elif question_type == 'multi-choice':
    if dataset in image_choice_dataset_list:
        eval_result,eval_list = E.evaluate_multi_choice_image(preds)
    else:
        eval_result,eval_list = E.evaluate_multichoice(preds,core_annotation)
else:
    eval_result = 'Dataset not supported'
    print('Dataset not supported')
    exit(0)

print(model_name,end = ':  ')
print(dataset,end = ':  ')
print(eval_result)
with open(os.path.join(output_dir,'eval.json'),'w') as f:
    json.dump(eval_result,f)

with open(os.path.join(output_dir,'eval_score.json'),'w') as f:
    json.dump(eval_list,f,indent=4)