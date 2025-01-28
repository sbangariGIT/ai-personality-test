import os
import openai
from dotenv import load_dotenv
# Load env variables
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPEN_AI", ""))

def ask_openai_models(system_prompt, user_prompt, model="gpt-3.5-turbo-1106"):
    """
    :return: string as the response
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0
    )
    return response.choices[0].message.content