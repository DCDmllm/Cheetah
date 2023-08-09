# Flintstones

The original Flintstones is a densely annotated dataset based on The Flintstones animated series, consisting of over 25000 videos, each 75 frames long. We randomly select 5 frames from video and reorganize the annotations to our style.

Source: 
- [Imagine this! scripts to compositions to videos](https://arxiv.org/abs/1804.03608)
## Metadata

```json
{
    "dataset": "Flintstones",
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
    "task_instruction_id": 8,
    "task_instance": {
        "context": "{image#1}Caption#1:Fred and Barney are having a conversation on the couch in the living room. Fred turns his head with a disdained look.{image#2}Caption#2:Fred and Barney are sitting in a room. Fred looks angry and sticks his tongue out while he and Barney are talking. {image#3}Caption#3:The circus performer on the television talks to his audience.{image#4}Caption#4:Fred is on tv in the room wearing a super hero outfit.{image#5}Caption#5:",
        "images_path": [
            "0.png",
            "1.png",
            "2.png",
            "3.png",
            "4.png"
        ]
    },
    "response": "FRED IS ON TV, SO APPARENTLY HE IS IN A LIVING ROOM.  HE IS WEARING WHAT APPEARS TO BE A SUPERHERO OUTFIT.  HE IS ALSO WEARING A MASK.  HIS HEAD IS TURNING FROM FRONT TO MY RIGHT.  HE IS TALKING."
}
```
