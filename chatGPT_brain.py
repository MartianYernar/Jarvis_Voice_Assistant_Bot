import openai
from openai import OpenAI

client = OpenAI()

def AI_get_response(text):
  try:
    completion = client.chat.completions.create(
        model="gpt-4",
        messages = [
            {'role': 'system', 'content': 'Your name is Jarvis, you are assistant AI for sir Yernar, answer questions no more than in 1-2 sentences'},
            {'role': 'user', 'content': text}
        ]
    )

    
    reply = completion.choices[0].message.content.strip()
    return reply
  except Exception as e:
    return e