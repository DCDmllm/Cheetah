import argparse
import os
import random

import numpy as np
import torch
import torch.backends.cudnn as cudnn

from omegaconf import OmegaConf
from cheetah.common.config import Config
from cheetah.common.registry import registry
from cheetah.conversation.conversation_llama2 import Chat, CONV_VISION

from cheetah.models import *
from cheetah.processors import *

def parse_args():
    parser = argparse.ArgumentParser(description="Demo")
    parser.add_argument("--cfg-path", required=True, help="path to configuration file.")
    parser.add_argument("--gpu-id", type=int, default=0, help="specify the gpu to load the model.")
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

print('Initializing Chat')
args = parse_args()

config = OmegaConf.load(args.cfg_path)
cfg = Config.build_model_config(config)
model_cls = registry.get_model_class(cfg.model.arch)
model = model_cls.from_config(cfg.model).to('cuda:{}'.format(args.gpu_id))

vis_processor_cfg = cfg.preprocess.vis_processor.eval
vis_processor = registry.get_processor_class(vis_processor_cfg.name).from_config(vis_processor_cfg)
chat = Chat(model, vis_processor, device='cuda:{}'.format(args.gpu_id))
print('Initialization Finished')

######## Example1 ########
print("\nExample 1:")
context = "<Img><HereForImage></Img> <Img><HereForImage></Img> <Img><HereForImage></Img> <Img><HereForImage></Img> What do these four pictures want to convey to us? "
raw_img_list = ['./examples/1.jpg', './examples/2.jpg', './examples/3.jpg', './examples/4.jpg']
print("Question: ", context)
llm_message = chat.answer(raw_img_list, context)
print("Answer: ", llm_message)

######## Example2 ########
print("\nExample 2:")
context = "<Img><HereForImage></Img> <Img><HereForImage></Img> What does these picture want to show us? "
raw_img_list = ['./examples/5.jpg', './examples/6.jpg']
print("Question: ", context)
llm_message = chat.answer(raw_img_list, context)
print("Answer: ", llm_message)

######## Example3 ########
print("\nExample 3:")
context = "<Img><HereForImage></Img> <Img><HereForImage></Img> What is the connection between these two pictures?  "
print("Question: ", context)
raw_img_list = ['./examples/21.jpg', './examples/22.png']
llm_message = chat.answer(raw_img_list, context)
print("Answer: ", llm_message)

context = "<Img><HereForImage></Img> <Img><HereForImage></Img> What makes this set of pictures look interesting? "
raw_img_list = ['./examples/21.jpg', './examples/22.png']
print("Question: ", context)
llm_message = chat.answer(raw_img_list, context)
print("Answer: ", llm_message)

######## Example4 ########
### round 1 ###
print("\nExample 4:")
context1 = "<Img><HereForImage></Img> What is this in picture? "
context = context1
print("Question 4-1: ", context)
raw_img_list = ['./examples/16.jpeg']
llm_message = chat.answer(raw_img_list, context)
print("Answer 4-1: ", llm_message)
### round 2 ###
context += ' [/INST]'
context += (" " + llm_message + " " + CONV_VISION.sep2)
context2 = "<Img><HereForImage></Img> Is it still the fish you thought it was now? "
context += (CONV_VISION.sep + "[INST] " + context2)
print("Question 4-2: ", context)
raw_img_list.append('./examples/17.jpeg')
llm_message = chat.answer(raw_img_list, context)
print("Answer 4-2: ", llm_message)
### round 3 ###
context += ' [/INST]'
context += (" " + llm_message + " " + CONV_VISION.sep2)
context3 = "What else can this pencil case be used for besides holding pens? "
context += (CONV_VISION.sep + "[INST] " + context3)
print("Question 4-3: ", context)
llm_message = chat.answer(raw_img_list, context)
print("Answer 4-3: ", llm_message)
