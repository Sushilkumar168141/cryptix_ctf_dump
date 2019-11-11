import random
from math import sqrt

a=''
with open('hashed.txt','r') as file:
	a=file.read()
x = []
x = a.split(':')
wordlist=[]
msg = []
for j in x[:-1]:
	wordlist.append(j)
	#msg.append()
print(wordlist)
for word in wordlist:
	msg.append(int(word,0))
print(msg)


unhashed_number = int(pow(numerator/denominator,2))
subtract_key = data
