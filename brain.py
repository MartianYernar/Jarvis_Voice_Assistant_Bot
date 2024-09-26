from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "you are openai bot who provides solution for tasks"},
    {"role": "user", "content": "Solve this problem: 2x=4"}
  ]
)


print(completion.choices[0].message)