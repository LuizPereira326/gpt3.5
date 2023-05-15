import openai

openai.api_key = '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'

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Traduza o seguinte texto do inglês para o português: 'Hello, world!'",
  max_tokens=60
)

print(response.choices[0].text.strip())
