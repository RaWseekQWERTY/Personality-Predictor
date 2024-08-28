import google.generativeai as genai
from dotenv import load_dotenv
import os

from src.core.prompts import questions, get_prompt

def setup_gemini():
    load_dotenv()

    GOOGLE_API_KEY = os.getenv('GOOGLE_API')
    genai.configure(api_key=GOOGLE_API_KEY) 
    model = genai.GenerativeModel('gemini-pro')

    return model

def gemini_response(prompt: str):
    model = setup_gemini()
    response = model.generate_content(prompt)
    return response

def ask_questiosn():
    user_answer = []
    questions_options = questions()

    for index, question in enumerate(questions_options, start=1):
        print(f"{index}. {question['question']}")
        for index, option in enumerate(question['options'], start=1):
            print(f'\t{index}. {option}')
        
        answer = int(input())
        user_answer.append(question['options'][answer-1])

    return user_answer

def main():
    qa = ask_questiosn()
    res = gemini_response(qa)
    return res

if __name__ == "__main__":
    main()