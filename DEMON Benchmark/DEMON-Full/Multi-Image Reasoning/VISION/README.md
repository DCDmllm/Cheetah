# VISION

The original VISION Datasets are a collection of 14 industrial inspection datasets, designed to explore the unique challenges of vision-based industrial inspection. These datasets are carefully curated from Roboflow and cover a wide range of manufacturing processes, materials, and industries. Based on the annoations, we furthur design several challenging tasks which require multi-image reasoning to answer.

Source: 
- [VISION Datasets: A Benchmark for Vision-based InduStrial InspectiON](https://arxiv.org/abs/2306.07890)
## Metadata

```json
{
    "dataset": "VISION",
    "split": "full",
    "num_sample": 2000,
    "task_instruction": [
        "Are these two workpieces the same type? You must choose your answer from the Choice List. ",
        "Are these two workpieces of the same kind? You must choose your answer from the Choice List. ",
        "Are these two workpieces the same category? You must choose your answer from the Choice List. ",
        "Are these two workpieces the same classification? You must choose your answer from the Choice List. ",
        "Are these two workpieces the same sort? You must choose your answer from the Choice List. ",
        "Are these two workpieces the same variety? You must choose your answer from the Choice List. ",
        "Are these two workpieces the same genre? You must choose your answer from the Choice List. ",
        "Are these two workpieces the same family? You must choose your answer from the Choice List. ",
        "Are these two workpieces the same species? You must choose your answer from the Choice List. ",
        "Are these two workpieces the same breed? You must choose your answer from the Choice List. ",
        "Are the damages to the following two identical workpieces of the same type? You must choose your answer from the Choice List. ",
        "Are the damages on both workpieces identical? You must choose your answer from the Choice List. ",
        "Are the damages on both workpieces the same? You must choose your answer from the Choice List. ",
        "Are the damages on both workpieces of the same type? You must choose your answer from the Choice List. ",
        "Do both workpieces have identical damages? You must choose your answer from the Choice List. ",
        "Do both workpieces have the same damages? You must choose your answer from the Choice List. ",
        "Do both workpieces have damages of the same type? You must choose your answer from the Choice List. ",
        "Are the damages on these two identical workpieces similar? You must choose your answer from the Choice List. ",
        "Are the damages on these two identical workpieces alike? You must choose your answer from the Choice List. ",
        "Are the damages on these two identical workpieces equal? You must choose your answer from the Choice List. "
    ],
    "question_type": "multi-choice"
}
```

## Example

```json
{
    "sample_id": 0,
    "task_instruction_id": 5,
    "task_instance": {
        "context": "{image#1}{image#2}Choice List:['True', 'False'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg"
        ]
    },
    "response": "True"
}
```
