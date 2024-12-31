import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("apt install python")
    os.system("apt install python2")
    os.system("apt install python3-pip")
    os.system("apt install nodejs-lts")
    os.system("apt install npm")
    os.system("npm i string")
    os.system("git pull")

elif c == "1":
    os.system("apt install python")
    os.system("apt install python2")
    os.system("apt install python3-pip")
    os.system("apt install nodejs-lts")
    os.system("apt install npm")
    os.system("npm i string")
    os.system("git pull")
    print("Done.")
