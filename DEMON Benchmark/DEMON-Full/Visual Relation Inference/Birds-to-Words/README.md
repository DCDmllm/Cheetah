# Birds-to-Words

The original dataset is of 41k sentences describing fine-grained differences between photographs of birds. The language collected is highly detailed, while remaining understandable to the everyday observer (e.g., "heart-shaped face," "squat body"). We reorgnize the orignal annotations to our style.

Source: 
- [Neural Naturalist: Generating Fine-Grained Image Comparisons](https://arxiv.org/abs/1909.04101)
## Metadata

```json
{
    "dataset": "Birds-to-Words",
    "split": "full",
    "num_sample": 14381,
    "task_instruction": [
        "What's the difference between 2 birds? ",
        "Identify the alterations between these two birds. ",
        "What modifications can be observed between these two birds? ",
        "Name all the differences between these two birds.",
        "Point out the variations between the two birds. ",
        "Describe the contrast between these two birds. ",
        "What distinguishes these two birds? ",
        "Can you highlight the differences in these two birds? ",
        "Identify the transformations in the second bird compared to the first. ",
        "Explain the disparities between the first and second bird. "
    ],
    "question_type": "open-ended"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 7,
    "task_instance": {
        "context": "{image#1}{image#2}Difference:",
        "images_path": [
            "0.jpg",
            "1.jpg"
        ]
    },
    "response": "animal1 has a black head while animal2 has a red head . animal1 has a skinny black beak while animal2 has a thicker red beak . animal1 has green wings compared to animal2 which has red wings . animal1 has a red belly and animal2 has a yellow belly ."
}
```
