# OCR-VQA

The original OCR-VQA dataset contains 207572 images and associated question-answer pairs. Based on the annoations, we furthur design several challenging tasks which require multi-image reasoning to answer.

Source: 
- [OCR-VQA: Visual Question Answering by Reading Text in Images](https://ieeexplore.ieee.org/document/8978122)
## Metadata

```json
{
    "dataset": "OCR-VQA",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "I will give you two pictures of the book cover. Please look at the pictures and answer a question You must choose your answer from the Choice List. ",
        "I will provide you with two images of the book cover. Please examine the images and answer a question. You must choose your answer from the Choice List. ",
        "I will give you two pictures of the book cover. Please look at the pictures and answer a question. You must choose your answer from the Choice List. ",
        "I will show you two photos of the book cover. Please review the photos and answer a question. You must choose your answer from the Choice List. ",
        "I will present you with two snapshots of the book cover. Please inspect the snapshots and answer a question. You must choose your answer from the Choice List. ",
        "I will display two visuals of the book cover. Please observe the visuals and answer a question. You must choose your answer from the Choice List. ",
        "I will share two graphics of the book cover. Please analyze the graphics and answer a question. You must choose your answer from the Choice List. ",
        "I will upload two illustrations of the book cover. Please scrutinize the illustrations and answer a question. You must choose your answer from the Choice List. ",
        "I will send you two screenshots of the book cover. Please examine the screenshots and answer a question. You must choose your answer from the Choice List. ",
        "I will provide you with two depictions of the book cover. Please evaluate the depictions and answer a question. You must choose your answer from the Choice List. "
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
        "context": "{image#1}{image#2}Question: Are the authors of these two books the same? Choice List:['not the same', 'David W. Beskeen', 'Stephan Van Dam', 'Sally M. Walker'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg"
        ]
    },
    "response": "Stephan Van Dam"
}
```
