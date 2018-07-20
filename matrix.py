import random

class Matrix:
     

    def __init__(self, nrows, ncols):
        
        self.matrixa = []
        self.nrows = nrows
        self.ncols = ncols
        
        for i in range(1,self.nrows+1):           # row
            self.matrixa.append([])
    
            for j in range(1,self.ncols+1):       #column
                self.matrixa[i-1].append(random.randint(0,9))
        
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
        c = Matrix(self.nrows, self.ncols)
        
        for i in range(0,self.nrows):   
            for j in range(0,self.ncols):                                      
                c.matrixa[i][j]= 0
        
        c.matrixa = [[self.nrows[i] for self.nrows in self.matrixa] for i in range(0,self.nrows)]
            
        return c
        
    def display(self):
            
        for i in range(0,self.nrows):
            for j in range(0,self.ncols):
                print(self.matrixa[i][j],end="  ")              
            print(" ")                    
            
            
print("產生矩陣A  3*3")
print("===============")
A=Matrix(3,3)
print(A.display())
print("===============")
print("產生矩陣B  3*3")
B=Matrix(3,3)
print(B.display())
print("===============")

print("======A+B======")
C=A.add(B)
print(C.display())
print("======A-B======")
D=A.sub(B)
print(D.display())
print("======A*B======")
E=A.mul(B)
print(D.display())
print("==Transpose A==")
F=A.transpose()
print(F.display())
print("==Transpose B==")
G=B.transpose()
print(G.display())
print("===============")