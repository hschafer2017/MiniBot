from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


chatbot = ChatBot("MiniBot",
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                    "chatterbot.logic.MathematicalEvaluation",
                    "chatterbot.logic.TimeLogicAdapter",
                    "chatterbot.logic.BestMatch"
                    ],
                  input_adapter="chatterbot.input.TerminalAdapter",
                  output_adapter="chatterbot.output.TerminalAdapter",
                  database_uri='sqlite:///database.sqlite3'
)


general_trainer = ChatterBotCorpusTrainer(chatbot)

general_trainer.train(
    "chatterbot.corpus.english", 
    "training_data/training_data.yml"
)

while True:
    try:

        bot_response = chatbot.get_response(input())

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
