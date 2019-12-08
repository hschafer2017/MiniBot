from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


chatbot = ChatBot("MiniBot",
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'I am sorry, but I do not understand.',
                        'maximum_similarity_threshold': 0.85
                    },
                    {
                        'import_path': "chatterbot.logic.MathematicalEvaluation"
                    },
                    {
                        'import_path': 'chatterbot.logic.TimeLogicAdapter',
                    }
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

        bot_response = chatbot.get_response(input(f'You: '))

        print(f'MiniBot: {bot_response}')

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
