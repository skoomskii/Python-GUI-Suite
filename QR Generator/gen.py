import string
import secrets
import os

def generator(x,y,z,size):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(size))
        if (sum(c in string.punctuation for c in password)>=x
                and sum(c.isupper() for c in password)>=y
                and sum(c.isdigit() for c in password)>=z):
            return password

def code():
    x = input('Nos. Special Characters: ')
    y = input('Nos. Upper Cases: ')
    z = input('Nos. Digits: ')
    size = input('Size: ')
    if (int(x)+int(y)+int(z)>int(size)):
        os.system('cls')
        code()
    else: return generator(int(x),int(y),int(z),int(size))

def codeGen():
    print('******************** Code Generator ********************')
    data = code()
    if (data == 'None'):
        codeGen()
    else:
        print(f'\nCode: {data}\n************************************************************')
        clr=[]
        clr= input('Clear: ')
        if (len(clr)>0):
            os.system('cls')
            codeGen()
        else: return data

if __name__ == "__main__":
    codeGen()