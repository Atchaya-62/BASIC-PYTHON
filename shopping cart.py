#write a python prog to create a class representing a shopping cart include methods like add,remove items and print the bill

class mart:

    dict={"Milk":30 , "Chocolate":10 , "Sugar":35 , "Tea powder":40 , "Curd": 20 , "Soap":30}

    def __init__(self,name):
        self.name=name
        self.li=[]
        self.total= 0
        print(mart.dict)

    def print(self):
        print(self.li)

    def add(self,item):
        self.li.append(item)

    def remove(self,a):
        self.li.remove(a)
    

    def bill(self):
        print("Name :\n",self.name)
        for i in self.li:
            print(i,        mart.dict[i],"\n")
            self.total += mart.dict[i]
        print("Total:   " ,self.total)

name=input("Enter name ")
obj=mart(name)
print("Add things to your Cart \n If enough type stop")
n=True
while(n==True):
   k=input()

   if (k=="stop"):
       n=False
   else:
       obj.add(k)
obj.print()
print("Remove things from your Cart \n If enough type stop")

o=True
while(o==True):
    a=input()
    if (a=="stop"):
        o=False
    else:
        obj.remove(a)
obj.bill()
        


