# VIST

This dataset includes 81,743 unique photos in 20,211 sequences, aligned to both descriptive (caption) and story language. We reorgnize the orignal annotations to our style.

Source: [Visual Storytelling](https://arxiv.org/abs/1604.03968)

## Metadata

```json
{
    "dataset": "VIST",
    "split": "full",
    "num_sample": 26126,
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
        "context": "{image#1}Caption#1:The local parish holds a craft show each year.{image#2}Caption#2:Lots of folks come out and set up tables to sell their crafts.{image#3}Caption#3:Some of these crafts are very unique and take a lot of talent to make.{image#4}Caption#4:Folks of all ages come out to peruse the crafts for sale.{image#5}Caption#5:",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg"
        ]
    },
    "response": "Some of the crafters even dress up in unique costumes as part of their selling act."
}
```
