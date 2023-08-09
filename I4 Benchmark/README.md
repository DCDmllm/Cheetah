# I4 Benchmark
We build I4 (semantically **I**nterconnected, **I**nterleaved **I**mage-Text **I**nstruction-Following), an extensive large-scale benchmark of 31 tasks, where each task is paired with 10 meticulously-designed task definition and transformed into a unified instruction-response format. 

![example](./demo.svg)
Download Link:
- [Google Drive](https://drive.google.com/drive/folders/1x3O7brcJi4XJS2c6LLUpG5Xx0mg1WkRG?usp=drive_link)

I4 has three important properties: 

- **Interleaved vision-language context:** all the instructions contain sequences of inter-related images and texts, such as storyboards with scripts, textbooks with diagrams. 
- **Diverse forms of complex instructions:** the instructions range from predicting dialogue for comics, to discovering differences between surveillance images, and to conversational embodied tasks. 
- **Vast range of instruction-following scenarios:** the benchmark covers multiple application scenarios, including cartoons, industrial images, driving recording, etc...

|         | Tasks | Scenarios | Images | Instructions | Avg. Images/Instructions | Avg. Words/Instruction |
| ------- | ----- | --------- | ------ | ------------ | ------------------------ | ---------------------- |
| I4-Core | 29    | 19        | 62,813 | 18,176        | 3.46                     | 92.69                     |
| I4-Full | 31    | 20        | 1,769,744 |  477,716 | 3.70 | 97.58 |

## Benchmark Construction

### Data Format
All task instances are given to the models in a unified instruction-response form to easily achieve zero-shot generalization on various tasks. Formally, each instance in I4 is composed of the following components:
- *Task_Instruction*: provides a complete natural language definition of a given task, including the input/output format and the task objective.
- *Task_Instance*: is a concrete sample of a given task that consists of interleaved image-text sequential context (e.g., visually-rich textbooks and webpages, specific questions about the context).
- *Response*: represents the target output in natural language for a given task instruction and task instance. For classification tasks, we convert the class labels as options into the instruction and ask the model to output the option index in natural language as repsonse.

Without any specific emphasis, we use the term *instruction* to refer to the combination of *Task_Instruction* and *Task_Instance*. For each task, we manually design 10 instruction templates in natural language to increase the diversity.

### Task Collection and Categorization
To comprehensively benchmark the interleaved vision-language instruction-following ability, we extensively gather a wide variety of multi-modal datasets from different fields and scenarios. Our I4 benchmark covers 31 tasks of 7 categories across various scenarios (i.e., surveillance, webpage, industrial, cartoon, etc.). Note that some datasets (i.e., ALFRED, VISION, OCR-VQA) are not originally proposed for the task that involves interleaved image-text sequences. To further increase task diversity, we meticulously design certain rules to transform them to desired tasks, strictly following the original annotation information.

## Evaluation Protocols
Thanks to the unified task format of I4, all tasks can be evaluated in a zero-shot manner. For the open-ended generation tasks, we adopt *ROUGE-L* for evaluation. For the tasks that require the models to output option indexes, we take the *Accuracy* as the evaluation metric. While well-formated options are provided, we empirically observe that many MLLMs struggle to strictly follow instructions to output the option indexes but generate free-form text. Thus, when models do not exactly output the required options, we match their outputs to one of the given options based on the TF-IDF distance, which we find is more robust than model-based methods (ChatGPT and SentenceBERT).
Since we explore quantities of tasks, we take maximally 500 instances per task for evaluation efficiency and exclude several datasets that are difficult to obtain and are subject to strict copyright restrictions (referred as **I4-Core**). Meanwhile, we report the full version of the benchmark to facilitate future research on large-scale multi-modal instruction tuning (referred as **I4-Full**). 

## Evaluation Result

| Model            | Version         | Multi Modal Dialogue | Visual Story Telling List | Visual Relation Inference | Multi Modal Cloze | Knowledge Grounded QA | Text Rich Images QA | Multi Image Reasoning |
| ---------------- | --------------- | -------------------- | ------------------------- | ------------------------- | ----------------- | --------------------- | ------------------- | --------------------- |
| BLIP-2           | vicuna-7b        | 11.96                | 20.10                     | 3.67                      | 18.25             | 39.73                 | 30.53               | 39.53                 |
| InstructBlip     | vicuna-7b       | 33.58                | 24.41                    | 11.49                    | 21.20             | 47.40                 | 44.40            | 48.55                 |
| LLaMA-Adapter V2 | llama-7b        | 14.22                | 17.57                    | 13.51                     | 18.00             | 44.80                 | 32.00               | 44.03                 |
| LLaVA            | vicuna-7b       | 7.79                 | 10.70                   | 8.27                      | 15.85             | 36.20                 | 28.33               | 41.53                 |
| MiniGPT-4        | vicuna-7b       | 13.70                | 17.07                     | 7.95                      | 16.60             | 30.27                 | 26.40               | 43.50                 |
| mPLUG-Owl        | llama-7b        | 12.67                | 19.33                     | 5.40                      | 16.25             | 33.27                 | 32.47               | 42.50                 |
| OpenFlamingo     | llama-7b        | 16.88                | 24.22                    | 13.85                     | 21.65             | 32.00                 | 30.60               | 41.63                 |
| Otter            | llama-7b        | 15.37                | 15.57                     | 11.39                     | 16.00             | 41.67                 | 27.73               | 43.85                |
| Cheetah          | llama-2-7b-chat | **42.70**            | 24.76                   | 25.50                     | **22.95**         | **51.00**             | **44.93**           | 48.68                 |
| Cheetah          | vicuna-7b       | 37.50                | **25.20**                 | **25.90**                 | 22.15           | 48.60                | **44.93**            | **50.28**           |

## Contact
If you want to update your model in I4-Benchmark, feel free to contact us via email zhiqige2000@gmail.com.

## License
The I4-Benchmark is released under the [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode) license.