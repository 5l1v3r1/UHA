import uha

import time

from os import listdir
from os.path import isfile, join

file_names = [f for f in listdir("to_hash\\") if isfile(join("to_hash\\", f))]


times = []

for i in range(len(file_names)):
    start = time.time()
    filename = file_names[i]
    try:
        file = open("to_hash\\" + filename ,"rb").read()
        hash_file = uha.uHash(file)
        end = time.time()
        print("SUCCSESFULLY HASHED " + filename + " WITH A LENGTH OF " + str(len(hash_file)) + " A HASH OF " + str(hash_file) + " AND A TIME OF " + str(end - start) + " s")
    except:
        print("HASHING " + filename + " FAILED")