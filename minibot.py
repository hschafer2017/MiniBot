from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


app = Flask(__name__)

chatbot = ChatBot("MiniBot",
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'I am sorry, but I do not understand.',
                        'maximum_similarity_threshold': 0.7
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

@app.route("/")
def home():    
    return render_template("index.html") 


@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(chatbot.get_response(userText)) 


if __name__ == "__main__":    
    app.run()
    # For Heroku deployment
    # app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
