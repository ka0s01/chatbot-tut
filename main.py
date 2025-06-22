# from langchain_openai import ChatOpenAI  
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
# from dotenv import load_dotenv
# import os

# load_dotenv()
# llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

# memory = ConversationBufferMemory()
# conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         break
#     response = conversation.predict(input=user_input)
#     print("Bot:", response)
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use gemini-1.5-flash instead of gemini-pro
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

print("Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    try:
        response = chat.send_message(user_input)
        print("Bot:", response.text)
    except Exception as e:
        print("Error:", e)
