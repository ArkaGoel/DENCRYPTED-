import hashlib
print("Hello, Welcome to DEECRYPTED!!")
print("Decrypt any Password here (NOTE- ONLY MD5 HASHES ALLOWED)")
print("██████╗░███████╗███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗███████╗██████╗░██╗██╗")
print("██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║██║")
print("██║░░██║█████╗░░█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░░██║░░██║██║██║")
print("██║░░██║██╔══╝░░██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██╔══╝░░██║░░██║╚═╝╚═╝")
print("██████╔╝███████╗███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░███████╗██████╔╝██╗██╗")
print("╚═════╝░╚══════╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═════╝░╚═╝╚═╝")
print("If error comes that means that the password is not in wordlist")
type_hash = input("Enter MD5 hash: ")
wordlist = input("Enter File Name: ")
try:
    pass_file = open(wordlist, 'r')
except:
    print("No password file found")
    quit();
for word in pass_file:
    encode = word.encode("utf-8")
    digest = hashlib.md5(encode.strip()).hexdigest();
    if digest == type_hash:
        print("Password Found 😈!!");
        print("The password is " + word);
        break