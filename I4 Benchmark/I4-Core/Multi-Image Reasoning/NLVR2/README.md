# NLVR2

NLVR2 is a dataset for joint reasoning about natural language and images, with a focus on semantic diversity, compositionality, and visual reasoning challenges.

Source: 
- [A Corpus for Reasoning About Natural Language Grounded in Photographs](https://arxiv.org/abs/1811.00491)
## Metadata

```json
{
    "dataset": "NLVR2",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "Presented with two images and a sentence that depicts their relation, your task is to determine if the sentence accurately describes the relationship. You must choose your answer from the Choice List. ",
        "Given two images and a sentence outlining their relation, your responsibility is to judge whether the sentence correctly describes the connection between them. You must choose your answer from the Choice List. ",
        "Upon receiving two images and a statement that illustrates their relation, your job is to decide whether the sentence correctly characterizes the relationship. You must choose your answer from the Choice List. ",
        "Using two images and a sentence that narrates their relationship, your task is to evaluate whether the sentence accurately portrays the link between them. You must choose your answer from the Choice List. ",
        "With two images and a sentence describing their interrelation at your disposal, your job is to assess whether the sentence correctly represents the connection between the images. You must choose your answer from the Choice List. ",
        "Provided with two images and a sentence describing their relationship, your role is to determine if the sentence accurately conveys the relation. You must choose your answer from the Choice List. ",
        "Given two images and a sentence explaining their association, your task is to judge if the sentence correctly communicates the relationship between them. You must choose your answer from the Choice List. ",
        "Using two images and a sentence that presents their correlation, your responsibility is to evaluate whether the sentence appropriately depicts the relation. You must choose your answer from the Choice List. ",
        "With two images and a sentence expressing their linkage at hand, your job is to decide whether the sentence correctly interprets the relationship between the images. You must choose your answer from the Choice List. ",
        "Presented with two images and a sentence that specifies their connection, your duty is to assess if the sentence accurately describes the relation. You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 3,
    "task_instance": {
        "context": "{image#1}{image#2}Relation: None of the gloves pictured are blackChoice List:['True','False']Answer: ",
        "images_path": [
            "0.png",
            "1.png"
        ]
    },
    "response": "True"
}
```
