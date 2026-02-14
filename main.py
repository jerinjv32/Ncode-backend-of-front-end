import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
load_dotenv()


class PromptModel(BaseModel):
    prompt: str


class ResponseModel(BaseModel):
    title: str


HF_TOKEN = os.getenv('HF_TOKEN')

client = InferenceClient(
    api_key=HF_TOKEN,
)


@app.post('/chat')
def chat_bot(body: PromptModel):
    prompt = body.prompt
    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct:nebius",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    response = completion.choices[0].message.content
    return ResponseModel(title=response)

