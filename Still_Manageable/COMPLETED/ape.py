from Crypto.Util.number import *

n = 3073416132828889709313918053975078361304902307
c = 1217323181436745647195685030986548015017805440
p = 13558774610046711780701
q = 226673591177742970257407
e = 65537
totient = (p-1)*(q-1)
d = inverse(e,totient)
#print(d)
m = pow(c,d,n)
#print(m)
message = (hex(m)[2:-1]).decode('hex')
print(message)