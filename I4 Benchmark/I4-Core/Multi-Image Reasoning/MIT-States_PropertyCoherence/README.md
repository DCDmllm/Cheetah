# MIT-States_PropertyCoherence

The original dataset contains objects, scenes, and materials, each of which is found in a variety of transformed states. Based on the annoations, we furthur design several challenging tasks which require multi-image reasoning to answer.

Source: 
- [Discovering States and Transformations in Image Collections](http://web.mit.edu/phillipi/Public/states_and_transformations/index.html)

## Metadata
```json
{
    "dataset": "MIT-States_PropertyCoherence",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "Are the following four images of the same class?  You must choose your answer from the Choice List. ",
        "Do the following four images belong to the same category?  You must choose your answer from the Choice List. ",
        "Are these four images of the same kind?  You must choose your answer from the Choice List. ",
        "Do these four images share the same class?  You must choose your answer from the Choice List. ",
        "Are the four images below from the same group?  You must choose your answer from the Choice List. ",
        "Do the four images underneath have the same type?  You must choose your answer from the Choice List. ",
        "Are these four pictures of the same sort?  You must choose your answer from the Choice List. ",
        "Do these four pictures fall into the same category?  You must choose your answer from the Choice List. ",
        "Are the four pictures below of the same kind?  You must choose your answer from the Choice List. ",
        "Do the four pictures underneath belong to the same class?  You must choose your answer from the Choice List. ",
        "Are the following two similar images described by the same adjective?  You must choose your answer from the Choice List. ",
        "Do the following two similar images have the same adjective?  You must choose your answer from the Choice List. ",
        "Are these two images that look alike described by the same word?  You must choose your answer from the Choice List. ",
        "Do these two images that are similar share the same adjective?  You must choose your answer from the Choice List. ",
        "Are the two images below that resemble each other described by the same term?  You must choose your answer from the Choice List. ",
        "Do the two images underneath that are alike have the same word?  You must choose your answer from the Choice List. ",
        "Are these two pictures that look similar described by the same adjective?  You must choose your answer from the Choice List. ",
        "Do these two pictures that are similar share the same word?  You must choose your answer from the Choice List. ",
        "Are the two pictures below that resemble each other described by the same term?  You must choose your answer from the Choice List. ",
        "Do the two pictures underneath that are alike have the same adjective?  You must choose your answer from the Choice List. ",
        "Q:What do the following two pictures describe as opposite?  You must choose your answer from the Choice List. ",
        "Q:What is the opposite word that the following two pictures illustrate?  You must choose your answer from the Choice List. ",
        "Q:What is the word that the following two images show as opposite?  You must choose your answer from the Choice List. ",
        "Q:What is the opposite term that these two pictures demonstrate?  You must choose your answer from the Choice List. ",
        "Q:What is the term that these two images display as opposite?  You must choose your answer from the Choice List. ",
        "Q:What is the opposite adjective that the two pictures below depict?  You must choose your answer from the Choice List. ",
        "Q:What is the adjective that the two images below present as opposite?  You must choose your answer from the Choice List. ",
        "Q:What is the opposite word that the two pictures underneath illustrate?  You must choose your answer from the Choice List. ",
        "Q:What is the word that the two images underneath show as opposite?  You must choose your answer from the Choice List. ",
        "Q:What is the opposite term that these two photos demonstrate?  You must choose your answer from the Choice List. "
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
