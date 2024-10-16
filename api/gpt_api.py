# import requests

# # Load API key for Together.AI
# api_key = '1d5e0fb7ec8105b51725f3e3751513868a9f4ea5a105c8fd35aebf25b1f61154'


# # Function to call Together.AI API
# def ask_question(prompt):
#     url = "https://api.together.xyz/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",  # Example model, adjust as needed
#         "messages": [{"role": "user", "content": prompt}],
#         "max_tokens": 150,
#         "temperature": 0.8
#     }

#     # Send the request to Together.AI
#     response = requests.post(url, headers=headers, json=payload)
    
#     # Check for a successful response
#     if response.status_code == 200:
#         return response.json()['choices'][0]['message']['content']
#     else:
#         print(f"Error: {response.status_code}, {response.text}")
#         return None

# # Example prompt for asking about interests
# def get_student_interest():
#     prompt = """
#     Please answer the following:
#     1. What kind of software projects do you enjoy (web, apps, etc.)?
#     2. Are you more interested in theoretical concepts or practical coding?
#     """
#     return ask_question(prompt)

# # Test the function
# print(get_student_interest())



# # university-advisor/api/gpt_api.py
# import openai

# # Set your OpenAI API key here
# openai.api_key = "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"  # Replace with your actual API key

# def ask_question(prompt):
#     """
#     Function to ask ChatGPT a question and get a response.
#     """
#     response = openai.Completion.create(
#         engine="gpt-3.5-turbo",  # You can also use '' if you prefer
#         prompt=prompt,
#         max_tokens=150,
#         temperature=0.7
#     )
#     return response['choices'][0]['text']

import openai
import os
from dotenv import load_dotenv

# Load API key
def configure():
    load_dotenv()
    openai.api_key=os.getenv('api_key')

def ask_question(prompt):
    configure()
    response = openai.Completion.create(
        engine="gpt-4",    # Or 'gpt-3.5-turbo'
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response['choices'][0]['text']

# Example prompt for asking about interests
def get_student_interest():
    prompt = """
    Please answer the following:
    1. What kind of software projects do you enjoy (web, apps, etc.)?
    2. Are you more interested in theoretical concepts or practical coding?
    """
    return ask_question(prompt)


