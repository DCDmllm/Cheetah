# RecipeQA_TextCloze

The original RecipeQA dataset is for multimodal comprehension of cooking recipes. It comprises of approximately 20K instructional recipes with multiple modalities such as titles, descriptions and aligned set of images. Based on the annoations, we furthur design several challenging tasks.

Source: 
- [A Challenge Dataset for Multimodal Comprehension of Cooking Recipes](https://arxiv.org/abs/1809.00812)
## Metadata

```json
{
    "dataset": "RecipeQA_TextCloze",
    "split": "full",
    "num_sample": 9761,
    "task_instruction": [
        "Presented with a recipe tutorial interwoven with text and images, your task is to scrutinize it carefully and select the most suitable text to fill in the missing blank, thereby accurately completing the recipe summary. You must choose your answer from the Choice List. ",
        "Given a recipe guide interspersed with text and images, your responsibility is to meticulously review it and choose the best fitting text to complete the missing section, ensuring the recipe summary is correct. You must choose your answer from the Choice List. ",
        "Upon receiving an image-text interleaved recipe tutorial, your job is to examine it attentively and pick the most appropriate text to fill in the missing gap, effectively completing the recipe summary. You must choose your answer from the Choice List. ",
        "Using a recipe tutorial comprised of alternating text and images, your task is to scrutinize it and select the most suitable wording to fill in the blank space, thereby accurately finalizing the recipe summary. You must choose your answer from the Choice List. ",
        "With an image-text combined recipe tutorial at your disposal, your job is to thoroughly examine it and opt for the best text to fill the missing section, correctly rounding off the recipe summary. You must choose your answer from the Choice List. ",
        "Provided with a recipe tutorial intermingled with images and text, your role is to closely inspect it and choose the best text to fill in the blank, thereby correctly completing the recipe overview. You must choose your answer from the Choice List. ",
        "Given a recipe tutorial integrated with text and images, your task is to carefully study it and select the optimal text for the missing blank, thus correctly finalizing the recipe summary. You must choose your answer from the Choice List. ",
        "Using a recipe tutorial interleaved with text and images, your responsibility is to examine it carefully and choose the best-suited text to fill the void, effectively completing the recipe summary. You must choose your answer from the Choice List. ",
        "With an image-text blended recipe tutorial at hand, your job is to attentively examine it and select the most fitting text to complete the missing part, thereby correctly concluding the recipe summary. You must choose your answer from the Choice List. ",
        "Presented with an image-text combined recipe tutorial, your duty is to analyze it thoroughly and select the most apt text to fill in the missing blank, thereby accurately concluding the recipe summary. You must choose your answer from the Choice List. "
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
        "context": "Recipe: smoked-paprika-chicken-tacos-with-spicy-goat-chees\nDetails: Step#1: 2 pounds boneless, skinless chicken thighs1. \nStep#2: 1 tablespoon unsalted butter1/2 jalapeño pepper, diced2garlic cloves, minced1 tablespoon flour1/2 cup milk6 ounces goat cheese, crumbled. {image#1}\nStep#3: corn tortillas for servingchopped tomatoessliced avocadocilantro, de-stemed. \nStep#4: 1. {image#2}\nRecipe Summary: 'UNKNOWN', 'Spicy Goat Cheese Queso', 'Taco Additions', 'Directions'\nChoice List:['Barbecue Chicken Cheese Spicy Mini Burrito', 'Bake and Enjoy', 'Prepare Sauce', 'Chicken Ingredients'] Your answer to replace 'UNKNOWN' is:",
        "images_path": [
            "0.jpg",
            "1.jpg"
        ]
    },
    "response": "Chicken Ingredients"
}
```
