import os
import re

list_of_file = os.listdir(".")

for file in list_of_file:
    search_object = re.search(r'[\d \d]_rev.txt', file, re.M | re.I)
    if search_object:
        try:
            os.remove(file)
        except:
            print("unable to remove file")
