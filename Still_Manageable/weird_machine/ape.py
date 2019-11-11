import random
import string
from itertools import *
#from deep_memory import message
message = 'flag{'
#print("Encrpyt everything!!.... Oh no, system failure. Encrypting last message received")
rand = random.randint(1,10000)
alphanum = string.ascii_letters + string.digits
#rand=3
def random_string(rand_seed, message):
    random.seed(rand)
    print(rand_seed)
    rand_string = ''
    for i in range(len(message)):
        rand_string += alphanum[random.randint(1,1000)%len(alphanum)]
    #print(rand_string)
    return rand_string

def encrpyt(random_str, message):
    encrpyted = ''
    msg=''
    cipher=''
    for i in range(len(message)):
        k = ord(message[i])^ord(random_str[i])
        encrpyted += str(k)
        cipher = chr(k ^ ord(random_str[i]))
        msg+=cipher
        print(k)
        #cipher += (bin(k)[2:]).zfill(8)
    #print(encrpyted)
    print(msg)
    return encrpyted

cipher = (encrpyt(random_string(rand, message), message))
print(cipher)

'''
#avail_words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
#w = list(product(avail_words,avail_words,repeat = 1))
cipher = '000010010101110100011000010100110011110101100010011000000001111100110101011000110101010100110100010010110101101001010101001101100110110000111100011000010001111000001011000011010000100000000001010101100011100000100101'
print(cipher)
q=8
wordlist = [cipher[i:i+q] for i in range(0,len(cipher),q)]
print(wordlist)
ans=''
message = 'flag{abcdefghijklmnopqrstuvwxyz}'
for z in range(1,10000):
    rand=z
    random_str = random_string(rand,message)
    for j in range(len(wordlist)):
        x =(int(wordlist[j],2))
        #for i in range(len(random_str)):
        m = x ^ ord(random_str[j])
        #print(chr(m))
        ans+=chr(m)
    print(ans)
    ans=''
    input()
#print(random_str)

'''