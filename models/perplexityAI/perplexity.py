from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("PERPLEXITY_API", ""), base_url="https://api.perplexity.ai")

def ask_perplexity_models(system_prompt, user_prompt, model="llama-3-sonar-large-32k-online"):
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
    )
    return response.choices[0].message.content