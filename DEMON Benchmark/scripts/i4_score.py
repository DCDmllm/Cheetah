import json
import argparse
import os

dataset_list={}
dataset_list['multi_modal_dialogue'] = ['MMCoQA','ALFRED']
dataset_list['visual_story_telling_list'] = ['AESOP','DiDeMoSV','FlintstonesSV','PororoSV','VIST']
dataset_list['visual_relation_inference'] = ['IEdit','Spot-the-Diff','Birds-to-Words','CLEVR-Change']
dataset_list['multi_modal_cloze'] = ['COMICS_Dialogue','COMICS_Panel','RecipeQA_VisualCloze','RecipeQA_TextCloze']
dataset_list['knowledge_grounded_qa'] = ['WebQA','TQA','MultiModalQA']
dataset_list['text_rich_images_qa'] = ['SlideVQA','OCR-VQA','DocVQA']
dataset_list['multi_image_reasoning'] = ['Fashion200K','NLVR2','nuscenes','VizWiz','MIT-States_StateCoherence','MIT-States_PropertyCoherence','VISION','RecipeQA_ImageCoherence']

parser = argparse.ArgumentParser()
parser.add_argument('--result_dir', type=str, required=True)
args = parser.parse_args()
result_dir = args.result_dir
model_name = result_dir.split('/')[-1]
print(model_name)

def dict_mean(dict_list):
    mean_dict = {}
    for key in dict_list[0].keys():
        mean_dict[key] = round(sum(d[key] for d in dict_list) / len(dict_list), 5)*100
        
    return mean_dict

for task in dataset_list.keys():
    for dataset in dataset_list[task]:
        output_dir = os.path.join(result_dir, dataset)
        if not os.path.exists(os.path.join(output_dir,'eval.json')):
            print('%s--%s  No evaluation file found'%(model_name, dataset))
            exit(0)

with open((result_dir,'i4-score.txt'),'w+') as f:
    for task in dataset_list.keys():
        task_result_list = []
        for dataset in dataset_list[task]:
            dataset_result = json.load(open(os.path.join(output_dir,'eval.json'),'r'))
            task_result_list.append(dataset_result)
        task_result = dict_mean(task_result_list)
        print('%s--%s  %s'%(model_name, task, task_result))
        f.write('%s--%s  %s'%(model_name, task, task_result))