import hashlib

flag = 0

pass_hash = input("Enter the md5 hash code: ")

wordlist = input("Enter the File name here: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("There's no file such like that, hence no file found.")
    quit()

for word in pass_file:
    
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    


    print(word)
    print(digest)
    print(pass_hash)
    

    if digest == pass_hash:
        print("Password found, cheer up!")
        print("The followiing password is: " + word)
        flag = 1
        break

if flag == 0:
    print("password/passphrase is not in the program list")
