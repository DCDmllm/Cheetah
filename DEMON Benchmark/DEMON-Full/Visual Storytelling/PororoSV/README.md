# PororoSV

The original Pororo dataset contains 16K clips of one second videos about 13 distinct characters. The manually written description has an average length of 13.6 words that describes what is happening and which characters are in each video clip. These 16K video clips are sorted into 408 movie stories. We randomly select 5 frames from video and reorganize the annotations to our style.

Source: 
- [StoryGAN: A Sequential Conditional GAN for Story Visualization](https://arxiv.org/abs/1812.02784)
## Metadata

```json
{
    "dataset": "PororoSV",
    "split": "full",
    "num_sample": 12399,
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
        "context": "{image#1}Caption#1: there is a house and many trees{image#2}Caption#2: Loopy puts cherry on a pie. Loopy is done with the pie.{image#3}Caption#3: Loopy puts pie on the table. Loopy looks very happy. There are bread a book apples and a pie on the table.{image#4}Caption#4: Loopy tastes pie and Loopy thinks it is delicious. Loopy turns over the page.{image#5}Caption#5:",
        "images_path": [
            "0.png",
            "1.png",
            "2.png",
            "3.png",
            "4.png"
        ]
    },
    "response": " Loopy marvels at the picture on the book. Loopy eats a piece of pie."
}
```
