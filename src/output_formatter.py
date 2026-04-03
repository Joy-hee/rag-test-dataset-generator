import json


def format_to_deepeval(qas):
    formatted_data = []
    for qa in qas:
        formatted_data.append({
            'question': qa['question'],
            'answer': qa['answer'],
            'source_document': qa.get('source_document', 'Unknown'),
            'question_type': qa.get('question_type', 'general')
        })
    return json.dumps(formatted_data, indent=4)


def format_to_mlflow(qas):
    mlflow_data = []
    for qa in qas:
        mlflow_data.append({
            'question': qa['question'],
            'answer': qa['answer'],
            'source_document': qa.get('source_document', 'Unknown'),
            'question_type': qa.get('question_type', 'general')
        })
    return mlflow_data  # Typically, MLflow can handle dict or lists directly.


# Example usage
# qas = [
#     {'question': 'What is AI?', 'answer': 'Artificial Intelligence', 'source_document': 'doc1', 'question_type': 'definition'},
#     {'question': 'Explain deep learning.', 'answer': 'A subset of AI...', 'source_document': 'doc2'}
# ]
# print(format_to_deepeval(qas))
# print(format_to_mlflow(qas))
