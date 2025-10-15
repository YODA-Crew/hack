# Ensure your OpenAI client is available with:
# pip install openai

# %%
import os
import weave
from openai import OpenAI

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# %%

weave.init('gregoryturri-startup/intro-example') # 🐝

@weave.op() # 🐝 Decorator to track requests
def create_completion(message: str) -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
    )
    return response.choices[0].message.content

message = "Tell me a joke."
create_completion(message)
# %%
