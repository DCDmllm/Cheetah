# Spot-the-Diff
The original dataset is collected by crowd-sourcing difference descriptions for pairs of image frames extracted from video-surveillance footage. Annotators were asked to succinctly describe all the differences in a short paragraph. We reorgnize the orignal annotations to our style.

Source: 
- [Learning to Describe Differences Between Pairs of Similar Images](https://arxiv.org/abs/1808.10584)
## Metadata

```json
{
    "dataset": "Spot-the-Diff",
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
    "response": "person with umbrella is gone. person with red coat is moved. car up at top to left is now missing"
}
```
