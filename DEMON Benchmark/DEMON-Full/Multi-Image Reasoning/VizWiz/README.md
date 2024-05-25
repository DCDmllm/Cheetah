# VizWiz

The original VizWiz dataset contains data submitted by users of a mobile phone application, who each took a picture and (optionally) recorded a spoken question about that picture. Based on the annoations, we furthur design several challenging tasks which require multi-image reasoning to answer.

Source: 
- [Why Does a Visual Question Have Different Answers?](https://arxiv.org/abs/1908.04342)
## Metadata

```json
{
    "dataset": "VizWiz",
    "split": "full",
    "num_sample": 5000,
    "task_instruction": [
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n I will give you two sets of pictures, questions, and answers to determine if they belong to the same 'Question-Answer Differences'. You must choose your answer from the Choice List. ",
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n I will provide you with two groups of pictures, questions, and answers to see if they have the same 'Question-Answer Differences'. You must choose your answer from the Choice List. ",
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n To check if they share the same 'Question-Answer Differences', I will give you two sets of pictures, questions, and answers. You must choose your answer from the Choice List. ",
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n Two sets of pictures, questions, and answers will be given to you to compare their 'Question-Answer Differences'. You must choose your answer from the Choice List. ",
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n I will present you with two collections of pictures, questions, and answers to examine if they match in their 'Question-Answer Differences'. You must choose your answer from the Choice List. ",
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n To evaluate if they have identical 'Question-Answer Differences', I will supply you with two sets of pictures, questions, and answers. You must choose your answer from the Choice List. ",
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n Two batches of pictures, questions, and answers will be delivered to you to assess their 'Question-Answer Differences'. You must choose your answer from the Choice List. ",
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n I will show you two groups of pictures, questions, and answers to determine if they agree on their 'Question-Answer Differences'. You must choose your answer from the Choice List. ",
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n To verify if they have the same 'Question-Answer Differences', I will offer you two sets of pictures, questions, and answers. You must choose your answer from the Choice List. ",
        "There are ten possible explanations for the ten different answers to a VQA:\n1:Low Quality Image(LQI), image is too small, out of focus, having poor quality, or nothing is visible.\n2:Answer Not Present(IVE), good image, but answer to the question is not present in the image (Insufficient Visual Evidence), so some answers reflect guesses.\n3:Invalid(INV), a proper or semantically correct question is absent.\n4:Difficult(DFF), questions that require domain expertise,special skills, or too much effort.\n5:Ambiguous(AMB), good image and valid question, but taken together they have more than one valid interpretation, leading to multiple answers.\n6:Subjective(SBJ), opinion-driven questions, such as assessing beauty, fashion sense, emotions.\n7:Synonyms(SYN), answers present the same idea, but using different words having similar meaning.\n8:Granular(GRN), answers present the same idea, but in different levels of detail or specialization.\n9:Spam(SPM), a person inadequately answers a simple, straight-forward visual question.\n10:Other(OTH), others\n Two sets of pictures, questions, and answers will be provided to you to measure their 'Question-Answer Differences'. You must choose your answer from the Choice List. "
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
        "context": "{image#1}{image#2}Question1:What is this bottle? Answer1:['nasal spray', 'unanswerable', 'nasal spray', 'visine', 'nasal spray', 'unanswerable', 'unsuitable', 'unanswerable', 'saline', 'unanswerable'] Question2:How do I turn on the oven? Answer2:['unanswerable', 'unanswerable', 'unsuitable', 'unsuitable', 'unanswerable', 'knob', 'button', 'unanswerable', 'unanswerable', 'light match']Choice List:['True', 'False'] Your answer is:",
        "images_path": [
            "0.jpg",
            "1.jpg"
        ]
    },
    "response": "True"
}
```