import replace
import affine
import affine_rec

def main():
    choose = int(input("Choose which cipher you want to use:\n1-replace\n2-affine\n3-affine reccurent\n"))
    message = input("Write your message:\n")
    if choose == 1:
        key = replace.key()
        cipher_text = replace.encode_0(key,message)
        open_text = replace.decode_0(key,cipher_text)
        print(cipher_text,open_text,sep = " ")
    elif choose == 2:
        a = list(map(int,input("choose coefs of a: ").split()))
        b = list(map(int,input("choose coefs of b: ").split()))
        key = (a,b)
        dict = affine.generate_dict(affine.generate_polynomes(3,3))
        cipher_text = affine.encrypt(message,key,dict)
        open_text = affine.decrypt(cipher_text,key,dict)
        print(cipher_text,open_text,sep = " ")
    elif choose == 3:
        a = list(map(int,input("choose coefs of a: ").split()))
        b = list(map(int,input("choose coefs of b: ").split()))
        c = list(map(int,input("choose coefs of c: ").split()))
        d = list(map(int,input("choose coefs of d: ").split()))
        key1 = (a,b)
        key2 = (c,d)
        dict = affine.generate_dict(affine.generate_polynomes(3,3))
        cipher_text = affine_rec.encrypt_2(message,key1,key2,dict)
        open_text = affine_rec.decrypt_2(cipher_text,key1,key2,dict)
        print(cipher_text,open_text,sep = " ")
if __name__ == "__main__":
    main()