# WebQA

WebQA mirrors the way humans use the web: 1) Ask a question, 2) Choose sources to aggregate, and 3) Produce a fluent language response. For ease of use, we provide the ground truth knowledge sources as context. 

Source: 
- [WebQA: Multihop and Multimodal QA](https://arxiv.org/abs/2109.00590)
## Metadata

```json
{
"metadata": {
    "dataset": "WebQA",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "I will give you several images and a question, your job is to seek information in the slide and answer the question correctly. You must choose your answer from the Choice List. ",
        "Based on the images, please answer the following question. You must choose your answer from the Choice List. ",
        "Given the provided images and a question, your task is to derive information from the images and respond to the question accurately. You must choose your answer from the Choice List. ",
        "Based on the content within these images, could you provide an answer to the ensuing question? You must choose your answer from the Choice List. ",
        "Upon reviewing several images, your task is to extract the necessary information and answer the given question. You must choose your answer from the Choice List. ",
        "Please examine the images closely and provide a suitable response to the question that follows. You must choose your answer from the Choice List. ",
        "Having viewed the images, can you use the information presented to answer the following question? You must choose your answer from the Choice List. ",
        "Please analyze the data in these images and accordingly answer the proposed question. You must choose your answer from the Choice List. ",
        "Using the images as your reference, please respond to the following question. You must choose your answer from the Choice List. ",
        "Examine the images carefully, and then answer the question based on the information gleaned. You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
},
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 0,
    "task_instance": {
        "context": "{image#1}Image Caption #1: Western Cottage pump organ {image#2}Image Caption #2: Wurlitzer Model 44 Electrostatic Reed Organ.png Question: On which organ, are more round visible stop knobs installed; Western Cottage pump organ or Wurlitzer Model 44 Electrostatic Reed Organ?   Choice List:['The Western Cottage pump organ and the Wurlitzer Model 44 Electrostatic Reed Organ have an equal number of round visible stop knobs installed.', 'The Wurlitzer Model 44 Electrostatic Reed Organ has more round visible stop knobs installed compared to the Western Cottage pump organ.', 'The Western Cottage pump organ has more round visible stop knobs installed compared to the Wurlitzer Model 44 Electrostatic Reed Organ.', 'The Wurlitzer Model 44 Electrostatic Reed Organ has the same number of round visible stop knobs installed as the Western Cottage pump organ.'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg"
        ]
    },
    "response": "The Western Cottage pump organ has more round visible stop knobs installed compared to the Wurlitzer Model 44 Electrostatic Reed Organ."
}
```
