# Fashion200K

The original dataset contains more than 200,000 clothing images of five categories (dress, top, pants, skirt and jacket) and their associated product descriptions from online shopping websites. Based on the annoations, we furthur design several challenging tasks which require multi-image reasoning to answer.

Source: 
- [Automatic Spatially-aware Fashion Concept Discovery](https://arxiv.org/abs/1708.01311)
## Metadata

```json
{
    "dataset": "Fashion200K",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "Dress or any top with pants can combine a suit. Q:How many suit can the following five pictures combine?  You must choose your answer from the Choice List. ",
        "Dress or any top with pants can combine a suit. Q:What is the total number of combinations that can be made from five clothing?  You must choose your answer from the Choice List. ",
        "Dress or any top with pants can combine a suit. Q:What is the number of possible combinations that can be made from five clothing?  You must choose your answer from the Choice List. ",
        "Dress or any top with pants can combine a suit. Q:How many ways can you combine a suit?  You must choose your answer from the Choice List. ",
        "Dress or any top with pants can combine a suit. Q:What is the total number of ways to combine a suit?  You must choose your answer from the Choice List. ",
        "Dress or any top with pants can combine a suit. Q:How many different ways can you combine a suit?  You must choose your answer from the Choice List. ",
        "Dress or any top with pants can combine a suit. Q:What is the total number of possible combinations that can be made from five clothing?  You must choose your answer from the Choice List. ",
        "Dress or any top with pants can combine a suit. Q:How many different possible combinations can be made from five clothing?  You must choose your answer from the Choice List. ",
        "Dress or any top with pants can combine a suit. Q:What is the total number of ways to arrange a suit?  You must choose your answer from the Choice List. ",
        "Dress or any top with pants can combine a suit. Q:How many different ways can you arrange a suit?  You must choose your answer from the Choice List. ",
        "Are the clothes in these four pictures the same color?  You must choose your answer from the Choice List. ",
        "Do these four pictures show the same color of clothes?  You must choose your answer from the Choice List. ",
        "Are the clothes in these four pictures the same hue?  You must choose your answer from the Choice List. ",
        "Is the color of the clothes in these four pictures identical?  You must choose your answer from the Choice List. ",
        "Do the clothes in these four pictures have the same color?  You must choose your answer from the Choice List. ",
        "Are the colors of the clothes in these four pictures identical?  You must choose your answer from the Choice List. ",
        "Is the hue of the clothes in these four pictures the same?  You must choose your answer from the Choice List. ",
        "Do these four pictures depict clothes of the same color?  You must choose your answer from the Choice List. ",
        "Are the colors of the clothes in these four pictures consistent?  You must choose your answer from the Choice List. ",
        "Is there any difference in color between the clothes in these four pictures?  You must choose your answer from the Choice List. ",
        "Do the following two clothes belong to the same dressing style?  You must choose your answer from the Choice List. ",
        "Are these two clothes part of the same fashion style?  You must choose your answer from the Choice List. ",
        "Do these two clothes match the same style of dressing?  You must choose your answer from the Choice List. ",
        "Is this pair of clothes in the same style category?  You must choose your answer from the Choice List. ",
        "Do these two clothes have the same fashion sense?  You must choose your answer from the Choice List. ",
        "Are these two clothes similar in their style of dress?  You must choose your answer from the Choice List. ",
        "Do these two clothes follow the same style trend?  You must choose your answer from the Choice List. ",
        "Is this a matching pair of clothes in terms of style?  You must choose your answer from the Choice List. ",
        "Do these two clothes share the same style theme?  You must choose your answer from the Choice List. ",
        "Are these two clothes consistent with the same style of fashion?  You must choose your answer from the Choice List. ",
        "Are the following three pictures the same type of clothing?  You must choose your answer from the Choice List. ",
        "Do these three pictures belong to the same category of clothing?  You must choose your answer from the Choice List. ",
        "Are these three pictures of clothes in the same style?  You must choose your answer from the Choice List. ",
        "Do these three pictures show clothes that have the same fashion theme?  You must choose your answer from the Choice List. ",
        "Are these three pictures of clothes that match the same dressing style?  You must choose your answer from the Choice List. ",
        "Do these three pictures represent the same type of clothes?  You must choose your answer from the Choice List. ",
        "Are these three pictures of clothes that share the same style criteria?  You must choose your answer from the Choice List. ",
        "Do these three pictures display clothes that fit the same style trend?  You must choose your answer from the Choice List. ",
        "Are these three pictures of clothes that are similar in their style of dress?  You must choose your answer from the Choice List. ",
        "Are these three pictures of clothes that are consistent with the same style of fashion?  You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
},
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 1,
    "task_instance": {
        "context": "{image#1}{image#2}{image#3}{image#4}{image#5}Choice List:['0','1','2','3','4','5','6'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg"
        ]
    },
    "response": 4
}
```
