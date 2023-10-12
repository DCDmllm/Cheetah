# ALFRED

The original ALFRED (Action Learning From Realistic Environments and Directives) is a benchmark for learning a mapping from natural language instructions and egocentric vision to sequences of actions for household tasks. We transfer the original annotations to the form of multi-modal dialogue.

Source: 
- [A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://arxiv.org/abs/1912.01734)
## Metadata

```json
{
    "dataset": "ALFRED",
    "split": "core",
    "num_sample": 2294,
    "task_instruction": [
        "Give you a main goal, your job is to figure out what to do now by looking at current envirments. Your past views as well as decisions are also provided.",
        "Given a primary objective and your current surroundings, use your previous decisions and perspectives to determine your next move.",
        "Using the final goal as your guide, reflect on your past successful strategies as a smart agent. Observe the information in the image to inform your present decision.",
        "As an intelligent entity, consider your past correct actions and aim for the ultimate goal. Now, examine the data within the picture to decide your immediate action.",
        "You are an intelligent agent who has made smart decisions in the past. To achieve the end goal, scrutinize the image's details and contemplate your immediate action.",
        "Given your past actions and the main goal, analyze your current environment. Decide your next step based on this analysis.",
        "Your ultimate task is to reach the main goal. Reflect on your past decisions, consider your current surroundings, and determine your immediate action.",
        "You are a smart agent aiming to reach a final goal. Consider your successful decisions from past rounds and the current situation presented in the image. What would be your next move?",
        "As an intelligent entity, you are tasked with reaching the main goal. Utilizing your past decisions and the information in the picture, contemplate your next action.",
        "Your objective is the main goal. Evaluate your current environment and your past decisions, and decide your immediate course of action."
    ],
    "question_type": ""
}
```

## Example

```json
{
    "sample_id": 3,
    "task_instruction_id": 2,
    "task_instance": {
        "context": "Your Main Goal:  Place a soap container on a counter.  Step Details: {image#1}Step#1: Turn left and walk to the right sink. {image#2}Step#2: Open the bottom left cabinet and take out the closest soap container. {image#3}Step#3: Take a step left. {image#4} Current Step: ",
        "images_path": [
            "6.jpg",
            "7.jpg",
            "8.jpg",
            "9.jpg"
        ]
    },
    "response": "Place the soap container on the counter in between the two sinks."
}
```
