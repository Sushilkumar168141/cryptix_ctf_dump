import random
import string
#from deep_memory import message
message = 'flag{it_is_so_R4nd0M_abcdef}'
#print("Encrpyt everything!!.... Oh no, system failure. Encrypting last message received")

rand = random.randint(1,10000)
alphanum = string.ascii_letters + string.digits

output=''
def random_string(rand_seed, message):
    random.seed(rand_seed)
    rand_string = ''
    for i in range(len(message)):
        rand_string += alphanum[random.randint(1,1000)%len(alphanum)]
    print(rand_string)
    return rand_string

def encrpyt(random_str, message):
    encrpyted = ''
    for i in range(len(message)):
        k = ord(message[i])^ord(random_str[i])
        encrpyted += (bin(k)[2:]).zfill(8)
    #output = encrpyted
    return encrpyted
output = (encrpyt(random_string(rand, message), message))
print(output)
with open('encrypt.txt','w') as file:
    file.write(output)
'''
for z in range(10):
    a = random_string(z,message)
    if (encrpyt(a,message) == output):
        print(z,a)
        #input()

'''