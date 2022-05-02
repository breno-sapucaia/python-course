with open("abc.tx", "a+") as file:
    print(file.read())


import os

os.remove("abc.tx")
