# IEdit
The original dataset is a new language-guided image editing dataset that contains a large number of real image pairs with corresponding editing instruction. We reorgnize the orignal annotations to our style.

Source: 
- [Expressing Visual Relationships via Language](https://arxiv.org/abs/1906.07689)
## Metadata

```json
{
    "dataset": "IEdit",
    "split": "full",
    "num_sample": 2000,
    "task_instruction": [
        "Please give a editing Request to describe the transformation from the source image to the target image.",
        "What is the correct image edit instruction that can transfrom the source image to target image?",
        "What editing actions would you suggest to modify the source image into the target image?",
        "Please provide instructions for editing the source image to match the target image.",
        "Describe the editing process to convert the source image to the target image.",
        "What editing procedures should be implemented to transition the source image into the target image?",
        "How can the source image be edited to resemble the target image?",
        "Please give directions for the necessary edits to morph the source image into the target image.",
        "What transformations must be applied to the source image to achieve the target image?",
        "Can you describe the editing process to transform the source image into the target image?"
    ],
    "question_type": "open-ended"
}
```

## Example

```json
{
        "sample_id": 0,
        "task_instruction_id": 1,
        "task_instance": {
            "context": "Source Image:{image#1} Target Image:{image#2}Instruction:",
            "images_path": [
                "0.jpg",
                "1.jpg"
            ]
        },
        "response": "take the people out of the back in the photo. Remove the two people behind the woman in the white dress and the man in the blue suit. remove people behind the couple in the centre"
    }
```
