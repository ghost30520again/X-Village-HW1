import random
from copy import deepcopy

class Matrix:

    def __init__(self, nrows, ncols):
        self.matrixa = []
        self.nrows = nrows
        self.ncols = ncols
        
        for i in range(1,self.nrows+1):           # row
            self.matrixa.append([])
    
            for j in range(1,self.ncols+1):       #column
                self.matrixa[i-1].append(random.randint(0,9))
        print(self.matrixa)

    def add(self, m):
        self.nrows
        self.ncols 
        c = Matrix(self.nrows, self.ncols)
        for i in range(0,self.nrows):   
            for j in range(0,self.ncols):                                      
                c.matrixa[i][j]= self.matrixa[i][j]+m.matrixa[i][j]
        return c

    def sub(self, m):
        self.nrows
        self.ncols 
        c = Matrix(self.nrows, self.ncols)
        for i in range(0,self.nrows):   
            for j in range(0,self.ncols):                                      
                c.matrixa[i][j]= self.matrixa[i][j]-m.matrixa[i][j]
        return c

    def mul(self, m):
        self.nrows
        self.ncols 
        c = Matrix(self.nrows,m.ncols)
        
        for i in range(0,self.nrows):   
            for j in range(0,m.ncols):                                      
                c.matrixa[i][j]= 0
    
        for i in range(0,self.nrows): 
            for j in range(0,m.ncols):
                for k in range(0,self.ncols):                                             
                    c.matrixa[i][j] += self.matrixa[i][k]*m.matrixa[k][j]                             
        return c

    def transpose(self):
        self.nrows
        self.ncols
        c = Matrix(self.nrows, self.ncols)
        
        for i in range(0,self.nrows):   
            for j in range(0,self.ncols):                                      
                c.matrixa[i][j]= 0
        
        c = [[self.nrows[i] for self.nrows in self.matrixa] for i in range(0,self.nrows)]
        
        return c
    
    def display(self):
        for i in range(0,self.nrows):
            for j in range(0,self.ncols):
                print(self.matrixa[i][j],end="  ")              
            print(" ") 

A=Matrix(3,2)
B=Matrix(2,4)

#A.add(B).display()             #輸出結果的第三行是用來存儲結果的矩陣
#A.sub(B).display()
A.mul(B).display()              #矩陣3*2乘上矩陣2*4=矩陣3*4   
#A.transpose()




