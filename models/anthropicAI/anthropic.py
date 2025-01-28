import anthropic
import os
from dotenv import load_dotenv
# Load env variables
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API", ""))


def ask_anthropic_models(system_prompt, user_prompt, model="claude-3-5-sonnet-20240620"):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        temperature=0,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt
                    }
                ]
            }
        ]
    )
    return str(message.content[0].text)
