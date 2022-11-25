def key():
    dict = {"a":"",
            "b":"",
            "c":"",
            "d":"",
            "e":"",
            "f":"",
            "g":"",
            "h":"",
            "i": "",
            "j": "",
            "k": "",
            "l": "",
            "m": "",
            "n": "",
            "o": "",
            "p": "",
            "q": "",
            "r": "",
            "s": "",
            "t": "",
            "u": "",
            "v": "",
            "w": "",
            "x": "",
            "y": "",
            "z": "",

            }
    for key in dict:
        n = input("Put a character")
        dict[key] = n
    return dict
def encode_0(key,open_text):
    cipher_text = ""
    for elem in open_text:
        cipher_text += key[elem]
    return cipher_text

def decode_0(key, cipher_text):
    open_text = ""
    for elem in cipher_text:
        for key2, value in key.items():
            if value == elem:
                open_text += key2
                break
    return open_text