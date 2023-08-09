# CLEVR-Change

The CLEVR-Change dataset is built upon the CLEVR engine, with 5 types of scene changes. We reorgnize the orignal annotations to our style.

Source: 
- [Robust Change Captioning](https://arxiv.org/abs/1901.02527)
- [Image Change Captioning by Learning from an Auxiliary Task](https://ieeexplore.ieee.org/document/9577664)
## Metadata

```json
{
    "dataset": "CLEVR-Change",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "What's the difference between 2 images? ",
        "Identify the alterations between these two images. ",
        "What modifications can be observed between these two pictures? ",
        "What has changed from the first image to the second? ",
        "Point out the variations between the two images. ",
        "Describe the contrast between these two images. ",
        "What distinguishes these two images? ",
        "Can you highlight the differences in these two pictures? ",
        "Identify the transformations in the second image compared to the first. ",
        "Explain the disparities between the first and second image. "
    ],
    "question_type": "open-ended"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 9,
    "task_instance": {
        "context": "{image#1}{image#2}Difference:",
        "images_path": [
            "0.jpg",
            "1.jpg"
        ]
    },
    "response": "the tiny cylinder changed to brown. the tiny object became brown. the small purple rubber cylinder in front of the blue cube turned brown. the small thing turned brown. the purple thing turned brown. the tiny purple thing changed to brown. the small purple matte cylinder to the left of the big metallic sphere turned brown. the small purple matte cylinder in front of the blue metallic block became brown. the small purple matte cylinder in front of the big cube became brown"
}
```
