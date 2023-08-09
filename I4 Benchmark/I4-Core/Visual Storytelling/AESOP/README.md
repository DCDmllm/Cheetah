# AESOP

AESOP is a new dataset that captures the creative process associated with visual storytelling. Visual panels are composed of clip-art objects with specific attributes enabling a broad range of creative expression. We reorgnize the orignal annotations to our style.

Source: 
- [Abstract Encoding of Stories, Objects, and Pictures](https://ieeexplore.ieee.org/document/9710625)
## Metadata

```json
{
    "dataset": "AESOP",
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
    "task_instruction_id": 3,
    "task_instance": {
        "context": "{image#1}Caption#1:Colin loved watching sports on the TV. He loved watching the various soccer clubs of the Major League soccer play. He wished he could learn how to play soccer and be a star.{image#2}Caption#2:One day, his dad, Jared who was also an avid soccer fan brought home a soccer ball. Colin was very excited. He mused about the opportunity of learning how to play soccer.{image#3}Caption#3:",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg"
        ]
    },
    "response": "Every day, Colin would go to the park to practice playing soccer with his friends, Bobby and Lizzy, and have fun until he became very good at playing soccer."
}
```
