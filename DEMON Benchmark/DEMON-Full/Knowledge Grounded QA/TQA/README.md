# TQA

The TextbookQuestionAnswering (TQA) dataset is drawn from middle school science curricula. The context needed to answer questions is provided and composed of both text and images.

Source: 
- [Are You Smarter Than a Sixth Grader? Textbook Question Answering for Multimodal Machine Comprehension](https://ieeexplore.ieee.org/document/8100054)
## Metadata

```json
{
    "dataset": "TQA",
    "split": "full",
    "num_sample": 9786,
    "task_instruction": [
        "Provided with a series of diagrams from a textbook, your responsibility is to correctly answer the following question. You must choose your answer from the Choice List.",
        "Using a selection of textbook diagrams, your task is to provide an accurate response to the subsequent query. You must choose your answer from the Choice List.",
        "With a set of diagrams extracted from a textbook, your role is to answer the ensuing question correctly. You must choose your answer from the Choice List.",
        "Given an assortment of diagrams from a textbook, please provide an accurate response to the next question. You must choose your answer from the Choice List.",
        "Based on a series of diagrams from a textbook, your job is to correctly answer the forthcoming question. You must choose your answer from the Choice List.",
        "Using a collection of textbook diagrams as your reference, please respond accurately to the following query. You must choose your answer from the Choice List.",
        "Given various diagrams sourced from a textbook, your duty is to accurately answer the subsequent question. You must choose your answer from the Choice List.",
        "Using the textbook diagrams provided, your task is to correctly answer the ensuing query. You must choose your answer from the Choice List.",
        "Upon reviewing a collection of diagrams from a textbook, your job is to accurately respond to the following question. You must choose your answer from the Choice List.",
        "Given a set of diagrams from a textbook, your responsibility is to provide a correct response to the next query. You must choose your answer from the Choice List."
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 2,
    "task_instance": {
        "context": "{image#1}{image#2}Question: What produces ozone? Choice List:['Sun','Oxygen','Hydrogen','Carbon'] Your answer is: ",
        "images_path": [
            "0.png",
            "1.png"
        ]
    },
    "response": "Oxygen"
}
```
