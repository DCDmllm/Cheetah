import argparse
import os
import random
import json
import numpy as np
import torch
import torch.backends.cudnn as cudnn
from torch.utils.data import Dataset
from omegaconf import OmegaConf
from cheetah.common.config import Config
from cheetah.common.registry import registry
from cheetah.conversation.conversation_llama2 import Chat, CONV_VISION
from tqdm import tqdm
from cheetah.models import *
from PIL import Image
from cheetah.processors import *

def parse_args():
    parser = argparse.ArgumentParser(description="Benchmark prediction")
    parser.add_argument("--cfg-path", required=True, help="path to configuration file.")
    parser.add_argument("--gpu-id", type=int, default=0, help="specify the gpu to load the model.")
    parser.add_argument('--batch-image', type=int, required=False, default=30)
    parser.add_argument('--i4-dir', type=str, required=True)
    parser.add_argument('--dataset', type=str, required=True)
    parser.add_argument("--result-dir",type=str,required=True)
    parser.add_argument(
        "--options",
        nargs="+",
        help="override some settings in the used config, the key-value pair "
        "in xxx=yyy format will be merged into config file (deprecate), "
        "change to --cfg-options instead.",
    )
    args = parser.parse_args()
    return args

def setup_seeds(seed = 50):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    cudnn.benchmark = False
    cudnn.deterministic = True

class IDataset(Dataset):
    def __init__(
        self, annoation, task_instructions, img_dir,
    ):
        self.img_dir = img_dir
        self.annotation = annoation
        self.task_instructions = task_instructions
    def __len__(self):
        return len(self.annotation)

    
    def __getitem__(self, index):
        ann = self.annotation[index]
        task_instruction = self.task_instructions[ann['task_instruction_id']]
        context = task_instruction + ann['task_instance']['context']
        raw_img_list = []
        if 'choice_list' in ann['task_instance'].keys():
            choice_str = 'Choice list:[\''+'\', \''.join(ann['task_instance']['choice_list']) +'\']. Your answer is:'
            context += choice_str
        for i in range(len(ann['task_instance']['images_path'])):
            rmv_txt = '{image#%d}'% (i+1)
            rmv_tbl = '{table#%d}'% (i+1)
            context = context.replace(rmv_txt, '<ImageHere>')
            context = context.replace(rmv_tbl, '<ImageHere>')
        for p in ann['task_instance']['images_path']:
            img_path = os.path.join(self.img_dir, p)
            raw_img_list.append(img_path)
        return {
            "sample_id": ann['sample_id'],
            "context": context,
            "raw_img_list": raw_img_list,
            "response": str(ann['response'])
        }        

def collate_fn(batch):
    batch_data={}
    batch_data['sample_id'] = [sample['sample_id'] for sample in batch]
    batch_data['context'] = [sample['context'] for sample in batch]
    batch_data['raw_img_list'] = [sample['raw_img_list'] for sample in batch]
    batch_data['response'] = [sample['response'] for sample in batch]
        
    return batch_data

def split_data(data):
    data_dict = {}
    for d in data:
        n_img = len(d['task_instance']['images_path'])
        if n_img in data_dict:
            data_dict[n_img].append(d)
        else:
            data_dict[n_img] = [d]
    return data_dict

args = parse_args()

i4_dir = args.i4_dir
dataset_name = args.dataset
batch_image = args.batch_image
dataset_dir = os.path.join(i4_dir, dataset_name,'core')
img_dir  = os.path.join(dataset_dir,'images')
output_dir = os.path.join(args.result_dir,dataset_name)
model_name = args.result_dir.split('/')[-1]
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
core_annotation = json.load(open(os.path.join(dataset_dir,'core.json'),'r'))
prediction_results = []
data_dict = split_data(core_annotation['data'])

config = OmegaConf.load(args.cfg_path)
cfg = Config.build_model_config(config)
model_cls = registry.get_model_class(cfg.model.arch)
model = model_cls.from_config(cfg.model).to('cuda:{}'.format(args.gpu_id))

vis_processor_cfg = cfg.preprocess.vis_processor.eval
vis_processor = registry.get_processor_class(vis_processor_cfg.name).from_config(vis_processor_cfg)
chat = Chat(model, vis_processor, device='cuda:{}'.format(args.gpu_id))
print('Initialization Finished')
print('Predicting %s Using %s'%(dataset_name,model_name))
for n_img, sub_data in data_dict.items():
    print('Proceeding %d-length images samples | Num:%d'%(n_img,len(sub_data)))
    E = IDataset( sub_data, core_annotation['metadata']['task_instruction'],img_dir)
    data_loader = torch.utils.data.DataLoader(dataset=E, batch_size=max(int(batch_image/n_img),1),shuffle=False,num_workers = 8,collate_fn = collate_fn)
    for i,samples in enumerate(tqdm(data_loader)):
        pred_responses = chat.batch_answer(batch_raw_img_list=samples['raw_img_list'],batch_context=samples['context'],max_length=5000)
        for sid, gt, p in zip(samples['sample_id'],samples['response'],pred_responses):
            if torch.is_tensor(sid):
                sid = sid.item()
            prediction_results.append({'sample_id':sid,'pred_response':p, 'gt_response':gt})
            
with open(os.path.join(output_dir,'pred.json'),'w',encoding='utf8') as f:
    json.dump(prediction_results,f,indent=4,ensure_ascii=False)