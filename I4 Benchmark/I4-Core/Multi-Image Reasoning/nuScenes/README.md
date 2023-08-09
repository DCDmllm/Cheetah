# nuScenes

The original nuScenes dataset is a public large-scale dataset for autonomous driving developed by the team at Motional. Authors of paper [Visual Question Answering on Image Sets](https://arxiv.org/abs/2008.11976) furthur added question-answer annotations for a scene from several annotators using Amazon Mechanical Turk. We reorgnize the dataset into a multi-choice question answering task with the help of ChatGPT.

Source: 
- [nuScenes: A multimodal dataset for autonomous driving](https://arxiv.org/abs/1903.11027)
- [Visual Question Answering on Image Sets](https://arxiv.org/abs/2008.11976)
## Metadata

```json
{
    "dataset": "nuScenes",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "Given six images taken from different cameras on a street view car, your task is to answer questions about the depicted scene. You must choose your answer from the Choice List. ",
        "Upon receiving six photographs captured from various cameras on a street-view car, your responsibility is to provide accurate responses to questions about the scene. You must choose your answer from the Choice List. ",
        "Using six pictures taken from distinct cameras mounted on a street view car, your task is to answer queries about the presented scenario. You must choose your answer from the Choice List. ",
        "With six images from multiple cameras on a street view car provided, your job is to answer questions pertaining to the scene. You must choose your answer from the Choice List. ",
        "Given six pictures captured from different angles on a street view car, your duty is to respond accurately to questions about the depicted scene. You must choose your answer from the Choice List. ",
        "Presented with six images from various cameras on a street view car, your responsibility is to answer inquiries about the scene. You must choose your answer from the Choice List. ",
        "Using six photographs from multiple cameras on a street-view vehicle, your job is to provide answers to the questions about the scene. You must choose your answer from the Choice List. ",
        "Given a collection of six images taken from different cameras on a street view car, your task is to respond to the questions about the scenario. You must choose your answer from the Choice List. ",
        "With six images, each from a different camera on a street-view car, your assignment is to answer questions about the scene. You must choose your answer from the Choice List. ",
        "Upon viewing six pictures captured from various cameras on a street view vehicle, your role is to answer questions about the presented scene. You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 4,
    "task_instance": {
        "context": "{image#1}{image#2}{image#3}{image#4}{image#5}{image#6}Question: what is the shirt color of the man that is on the crosswalk?  Choice List:['yellow', 'blue', 'red', 'green'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg",
            "5.jpg"
        ]
    },
    "response": "red"
}
```
