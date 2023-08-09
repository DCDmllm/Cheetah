# MIT-States_StateCoherence

The original dataset contains objects, scenes, and materials, each of which is found in a variety of transformed states. Based on the annoations, we furthur design several challenging tasks which require multi-image reasoning to answer.

Source: 
- [Discovering States and Transformations in Image Collections](http://web.mit.edu/phillipi/Public/states_and_transformations/index.html)
## Metadata

```json
{
    "dataset": "MIT-States_StateCoherence",
    "split": "full",
    "num_sample": 2000,
    "task_instruction": [
        "I will provide you with two sets of pictures, each of which shows an object in the opposite state. Can you tell me if the states of these two sets of pictures are the same? You must choose your answer from the Choice List. ",
        "I have two sets of pictures that show an object in opposite states. Can you tell me if the states of these two sets of pictures are the same? You must choose your answer from the Choice List. ",
        "I will give you two sets of pictures, each of which depicts an object in its opposite state. Can you tell me if the states of these two sets of pictures are the same? You must choose your answer from the Choice List. ",
        "I have two sets of pictures that depict an object in its opposite state. Can you tell me if the states of these two sets of pictures are the same? You must choose your answer from the Choice List. ",
        "I will show you two sets of pictures, each showing an object in its opposite state. Can you tell me if the states of these two sets of pictures are the same? You must choose your answer from the Choice List. ",
        "I have two sets of pictures that show an object in its opposite state. Can you tell me if the states of these two sets of pictures are identical? You must choose your answer from the Choice List. ",
        "I will provide you with two sets of pictures, each showing an object in its opposite state. Can you tell me if the states of these two sets of pictures are identical? You must choose your answer from the Choice List. ",
        "I have two sets of pictures that depict an object in its opposite state. Can you tell me if the states of these two sets of pictures are identical? You must choose your answer from the Choice List. ",
        "I will show you two sets of pictures, each depicting an object in its opposite state. Can you tell me if the states of these two sets of pictures are identical? You must choose your answer from the Choice List. ",
        "I have two sets of pictures that depict an object in its opposite state. Can you tell me if the states of these two sets of pictures are the same? You must choose your answer from the Choice List. "
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
        "context": "{image#1}{image#2}{image#3}{image#4}Choice List:['True', 'False'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg",
            "3.jpg"
        ]
    },
    "response": "True"
}
```
