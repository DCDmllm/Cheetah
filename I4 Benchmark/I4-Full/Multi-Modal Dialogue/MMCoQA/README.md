# MMCoQA

The original MMCoQA dataset require models to answer users’ questions with multimodal knowledge sources via multi-turn conversations. We reorgnize the orignal annotations to our style.

Source: 
- [MMCoQA: Conversational Question Answering over Text, Tables, and Images](https://aclanthology.org/2022.acl-long.290/)
## Metadata

```json
{
    "dataset": "MMCoQA",
    "split": "full",
    "num_sample": 4925,
    "task_instruction": [
        "Provided with a variety of pertinent information, including images, text, tables, and previous Q&A history, your role is to answer the upcoming question accurately.",
        "With an assortment of related data such as images, text, tables, and past Q&A history, your task is to correctly respond to the following question.",
        "Using a collection of relevant information, including graphics, text, tables, and a history of Q&A, your job is to accurately answer the forthcoming question.",
        "Given a set of relevant data, comprising images, text, tables, as well as prior Q&A interactions, please provide an accurate response to the subsequent query.",
        "Drawing upon a pool of relevant data, including imagery, textual data, tables, and previous Q&A exchanges, your responsibility is to correctly answer the impending question.",
        "With the provided comprehensive data, which consists of images, text, tables, and prior Q&A records, your task is to provide an accurate answer to the next question.",
        "Using a corpus of relevant information including visuals, text, tabular data, and a history of Q&A, your assignment is to answer the subsequent query accurately.",
        "Having a collection of pertinent data that comprises of images, text, tables, and past Q&A dialogues, your duty is to provide an accurate response to the following question.",
        "Given the available relevant resources including images, texts, tables, and previous Q&A sessions, your task is to accurately answer the forthcoming question.",
        "Provided with a diverse set of relevant data, encompassing images, texts, tables, and a record of past Q&A interactions, you're tasked with providing an accurate response to the subsequent query."
    ],
    "question_type": "open-ended"
}
```

## Example

```json
{
    "sample_id": 2,
    "task_instruction_id": 1,
    "task_instance": {
        "context": "Global Table: {table#1} History Context 1: Table: {table#2} Question: what is the competition of Gøtu Ítróttarfelag with match against Rangers? Answer: UEFA Champions League.  History Context 2: Text: Introduced in 1992, the competition replaced the European Champion Clubs' Cup, or simply European Cup, which had run since 1955, adding a group stage to the competition and allowing multiple entrants from certain countries. The pre-1992 competition was initially a straight knockout tournament open only to the champion club of each country. During the 1990s, the format was expanded, incorporating a round-robin group stage to include clubs that finished runner-up of some nations' top-level league. While most of Europe's national leagues can still only enter their national league champion, Europe's strongest national leagues now provide up to five teams for the competition. Clubs that finish next-in-line in each nation's top level league, having not qualified for the UEFA Champions League competition, are eligible for the next-level UEFA Europa League competition. Question: When did the European cup become this competition? Answer: 1992.  Current Context: {image#3} {image#4} {image#5} Question: What Rangers 2010-11 player has a shaved head? Answer:",
        "images_path": [
            "2.png",
            "2.png",
            "3.jpg",
            "4.jpg",
            "5.jpg"
        ]
    },
    "response": "Madjid Bougherra. Steven Naismith. Conor Sammon. "
}
```
