from affine import *

def encrypt_2(message:str,key1:tuple,key2:tuple,dic:dict):
    cipher_text = ""
    i = 1
    for carac in message:
        if i == 1:
            var = key1
        elif i == 2:
            var = key2
            key1 = key2
            key2 = (lower_coef(numpy.convolve(key1[0], key2[0])), lower_coef(numpy.polyadd(key1[1], key2[1])))
        else:
            var = key2
            key1 = key2

            key2 = (lower_coef(numpy.convolve(key1[0], key2[0])), lower_coef(numpy.polyadd(key1[1], key2[1])))
        result = numpy.convolve(var[0], dic[carac])
        result = numpy.polyadd(result, var[1])
        result = lower_coef(result)
        print("(" + str(var[0][0]) + "x²" + "+" + str(var[0][1]) + "x" + "+" + str(var[0][2]) + ")(" + str(
            dic[carac][0]) + "x²" + "+" + str(dic[carac][1]) + "x" + "+" + str(dic[carac][2]) + ")+" + str(
            var[1][0]) + "x²" + "+" + str(var[1][1]) + "x" + "+" + str(var[1][1]) + "=" + str(result[0]) + "x²" + "+" + str(
            result[1]) + "x" + "+" + str(result[2]))
        for char in dic:
            if numpy.array_equal(dic[char], result):
                cipher_text += char
                i += 1
    return cipher_text

def decrypt_2(cipher_text:str,key1:tuple,key2:tuple,dic:dict):
    text = ""
    i = 1
    using = key1
    for elem in cipher_text:
        print(key1,key2)
        if i == 1:
            new_key = numpy.convolve(using[0], using[0])
            new_key = lower_coef(new_key)
            i+=1
        elif i == 2:
            using = key2
            new_key = numpy.convolve(using[0], using[0])
            new_key = lower_coef(new_key)
            key1 = key2
            key2 = (lower_coef(numpy.convolve(key1[0], key2[0])), lower_coef(numpy.polyadd(key1[1], key2[1])))
            i+=1
        else:
            using = key2
            new_key = numpy.convolve(using[0], using[0])
            new_key = lower_coef(new_key)
            key1 = key2
            key2 = (lower_coef(numpy.convolve(key1[0], key2[0])), lower_coef(numpy.polyadd(key1[1], key2[1])))
            i+=1
        while ((numpy.sum(new_key) != 1 or new_key[-1] != 1)):
            precedent_key = new_key
            new_key = numpy.convolve(using[0], precedent_key)
            new_key = lower_coef(new_key)
        result = numpy.polysub(dict[elem], key1[1])
        result = numpy.convolve(result, precedent_key)
        result = lower_coef(result)
        print("(" + str(dict[elem][0]) + "x²" + "+" + str(dict[elem][1]) + "x" + "+" + str(dict[elem][2]) + "-(" + str(
            key1[1][0]) + "x²" + "+" + str(key1[1][1]) + "x" + "+" + str(key1[1][2]) + "))(" + str(
            precedent_key[0]) + "x²" + "+" + str(precedent_key[1]) + "x" + "+" + str(
            precedent_key[2]) + ")" + "=" + str(result[0]) + "x²" + "+" + str(
            result[1]) + "x" + "+" + str(result[2]))
        for char in dict:
            if numpy.array_equal(dict[char], result):
                text += char
    return text