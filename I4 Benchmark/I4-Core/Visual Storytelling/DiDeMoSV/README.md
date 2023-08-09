# DiDemoSV
The original DiDeMoSV is collected from Flickr and the most common nouns indeed reflect this. Most of the captions are descriptive in that they describe the contents of the scene, the location of the objects/people in the scene, and the actions that are taking place in the scene. In DiDeMoSV, the focus is on the breadth of information that must be considered in the form of actions, objects, and settings. We reorgnize the orignal annotations to our style.

Source: 
- [StoryDALL-E: Adapting Pretrained Text-to-Image Transformers for Story Continuation](https://arxiv.org/abs/2209.06192)
## Metadata

```json
{
    "dataset": "DiDemoSV",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "Given the stories paired with the first several images, can you finish the story based on the last image?",
        "With the narratives paired with the initial images, how would you conclude the story using the last picture?",
        "Given the story so far from the first few images, can you complete the tale considering the final image?",
        "Based on the narratives associated with the initial images, use the final picture to bring the story to a close.",
        "Using the preceding stories paired with the images, can you draft the ending with reference to the last image?",
        "With the stories connected to the initial pictures, how would you write the climax based on the last picture?",
        "Taking the stories from the initial images into account, can you conclude the story using the elements of the final image?",
        "From the narratives given with the initial images,  write the conclusion using the final image",
        "Given the progression of the story with the first few images, can you write a fitting end considering the last image?",
        "Based on the stories accompanying the first images, can you devise a conclusion for the story that incorporates the last image?"
    ],
    "question_type": "open-ended"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 2,
    "task_instance": {
        "context": "{image#1}Caption#1:when the other cat walks into frame.{image#2}Caption#2:the cat laying on the rug jumps and lands on her other side..{image#3}Caption#3:",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg"
        ]
    },
    "response": "we see another cat walk behind a door."
}
```
