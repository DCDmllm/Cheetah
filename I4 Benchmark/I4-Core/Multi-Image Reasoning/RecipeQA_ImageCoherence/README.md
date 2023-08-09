# RecipeQA_ImageCoherence

The original RecipeQA dataset is for multimodal comprehension of cooking recipes. It comprises of approximately 20K instructional recipes with multiple modalities such as titles, descriptions and aligned set of images. Based on the annoations, we furthur design several challenging tasks which require multi-image reasoning to answer.

Source: 
- [A Challenge Dataset for Multimodal Comprehension of Cooking Recipes](https://arxiv.org/abs/1809.00812)
## Metadata

```json
{
    "dataset": "RecipeQA_ImageCoherence",
    "split": "core",
    "num_sample": 500,
    "task_instruction": [
        "Presented with a textual recipe tutorial, your task is to scrutinize it carefully and select the image that is incoherent in the provided sequence of images. You must choose your answer from the Choice List. ",
        "Given a text-based recipe guide, your responsibility is to meticulously review it and identify the image that doesn't fit in the following sequence of images. You must choose your answer from the Choice List. ",
        "Upon receiving a textual recipe tutorial, your job is to examine it attentively and choose the incoherent image in the subsequent image sequence. You must choose your answer from the Choice List. ",
        "Using a recipe tutorial composed entirely of text, your task is to scrutinize it and select the image that disrupts the continuity in the provided series of images. You must choose your answer from the Choice List. ",
        "With a text-based recipe tutorial at your disposal, your job is to thoroughly study it and pinpoint the image that is out of place in the following image sequence. You must choose your answer from the Choice List. ",
        "Provided with a textual recipe tutorial, your role is to closely inspect it and choose the image that doesn't align with the rest in the following sequence of images. You must choose your answer from the Choice List. ",
        "Given a recipe guide in textual format, your task is to carefully examine it and identify the incoherent image in the subsequent series of images. You must choose your answer from the Choice List. ",
        "Using a recipe tutorial written in text, your responsibility is to examine it carefully and select the incongruous image in the provided sequence of images. You must choose your answer from the Choice List. ",
        "With a text-only recipe tutorial at hand, your job is to attentively study it and choose the image that breaks the consistency in the following sequence of images. You must choose your answer from the Choice List. ",
        "Presented with a text-based recipe tutorial, your duty is to analyze it thoroughly and select the image that is inconsistent in the following series of images. You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 8,
    "task_instance": {
        "context": "Recipe: glow-in-the-dark-jello\nDetails: Step#1: Gather Your Supplies: You will need the following: *Jello (light-colored Jello such as Lemon or Lime will work best for this project) *16oz of tonic water *Stove *Liquid measuring cup *Small pot for boiling water *Mixing bowl *Mixing spoon *Refrigerator *Small Table Lamp with fluorescent blacklight (The blacklight must be fluorescent and not simply a colored bulb. \nStep#2: Measure Out Tonic Water: Measure out 8oz (1 cup) of tonic water in a liquid measuring cup. \nStep#3: Pour Tonic Water Into Pot: Pour tonic water into pot. \nStep#4: Turn Stove Burner on High: Put pot on burner and turn on high. \nStep#5: Pour Jello Packet Into Mixing Bowl: While water is boiling, pour Jello packet into mixing bowl. \nStep#6: Pour Boiling Water Into Mixing Bowl: Once water has boiled, pour the boiling tonic water into mixing bowl. \nStep#7: Stir Until Dissolved: Stir together Jello and boiling tonic water, making sure that the Jello powder fully dissolves. \nStep#8: Add Cold Water: Add one cup of cold tap water to the mixing bowl. \nStep#9: Chill in Fridge: Place the mixing bowl in the fridge and chill for four hours. \nStep#10: Remove and Test With Blacklight: After four hours, remove from fridge. \nRecipe Image Series: {image#1} {image#2} {image#3} {image#4}\nChoice List:['Image A: {image#5}', 'Image B: {image#6}', 'Image C: {image#7}', 'Image D: {image#8}']The incoherent image is:",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg",
            "5.jpg",
            "6.jpg",
            "7.jpg"
        ]
    },
    "response": "Image B"
}
```
