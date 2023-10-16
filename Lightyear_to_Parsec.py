class parsec:
    def __init__(self,unit):
        self.unit=unit

    def calculation(self,lightyear):
        parsec=lightyear*self.unit
        return parsec
        
a=int(input("Enter the number of lighyears you want to convert into Parsec: "))
 
obj=parsec(0.306601)
print(a,"lightyears is equal to",obj.calculation(a),"Kilometers")


