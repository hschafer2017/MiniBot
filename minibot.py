from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


chatbot = ChatBot("MiniBot",
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.TimeLogicAdapter'
                  ],
                  database_uri='sqlite:///database.sqlite3'
)
trainer = ListTrainer(chatbot)

trainer.train([
    "Hi there!",
    "Hello",
])

trainer.train([
    "Hi",
    "Hello",
])

trainer.train([
    "What's up?",
    "Whatever it is, it's nothing.",
])

response = chatbot.get_response('Hi')
print(response)