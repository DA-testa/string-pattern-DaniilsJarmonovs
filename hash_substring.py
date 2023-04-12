# Izstrādāja Daniils Jarmonovs, 18. grupa
from random import randint

def read_input():
    inp = input()
    if("I" in inp):
        P = input()
        T = input()
    elif("F" in inp):
        FName = input()
        with open(FName, mode="r") as file:
            P = file.readline()
            T = file.readline()
    return (P.rstrip(), T.rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def getHash(s):
    global b
    mult = 1
    hashcode = 0
    for i in range(len(s)-1, -1, -1):
        hashcode += ord(s[i])*mult
        mult = mult*b
    return hashcode

def editHash(p, hashcode, prev):
    global b, maxmult
    hashcode -= ord(prev)*maxmult
    hashcode = b*hashcode+ord(p[-1])
    return hashcode

def get_occurrences(pattern, text):
    global b, maxmult
    output = []
    b = randint(1, 20)
    Plen = len(pattern)
    Tlen = len(text)
    maxmult = b**(Plen-1)
    toFind = getHash(pattern)
    for i in range(Tlen-Plen+1):
        p = text[i:i+Plen]
        if(i==0):
            patternHash = getHash(p)
        else:
            prev = text[i-1]
            patternHash = editHash(p, patternHash, prev)
        if(patternHash==toFind):
            if(p==pattern):
                output += [i]
    return output

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))