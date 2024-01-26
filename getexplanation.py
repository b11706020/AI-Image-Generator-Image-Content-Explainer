from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
# Placeholder for your language processing API call
def get_input_explanation(user_input):
    # Replace this with your actual API call or processing logic to get the explanation of the input
    # For demonstration, return a placeholder string
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a helpful, respectful, and honest assistant. 
                Always answer as helpfully as possible using the  data provided. 
                You are a helpful assistant. Yo
                You should provide The appropriate explanation of the user input .
                you are tasked to provide a simple explanation or description for the user input"""},


            {"role": "assistant", "content": f"user input: {user_input}"}
        ]
    )
    return response.choices[0].message.content