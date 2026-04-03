# question_generator.py

import openai

class QuestionGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_relevant_question(self, context):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "user", "content": f"Generate a relevant question based on the following context: {context}"}
            ]
        )
        return response.choices[0].message['content']

    def generate_unanswerable_question(self, context):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "user", "content": f"Generate an unanswerable question based on the following context: {context}"}
            ]
        )
        return response.choices[0].message['content']

    def generate_extended_question(self, context):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "user", "content": f"Generate an extended question based on the following context: {context}"}
            ]
        )
        return response.choices[0].message['content']

    def generate_cross_document_question(self, context1, context2):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "user", "content": f"Generate a cross-document question based on the following contexts: {context1} and {context2}."}
            ]
        )
        return response.choices[0].message['content']

    def generate_special_case_question(self, context):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "user", "content": f"Generate a special case question based on the following context: {context}"}
            ]
        )
        return response.choices[0].message['content']
