import itertools
import numpy
from random import shuffle

alphabet = "abcdefghijklmnopqrstuvwxyz "
n=3
m=3

def generate_polynomes(n:int,m:int): #n^(m)
    nume = [num for num in range(n)]
    galois = list(itertools.product(nume,repeat=m))
    for i in range(len(galois)):
        galois[i] = list(galois[i])
    return galois

def generate_non_divisable_pol(n:int,m:int): #n^(m)
    nume = [num for num in range(n)]
    for elem in itertools.product(nume,repeat=m+1):
        if elem[0] == 0:
            continue
        lol = True
        elem = list(elem)
        for x in range(n):
            i = 0
            j = len(elem) - 1
            k = 0
            while j > 0:
                i += (elem[k]*x)**j
                j -= 1
                k +=1
            i += elem[k]
            if i % n == 0:
                lol = False
        if lol:
            return elem

my_polynom = generate_polynomes(n,m)
no_div = generate_non_divisable_pol(n,m)

def generate_dict(galois):
    dict = {}
    i=0
    for char in alphabet:
        dict[char] = galois[i]
        i += 1
    return dict

dict = generate_dict(my_polynom)

def lower_coef(result):
    for i in range(len(result)):
        result[i] %= n
    while result[0] == 0 and len(result) > m:
        result = numpy.delete(result, 0)
    while len(result) > m:
        result = list(map(int, numpy.ndarray.tolist(numpy.polydiv(result, no_div)[1])))
    for i in range(len(result)):
        result[i] = result[i] % n
    while len(result) < m:
        result.insert(0, 0)
    return result


def encrypt(message:str,key:tuple,dic:dict): #key(a,b)
    cipher_text = ""
    a,b = key[0],key[1]
    if a in dic.values() and key != [0,0,0]:
        for carac in message:
            result = numpy.convolve(a, dic[carac])
            result = numpy.polyadd(result, b)
            result = lower_coef(result)
            print("("+str(a[0])+"x^2"+"+"+str(a[1])+"x"+"+"+str(a[2])+")("+str(dic[carac][0])+"x^2"+"+"+str(dic[carac][1])+"x"+"+"+str(dic[carac][2])+")+"+str(b[0])+"x^2"+"+"+str(b[1])+"x"+"+"+str(b[1])+"="+str(result[0])+"x^2"+"+"+str(result[1])+"x"+"+"+str(result[2]))
            for char in dic:
                if numpy.array_equal(dic[char],result):
                    cipher_text += char
    return cipher_text

def decrypt(cipher_text:str,key:tuple,dict:dict):
    text = ""
    precedent_key = key[0]
    new_key = numpy.convolve(key[0],precedent_key)
    new_key = lower_coef(new_key)
    while((numpy.sum(new_key) != 1 or new_key[-1] != 1)):
        precedent_key = new_key
        new_key = numpy.convolve(key[0],precedent_key)
        new_key = lower_coef(new_key)
    for elem in cipher_text:
        result = numpy.polysub(dict[elem], key[1])
        result = numpy.convolve(result,precedent_key)
        result = lower_coef(result)
        print("(" + str(dict[elem][0]) + "x^2" + "+" + str(dict[elem][1]) + "x" + "+" + str(dict[elem][2]) +"-("+str(
            key[1][0]) + "x²" + "+" + str(key[1][1]) + "x" + "+" + str(key[1][2])+ "))(" + str(
            precedent_key[0]) + "x^2" + "+" + str(precedent_key[1]) + "x" + "+" + str(precedent_key[2]) + ")" + "=" + str(result[0]) + "x^2" + "+" + str(
            result[1]) + "x" + "+" + str(result[2]))
        for char in dict:
            if numpy.array_equal(dict[char],result):
                text += char
    return text
