import random
import sys

# the code uses the notation from the textbook

# calculatre modular inverse
def modInverse(a, m):
    m0=m
    y=0
    x=1
 
    if (m==1):
        return 0
 
    while (a>1):
        q=a//m
        t=m
        m=a%m
        a=t
        t=y
        y=x-q*y
        x=t
        
    if (x<0):
        x=x+m0
 
    return x

# modular exponentiation
def power(a,b,c):
    x=1
    y=a
 
    while b>0:
        if b%2!=0:
            x=(x*y)%c
        y=(y*y)%c
        b=int(b/2)

    return x%c

# calculate the public and private keys
def get_key(alpha,q):
    private=random.randint(1,q-1) # generate the private key XA, randomly choosen between 1 and q-1
    public=power(alpha,private,q) # calculate the public key as  YA = (alpha^XA)mod q
    return public,private

# encrypt the message using the reciever's public key
def encrypt(message,public,alpha,q):
    k=random.randint(1,q-1)  # choose k at random
    K=power(public,k,q)    # calculate K = (YA^(k))mod q
    
    c1=power(alpha,k,q)    # calculate c1 as c1 = (alpha^k)mod q
    c2=((K%q)*(message%q))%q # calculate c2 as c2 = (K*M)mod q where M is the message
    
    return c1,c2

# decrypt the message using the reciever's private key
def decrypt(c1,c2,private,q):
    K=power(c1,private,q)   # K = (c1^XA)mod q
    
    inverse=modInverse(K,q) # calculate the multiplicative inverse of K modulo q
    message=((c2%q)*(inverse%q))%q # message M = (c2*K^(-1)) mod q
    
    return message

q=1291 # order of the algorithm (q is prime)
alpha=1147 # alpha is a primitive root of q
message=129 #message M

if(message>=q): # messagge cannot be greater than or equal to than q
    print('Message cannot be greater than q')
    sys.exit(0)
    
print('q = {}, α = {} and message M = {}'.format(q,alpha,message))

public,private=get_key(alpha,q) # generate the keys
print('Private Key = {}, Public Key = {}'.format(private,public))

c1,c2=encrypt(message,public,alpha,q) # encrypt to get c1 and c2
print('After encrypting the message we obtain C1 = {} and C2 = {}'.format(c1,c2))

M_dash=decrypt(c1,c2,private,q) # decrypt and print the message M
print('The decrypted message is M = {}'.format(M_dash))