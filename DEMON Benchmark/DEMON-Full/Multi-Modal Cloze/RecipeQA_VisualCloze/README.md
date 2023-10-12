# RecipeQA_VisualCloze

The original RecipeQA dataset is for multimodal comprehension of cooking recipes. It comprises of approximately 20K instructional recipes with multiple modalities such as titles, descriptions and aligned set of images. Based on the annoations, we furthur design several challenging tasks.

Source: 
- [A Challenge Dataset for Multimodal Comprehension of Cooking Recipes](https://arxiv.org/abs/1809.00812)
## Metadata

```json
{
    "dataset": "RecipeQA_VisualCloze",
    "split": "full",
    "num_sample": 8834,
    "task_instruction": [
        "Presented with a textual recipe tutorial, your task is to scrutinize it carefully and select the most suitable image to fill in the missing blank, thereby accurately completing the recipe image series. You must choose your answer from the Choice List. ",
        "Given a text-based recipe guide, your responsibility is to meticulously review it and choose the most fitting image to fill the missing gap, ensuring the recipe image series is completed correctly. You must choose your answer from the Choice List. ",
        "Upon receiving a textual recipe tutorial, your job is to examine it attentively and pick the most appropriate image to complete the missing section, effectively finalizing the recipe image sequence. You must choose your answer from the Choice List. ",
        "Using a recipe tutorial composed entirely of text, your task is to scrutinize it and select the most suitable image to fill in the blank space, thereby accurately finishing the recipe image series. You must choose your answer from the Choice List. ",
        "With a text-based recipe tutorial at your disposal, your job is to thoroughly study it and opt for the best image to fill the missing section, correctly rounding off the recipe image sequence. You must choose your answer from the Choice List. ",
        "Provided with a textual recipe tutorial, your role is to closely inspect it and choose the best image to fill in the blank, thereby correctly completing the recipe image series. You must choose your answer from the Choice List. ",
        "Given a recipe guide in textual format, your task is to carefully examine it and select the optimal image for the missing blank, thus correctly finalizing the recipe image series. You must choose your answer from the Choice List. ",
        "Using a recipe tutorial written in text, your responsibility is to examine it carefully and choose the best-suited image to fill the void, effectively completing the recipe image sequence. You must choose your answer from the Choice List. ",
        "With a text-only recipe tutorial at hand, your job is to attentively study it and select the most fitting image to complete the missing part, thereby correctly concluding the recipe image series. You must choose your answer from the Choice List. ",
        "Presented with a text-based recipe tutorial, your duty is to analyze it thoroughly and select the most apt image to fill in the missing blank, thereby accurately concluding the recipe image sequence. You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 7,
    "task_instance": {
        "context": "Recipe: drum-bbq-smoker-no-welding\nDetails: Step#1: Prep: First I sanded off the paint on the lid, I will sand the rest later (it's wet here)Using a piece of string I marked off a quarter, then made a rectangle for the lid 40mm in. \nStep#2: Cut Out the Lid: Using an angle grinder I cut out the lid, being careful at the corners. \nStep#3: Making the Lip: To stop the lid falling through I used two thin strips of stainless steel I had, but use what you have. \nStep#4: Add Hinges: I lined up the hinges and center punched and drilled two holes on each hinge at opposite corners. \nStep#5: Handle: For the handle I just used an old stainless steel cupboard door handle I had and drilled through the lid. \nStep#6: Making the Chimney: To make the chimney I used a turbo I had recently  changed on my Landrover as it had places to bolt through. \nStep#7: Grill Rack and Chimney: For grill racks I used threaded bar. \nStep#8: Frame: I just made a simple frame. \nStep#9: Finishing: I sanded it and used stove spray paint to give a satin black finish. \n\nRecipe Image Series: {image#1} {image#2} {image#3} UNKNOWN\nChoice List:['Image A: {image#4}', 'Image B: {image#5}', 'Image C: {image#6}', 'Image D: {image#7}']Your answer to replace 'UNKNOWN' is:",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg",
            "5.jpg",
            "6.jpg"
        ]
    },
    "response": "Image B"
}
```
