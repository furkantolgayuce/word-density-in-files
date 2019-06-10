from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class word_density:
	def __init__(self,file):
		self.file = file

	def get_df(self):
		f = open(self.file,'r',encoding='utf8',errors="ignore")
		string = f.read()
		# purge
		for i in "0123456789:,-<>/=#.?][!''♪\"":
			string = string.replace(i,"").lower()
		# get list
		word_list = string.split()
    	
    	# word counting and dictionary make
		data = dict(Counter(word_list))

		# get DataFrame
		df = pd.DataFrame.from_dict(data=data,orient='index')
		df.rename(columns={0:'repetition'},inplace=True)
		df.sort_values(by=["repetition"],ascending=False,inplace=True)

		frequently_used_words = ['the', 'you', 'a', 'to', 'i', 'and', 'of', 'in', 'it', 'your', 'have',
		'are', 'this', 'on', 'what', 'me', 'they', 'that', 'youre', 'do', 'is',
		'for', 'not', 'im', 'my', 'them', 'we', 'he', 'if',
		'be', 'with', 'will', 'from','who','was', 'at', 'there', 'up', 'dont', 'no', 'were', 'so', 'now',
		'those', 'mr', 'here', 'him',  'its','said',  'by', 'as', 'or','when',
		'thats', 'theres', 'these', 'their', 'been', 'did', 'his',  'us',  'can', 'then',"her","she","all","our","too"]

		# most used word drop
		for i in frequently_used_words:
			df = df.drop(i, axis=0, errors="ignore")

		self.df = df
		return self.df


	def get_chart(self,number=25):
		plt.figure(figsize=(18,9))

		# İlk 30 kelimeyi aldık.
		data = self.df[:number]

		plt.bar(data.index,data["repetition"])
		plt.xticks(data.index,data.index,rotation=45)

		plt.show()
