from langflow.load import run_flow_from_json
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

question = input("Enter your question: ")

result = run_flow_from_json(flow="Chat_Mistral2.json",
                            input_value=question)

model = "open-mixtral-8x22b"

client = MistralClient(api_key="vNanzJFjXjZwcJOafKpRJMOlFG9fsvDU")

chat_response = client.chat(
    model=model,
    temperature= 0.1,
    messages=[ChatMessage(role="user", content=result[0].outputs[0].results)]
)

print(chat_response.choices[0].message.content)
