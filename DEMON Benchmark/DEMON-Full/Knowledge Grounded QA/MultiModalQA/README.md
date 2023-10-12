# ManyModalQA

ManyModalQA is a challenging question answering dataset that requires joint reasoning over text, tables and images. For ease of use, table data is pre-converted and provided as PNG files. 

Source:
- [MultiModalQA: Complex Question Answering over Text, Tables and Images](https://arxiv.org/abs/2104.06039)

## Metadata

```json
{
    "dataset": "MultiModalQA",
    "split": "full",
    "num_sample": 4577,
    "task_instruction": [
        "Given a collection of relevant data, which includes images, text, and tables, your task is to respond accurately to the ensuing question. You must choose your answer from the Choice List. ",
        "Utilizing the information, including images, text, and tables that I provide, could you provide a correct answer to the following question? You must choose your answer from the Choice List. ",
        "With the aid of provided information like images, text, and tables, your assignment is to respond correctly to the question. You must choose your answer from the Choice List. ",
        "Based on the data provided, which includes various forms like images, text, and tables, please respond to the following query. You must choose your answer from the Choice List. ",
        "Using the relevant information I provide, which encompasses images, text, and tables, please accurately answer the question. You must choose your answer from the Choice List. ",
        "Considering the information in different formats I've provided you, could you formulate a correct response to the ensuing query? You must choose your answer from the Choice List. ",
        "Given a set of information including images, text, and tables, your task is to use this data to answer the subsequent question correctly. You must choose your answer from the Choice List. ",
        "Relying on the furnished information, which includes graphics, text, and tabular data, could you provide an accurate response to the following question? You must choose your answer from the Choice List. ",
        "With the amalgam of information provided, encompassing images, texts, and tables, please construct a correct answer to the following question. You must choose your answer from the Choice List. ",
        "Using the array of information, including imagery, textual data, and tables, could you provide an accurate answer to the posed question? You must choose your answer from the Choice List. "
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
        "context": "Global Table: {table#1} Context: {image#2} Question: What sports is the Ben Piazza 1976 movie title? Choice List:['soccer', 'baseball', 'basketball', 'football'] Your answer is:",
        "images_path": [
            "0.png",
            "1.jpg"
        ]
    },
    "response": "baseball"
}
```
