# SlideVQA

This original SlideVQA, containing 2.6k+ slide decks composed of 52k+ slide images and 14.5k questions about a slide deck. SlideVQA requires complex reasoning, including single-hop, multi-hop, and numerical reasoning, and also provides annotated arithmetic expressions of numerical answers for enhancing the ability of numerical reasoning. We reorgnize the orignal annotations to our style.

Source: 
- [SlideVQA: A Dataset for Document Visual Question Answering on Multiple Images](https://arxiv.org/abs/2301.04883)
## Metadata

```json
{
    "dataset": "SlideVQA",
    "split": "full",
    "num_sample": 1987,
    "task_instruction": [
        "I will give you several slides and a question, your job is to seek information in the slide and answer the question correctly. You must choose your answer from the Choice List. ",
        "Based on the slides, please answer the following question. You must choose your answer from the Choice List. ",
        "Given the provided slides and a question, your task is to derive information from the slides and respond to the question accurately. You must choose your answer from the Choice List. ",
        "Based on the content within these slides, could you provide an answer to the ensuing question? You must choose your answer from the Choice List. ",
        "Upon reviewing several slides, your task is to extract the necessary information and answer the given question. You must choose your answer from the Choice List. ",
        "Please examine the slides closely and provide a suitable response to the question that follows. You must choose your answer from the Choice List. ",
        "Having viewed the slides, can you use the information presented to answer the following question? You must choose your answer from the Choice List. ",
        "Please analyze the data in these slides and accordingly answer the proposed question. You must choose your answer from the Choice List. ",
        "Using the slides as your reference, please respond to the following question. You must choose your answer from the Choice List. ",
        "Examine the slides carefully, and then answer the question based on the information gleaned. You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 7,
    "task_instance": {
        "context": "{image#1}{image#2}Question: Which takes less Processing Time, the solution that is a mature, supported product or Spark? Choice List:['Spark', 'the solution that is a mature, supported product', 'a solution that is new and untested', 'the solution that is more expensive'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg"
        ]
    },
    "response": "Spark"
}
```
