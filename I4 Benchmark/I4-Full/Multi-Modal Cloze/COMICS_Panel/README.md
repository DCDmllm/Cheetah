# COMICS_Panel

The original COMICS dataset contains ∼1.2 million panels drawn from almost 4,000 publicly-available comic books published during the “Golden Age” of American comics (1938–1954). It is challenging in both style and content compared to natural images. We follow the original code to generate several challenging tasks.

Source: 
- [The Amazing Mysteries of the Gutter: Drawing Inferences Between Panels in Comic Book Narratives](https://arxiv.org/abs/1611.05118)
## Metadata

```json
{
    "dataset": "COMICS_Panel",
    "split": "full",
    "num_sample": 6000,
    "task_instruction": [
        "I will give you a series of comic panels. You are supposed to select the next panel from candidates. You must choose your answer from the Choice List. ",
        "Upon examining a series of comic panels, your task is to select the subsequent panel from the provided options. You must choose your answer from the Choice List. ",
        "Presented with a sequence of comic panels, can you determine the most fitting next panel from the given choices? You must choose your answer from the Choice List. ",
        "Given a string of comic panels, your objective is to select the most appropriate following panel from the provided alternatives. You must choose your answer from the Choice List. ",
        "Having a number of comic panels in a sequence, can you discern which of the four options would best continue the storyline? You must choose your answer from the Choice List. ",
        "With a sequence of comic panels provided, could you identify the most relevant next panel from the available choices? You must choose your answer from the Choice List. ",
        "Upon viewing a series of comic panels, can you select the next panel that best fits the sequence from the candidates? You must choose your answer from the Choice List. ",
        "Presented with a number of sequential comic panels, your task is to determine the most suitable next panel from the four options. You must choose your answer from the Choice List. ",
        "When given a sequence of comic panels, can you choose the panel that best continues the storyline from the provided options? You must choose your answer from the Choice List. ",
        "With a string of comic panels in front of you, could you pick the most appropriate next panel from the available alternatives? You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 1,
    "task_instance": {
        "context": "{image#1}{image#2}{image#3}Choice List:['Image A: {image#4} ', ' Image B: {image#5} ', ' Image C: {image#6} ', ' Image D: {image#7} ']Your answer is: ",
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
