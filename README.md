# Entity-Extraction
Input a question and return keywords which can be used to search files using Rasa


## Installation
1. Create an Environment for this project with Python=3.6
2. Install Rasa 
  ```bash
pip install rasa
pip install rasa[spacy]
  ```
Requirements file should install all necessary dependencies.
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
```
You need to give admin permission to link spacy to the language model. So run anaconda as administrator.
```bash
python -m spacy link en_core_web_md en
```
Go to step 6. As steps 3,4,5 are already installed through 'requirements.txt' file

3. Install Rasa Core 
  ```bash
pip install rasa_core
  ```
4. Install Rasa NLU for intent classification & entity extraction.  
  ```bash
pip install rasa_nlu
  ```
5. Python SDK for the development of custom actions for Rasa Core.
 ```bash
pip install rasa_core_sdk
 ```
6. unzip the files to the required directory
7. Run actions.py
 ## Output
 ```bash
        Enter your query?
        what is the production quota of asset Lower Zakum ?
        production Lower Zakum
        Enter your query?
        bye
 ```
8. Comment train_nlu() if you dont want to train the model after initial modeling
9. To add more intents and locations for your questions. Go to ./Data/nlu.md
  ```md
      '##intent'- keyword you want to extract
      Under intent, give your questions for each intent using a '-'
      '##lookup'- In this, used for location as well as date 
      '##synonym'- Used for most frequent typos of each word
  ```
