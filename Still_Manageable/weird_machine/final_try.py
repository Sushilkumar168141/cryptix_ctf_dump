import random
import string

#rand = random.randint(1,100)
alphanum = string.ascii_letters + string.digits

cipher=''
output=''
with open('seq.txt','r') as file:
	cipher = file.read()

def random_string(rand_seed,wordlist):
    random.seed(rand_seed)
    rand_string = ''
    for i in range(len(wordlist)):
        rand_string += alphanum[random.randint(1,1000)%len(alphanum)]
    #print(rand_string)
    return rand_string

#print(cipher)

#wordlist=[]
#ans=''
q=8
wordlist = [cipher[i:i+q] for i in range(0,len(cipher),q)]
print(wordlist)
for z in range(10000):
	ans=''
	rand=z
	rand_str=random_string(z,wordlist)
	#print(rand_str)
	for j in range(len(wordlist)):
		x = int(wordlist[j],2)
		#print(x)
		m=x^ord(rand_str[j])
		ans+=chr(m)
	print(ans)
	output+=ans+'\n'
	#if ('fl' in ans):
	#	print(ans)
	#	input()
#with open('output.txt' , 'wb') as file:
#	file.write(output)