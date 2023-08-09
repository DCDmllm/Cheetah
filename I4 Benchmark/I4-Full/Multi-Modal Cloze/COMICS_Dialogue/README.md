# COMICS_Dialogue

The original COMICS dataset contains ∼1.2 million panels drawn from almost 4,000 publicly-available comic books published during the “Golden Age” of American comics (1938–1954). It is challenging in both style and content compared to natural images. We follow the original code to generate several challenging tasks.

Source: 
- [The Amazing Mysteries of the Gutter: Drawing Inferences Between Panels in Comic Book Narratives](https://arxiv.org/abs/1611.05118)
## Metadata

```json
{
    "dataset": "COMICS_Dialogue",
    "split": "full",
    "num_sample": 6000,
    "task_instruction": [
        "I will give you a series of comic panels. The dialogue box of the last panel is masked. Can you choose the most relevant one from the candidates? You must choose your answer from the Choice List. ",
        "Given previous full panels and one masked panel, your job is to select the most appropriate dialogue among four candidates. You must choose your answer from the Choice List. ",
        "Upon viewing a sequence of comic panels with the final one having a hidden dialogue, could you determine the most fitting dialogue option from the available choices? You must choose your answer from the Choice List. ",
        "Presented with a series of comic panels with the dialogue of the last one obscured, can you identify the most suitable dialogue from the four provided alternatives? You must choose your answer from the Choice List. ",
        "You will be given a string of comic panels with the dialogue of the last one masked. Can you pick the most accurate dialogue from the given options? You must choose your answer from the Choice List. ",
        "Given several comic panels and a last one with hidden dialogue, your task is to choose the dialogue that fits best from four candidates. You must choose your answer from the Choice List. ",
        "When presented with a sequence of comic panels and the last one's dialogue is hidden, can you select the most appropriate dialogue from the proposed choices? You must choose your answer from the Choice List. ",
        "Given a series of comic panels with the dialogue of the final panel obscured, can you choose the most suitable dialogue from the provided alternatives? You must choose your answer from the Choice List. ",
        "Here are a number of comic panels with the dialogue in the last one masked. Could you select the most fitting dialogue from the available options? You must choose your answer from the Choice List. ",
        "Upon analyzing a sequence of comic panels with the last one's dialogue masked, can you identify the dialogue that fits best from the available candidates? You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 6,
    "task_instance": {
        "context": "{image#1}{image#2}{image#3}{image#4}{image#5}Choice List:['ut suddenly - ', 'for pete ' s sake ! what ' s happened to him has he got hay fever ? ', 'ow ! my foot ! ', 'keep it up boy , we ' re making good time ! ']Your answer is: ",
        "images_path": [
            "0.jpg",
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg"
        ]
    },
    "response": "keep it up boy , we ' re making good time ! "
}
```
