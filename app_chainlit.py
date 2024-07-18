#%%
# from langchain.prompts import ChatPromptTemplate
# from langchain.schema import StrOutputParser
# from langchain.schema.runnable import Runnable
# from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl
#%%
# from groq import Groq
# from langchain_groq import ChatGroq
# from llama3 import app

#%%
# model = ChatGroq(model='llama3-70b-8192')
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You're a very knowledgeable historian who provides accurate and eloquent answers to historical questions.",
#         ),
#         ("human", "{question}"),
#     ]
# )
# runnable = prompt | model | StrOutputParser()

# @cl.on_chat_start
# async def on_chat_start():
    
#     cl.user_session.set("runnable", runnable)
#%%

# @cl.on_message
# async def on_message(message: cl.Message):
#     runnable = cl.user_session.get("runnable")  # type: Runnable

#     msg = cl.Message(content="")

#     async for chunk in runnable.astream(
#         {"question": message.content},
#         config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
#     ):
        
#         await msg.stream_token(chunk)

#     await msg.send()

# %%
@cl.on_message
async def on_message(message: cl.Message):
    #runnable = cl.user_session.get("runnable")  # type: Runnable

    # res = app.invoke({"question": message.content})
    # response = res['generation']

    import requests

    json_response = requests.post("http://localhost:10000/invoke",
        json={
            "input": {
                "question": message.content,
                "generation": "string",
                "web_search": "string",
                "documents": [
                "string"
                ]
            },
            "config": {
                "configurable": {
                "thread_id": 12,
                "thread_ts": "string"
                }
            },
            "kwargs": {}
        }
    )

    response = json_response.json()['output']['generation']

    await cl.Message(content=response).send()

#%%
# import requests

# response = requests.post("http://localhost:8000/invoke",
#     json={
#         "input": {
#             "question": "when was the patients blood pressure highest?",
#             "generation": "string",
#             "web_search": "string",
#             "documents": [
#             "string"
#             ]
#         },
#         "config": {
#             "configurable": {
#             "thread_id": 12,
#             "thread_ts": "string"
#             }
#         },
#         "kwargs": {}
#     }
# )

# print(response.json()['output']['generation'])