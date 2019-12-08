## MiniBot Prototype

[Live link](theminibot.herokuapp.com)

#### Dependencies
1. [Chatterbot](https://pypi.org/project/ChatterBot/)
```
pip3 install chatterbot
```

2. [Chatterbot Corpus](https://pypi.org/project/chatterbot-corpus/)

```
pip3 install chatterbot-corpus
```

3. [Natural Language ToolKit (NLTK)](http://www.nltk.org/index.html)
To install stopwords in iPython shell (Windows & Windows Subsystem for Linux): 

```
import nltk
nltk.download('stopwords')
```

To install NLTK stopwords on OS X:
- Go to list of [NLTK libraries](http://www.nltk.org/nltk_data/)
- Download source of Stopwords Corpus into a zip file
- Move unzipped `stopwords` folder to `/User/USERNAME/nltk_data/corpus/`

4. Flask
```
pip3 install Flask
```
5. A virtual environment of your choice (recommended)

### Training using Chatterbot Corpus data 
You can train the bot using Chatterbot Corpus data in multiple languages by downloading the corpus training data from the NLTK resource. Using the `ChatterBotCorpusTrainer` method, the chatbot will automatically be trained using this data each time to server is started. 

### Training using your own custom data set
The chatbot can also be trained using your own custom dataset. It can be trained using a JSON or `.yml` file containing sample conversations and responses. 

#### Example in .yml format
```
- - Are you a bot?
  - Maybe, maybe not.
```

Two dashes indicate the user input, and one dash indicates possible bot responses. For a larger example of training using a `.yml` file, please see the `training_data` folder in this repository. The chatbot can be trained using a combination of corpus data and data from a `.yml` file. 