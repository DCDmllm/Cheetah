# nuScenes

The original Gibson dataset includes over 1400 floor spaces from 572 full buildings. Authors of paper [Visual Question Answering on Image Sets](https://arxiv.org/abs/2008.11976) furthur added question-answer annotations for a scene from several annotators using Amazon Mechanical Turk. We reorgnize the dataset into a multi-choice question answering task with the help of ChatGPT.
Due to the scrict license of Gibson dataset, we are not able to release the dataset. Please refer to the original paper for more details.

Source: 
- [Gibson Env: Real-World Perception for Embodied Agents](https://arxiv.org/abs/1808.10654)
- [Visual Question Answering on Image Sets](https://arxiv.org/abs/2008.11976)
## Metadata

```json
{
    "dataset": "Gibson",
    "split": "full",
    "num_sample": 91479,
    "task_instruction": [
        "Given six images taken from different cameras on a 360 camera, your task is to answer questions about the depicted scene. You must choose your answer from the Choice List. ",
        "Upon receiving six photographs captured from various cameras on a 360 camera, your responsibility is to provide accurate responses to questions about the scene. You must choose your answer from the Choice List. ",
        "Using six pictures taken from distinct cameras mounted on a 360 camera, your task is to answer queries about the presented scenario. You must choose your answer from the Choice List. ",
        "With six images from multiple cameras on a 360 camera provided, your job is to answer questions pertaining to the scene. You must choose your answer from the Choice List. ",
        "Given six pictures captured from different angles on a 360 camera, your duty is to respond accurately to questions about the depicted scene. You must choose your answer from the Choice List. ",
        "Presented with six images from various cameras on a 360 camera, your responsibility is to answer inquiries about the scene. You must choose your answer from the Choice List. ",
        "Using six photographs from multiple cameras on a 360 camera, your job is to provide answers to the questions about the scene. You must choose your answer from the Choice List. ",
        "Given a collection of six images taken from different cameras on a 360 camera, your task is to respond to the questions about the scenario. You must choose your answer from the Choice List. ",
        "With six images, each from a different camera on a 360 camera, your assignment is to answer questions about the scene. You must choose your answer from the Choice List. ",
        "Upon viewing six pictures captured from various cameras on a 360 camera, your role is to answer questions about the presented scene. You must choose your answer from the Choice List. "
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
        "context": "{image#1}{image#2}{image#3}{image#4}{image#5}{image#6}Question: what is the square chair below the windows color?  Choice List:['white', 'blue', 'red', 'green'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg",
            "5.jpg"
        ]
    },
    "response": "white"
}
```
