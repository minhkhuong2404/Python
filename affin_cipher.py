import math
def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
def getMessage():
    print("Enter your message")
    return input()
def getKey():
    a , b = int(input())
    return a,b

def inverseModulo(a,m):
    if math.gcd(a,m) != 1:
        return None
    u1, u2, u3 = 1 , 0 ,a
    v1, v2 ,v3 = 0 , 1 ,m
    while v3!= 0:
        q = u3 // v3
        v1,v2,v3,u1,u2,u3 = (u1 - q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1 % m

def getTranslatedMessage(mode, message, key):
    if mode[0] == "d":
        inv_a = inverseModulo(a,26)
    
# print(inverseModulo(9,26)
