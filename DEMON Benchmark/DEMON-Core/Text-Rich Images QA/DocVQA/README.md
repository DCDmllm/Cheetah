# DocVQA

This original dataset consists of 50,000 questions defined on 12,000+ document images. Based on the annoations, we furthur design several challenging tasks which require multi-image reasoning to answer.

Source: 
- [DocVQA: A Dataset for VQA on Document Images](https://arxiv.org/abs/2007.00398)
## Metadata

```json
{
    "dataset": "DocVQA",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "I will give you some pictures, and each group of pictures will correspond to a question. Please answer it briefly. You must choose your answer from the Choice List. ",
        "For each group of pictures, there is a question. Please give a short answer to it. You must choose your answer from the Choice List. ",
        "Please answer briefly the question that corresponds to each group of pictures. You must choose your answer from the Choice List. ",
        "Each group of pictures has a related question. Please give a brief answer to it. You must choose your answer from the Choice List. ",
        "There is a question for each group of pictures. Please answer it in a short way. You must choose your answer from the Choice List. ",
        "Please give a short answer to the question that is related to each group of pictures. You must choose your answer from the Choice List. ",
        "For every group of pictures, there is a corresponding question. Please answer it briefly. You must choose your answer from the Choice List. ",
        "Each group of pictures relates to a question. Please give a brief answer to it. You must choose your answer from the Choice List. ",
        "There is a related question for each group of pictures. Please answer it shortly. You must choose your answer from the Choice List. ",
        "Please answer shortly the question that relates to each group of pictures. You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 1,
    "task_instance": {
        "context": "{image#1}{image#2}Question: what is purchase order no ?   Choice List:['99- 19686', '99-19688', '99-19685', '99-19687'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg"
        ]
    },
    "response": "99- 19686"
}
```
