import re
import csv

def processRow(row):
	tweet = row
	#hapus URL
	tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
	#Hapus mention
	tweet = re.sub('@[^\s]+','',tweet)
	#Hapus Hashtag
	tweet = re.sub('#[^\s]+','',tweet)
	

	tweet = re.sub("b' ","",tweet)
	tweet = re.sub("b'","",tweet)
	tweet = re.sub('b"','',tweet)
	#Remove additional white spaces
	tweet = re.sub('[/n]','',tweet)
	# #Remove not alphanumeric symbols white spaces
	# tweet = re.sub(r'[^\w]+', ' ', tweet)
	 
	#Remove :( or :)
	tweet = tweet.replace(':)','')
	tweet = tweet.replace(':(','')
	# # #trim
	tweet = tweet.strip('\'"')

	row = tweet

	return row


filename = 'Covid19-Sentiment.csv'
f = open(filename,'r', encoding='utf8')
reader = csv.reader(f)
w = open('Covid19-Sentiment_Clean.csv','a', encoding='utf8', newline='')
writer = csv.writer(w)
head = [['Tweet']]
writer.writerows(head)
for i in reader:
	clean = processRow(i[0])
	print(clean)
	clean = [[clean]]
	writer.writerows(clean)