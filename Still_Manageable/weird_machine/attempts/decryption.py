import random
import string

#rand = random.randint(1,100)
alphanum = string.ascii_letters + string.digits

#cipher='0000010101011010000101100000111100110110001011000001010000110100010101100011110000001101000111100000101000000010001011010101110101011110001000100101100100101100001010100000101100100111000001110100001101000011000100000001011000101011000111110010111001001000'
#with open('encrypt.txt','r') as file:
with open('../seq.txt' , 'r') as file:
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
	#if ('o1' in rand_str):
		#print(rand_str,z)
		#input()	
	for j in range(len(wordlist)):
		x = int(wordlist[j],2)
		#print(x)
		m=x^ord(rand_str[j])
		ans+=chr(m)
	#print(ans)
	if ('w3' in ans):
		print(ans)
		#input()
