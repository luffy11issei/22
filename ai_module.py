import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_solution(disease):
    prompt = f"What is the best treatment for {disease}?"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"⚠️ Error retrieving AI treatment: {str(e)}"
