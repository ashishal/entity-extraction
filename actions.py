from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer, Metadata, Interpreter
from rasa.nlu import config
import pprint
import spacy
import en_core_web_md
import pickle
spacy.load("en_core_web_md")

def train_nlu(data, configs, model_dir):
	training_data=load_data(data)																#load NLU training sample
	trainer = Trainer(config.load(configs))														#train the pipeline first
	interpreter = trainer.train(training_data)													#train the model
	model_directory = trainer.persist("models/nlu",fixed_model_name="chatter")					#store in directory

def run_nlu():
	interpreter = Interpreter.load('models/nlu/chatter/')
	while(True):
		print("Enter your query?")
		a=input()
		if("bye" not in a):
			dictofresult=interpreter.parse(a) #the result is a nested dictionary
			# pprint.pprint(dictofresult)
			x=''
			y=''
			x=dictofresult['intent']['name']
			if(dictofresult['entities']):
				y=dictofresult['entities'][0]['value']
			result=x+' '+y
			print(result)
		else:
			break

if __name__ == '__main__':
	train_nlu('./data/nlu.md', './config.yml', './models/nlu')
	run_nlu()
