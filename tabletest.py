print ("jd starting")
import csv


class myClass:
    #name = ""
    #age = 0
    #hobbies = ""

    def __init__(self, var1, var2, var3):
        self.name = var1
        self.age = var2
        self.hobbies = var3
        
        
my_list = []

with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        my_list.append(myClass(str(row[0]), int(row[1]), str(row[2:])))
        
        
print (my_list[1])
#print( my_list.keys())

print("jd finished")