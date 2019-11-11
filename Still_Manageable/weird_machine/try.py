import random
import string

#rand = random.randint(1,10000)
alphanum = string.ascii_letters + string.digits
#rand=4
def random_string(rand_seed,wordlist):
    random.seed(rand_seed)
    #print(rand_seed)
    rand_string = ''
    for i in range(len(wordlist)):
        #rand_string += alphanum[random.randint(1,1000)%len(alphanum)]
        for j in range(1001):
        	rand_string+=alphanum[j%len(alphanum)]
    #print(rand_string)

    	return rand_string


cipher = '000010010101110100011000010100110011110101100010011000000001111100110101011000110101010100110100010010110101101001010101001101100110110000111100011000010001111000001011000011010000100000000001010101100011100000100101'
#cipher = '00001001010111010001100001010011'
q=8
wordlist = [cipher[i:i+q] for i in range(0,len(cipher),q)]
#print(wordlist, len(wordlist))
def message_decoded(rand_string,wordlist):
	for z in range(1,10000):
		rand=z
		#print(random_string(z))
		random_str = (random_string(rand,wordlist))
		#print(random_str)
		ans=''
		for j in range(len(wordlist)):
			x =(int(wordlist[j],2))
			m = (x^ord(random_str[j]))
			ans+=chr(m)
		print(ans)
		if ('flag' in ans):
			print(rand,random_str)
			input()
	#input()
