# nqueens
# -*- coding: utf-8 -*-
import random
class Solver_8_queens:
    '''
    Dummy constructor representing proper interface
    '''
    def __init__(self, pop_size=300, cross_prob=0.9, mut_prob=0.03):
        self.pop_size = pop_size
        self.cross_prob = cross_prob
        self.mut_prob = mut_prob
        pass
    '''
    Dummy method representing proper interface
    '''
    def solve(self, min_fitness=0.9, max_epochs=100):
        osobi=[]
        pop=0
        while pop < self.pop_size:
            i=0
            osob=[]
            while i < 56:
                osob.append(0)
                i+=1
            j=0
            while osob.count(1)<8:
                osob.insert(random.randint(0,56),1)
            osobi.append(osob)
            pop+=1

        epoch=0
        fitness=0
        fitlist=osobi
        fts=0
        resi=0
        res=[]
        end=0
        while fts < min_fitness:
            for i in range(len(fitlist)):
##            while i < len(osobi):
                errors=0
                lx=[]
                ly=[]
                for j in range(len(fitlist[i])):
                    x=0
                    y=0
                    if fitlist[i][j]==1:
                        x=j//8 #строка 
                        y=j%8 #столбец
                        lx.append(x) #массив из строк
                        ly.append(y) #массив из столбцов
                        #j+=1

                m=0    
                for m in range(len(lx)-1):
                    n=m+1
                    while (n<len(lx)):
                        if (abs(lx[n]-lx[m])==abs(ly[n]-ly[m])) or (len(lx)!=8) or (len(ly)!=8):
                            errors+=1
                        n+=1

                errors=errors+(len(lx)-len(set(lx)))+(len(ly)-len(set(ly)))
                fitness=1/(1+errors)
##                if fitness>fts:
##                    fts=fitness
##                    if fts>=min_fitness:
##                        resi=i
##                        break
                        


                        
                fitlist[i].append(fitness)
            fitlist.sort(key=lambda i: i[63], reverse=True)
            
            for element in range(len(fitlist)):
                for e in range(len(fitlist[element])):
                    if fitlist[element][64]>=min_fitness:
                        resi=element
            if len(fitlist)>self.pop_size:
                for elem in range(self.pop_size, len(fitlist)):
                    fitlist.pop()
            
            for el in range(len(fitlist)):
                fitlist[el].pop()
            v=0
            stop=(len(fitlist)-60)
            
            while v < stop:
                j=v+1
                while j < stop:
                    if random.random() >=self.cross_prob:
                        dot=random.randint(1,62)
                        child1=[]
                        child2=[]
                        for k in range(dot):
                            child1.append(fitlist[v][k])
                            child2.append(fitlist[j][k])
                        while dot < len(fitlist[j]):
                            child1.append(fitlist[j][dot])
                            child2.append(fitlist[v][dot])
                            dot+=1
                        fitlist.append(child1)
                        fitlist.append(child2)                  
                        j=stop                          
                    else:
                        j+=1
                v+=1
##            print(fitlist)

            best=80
            while best<len(fitlist):
                if random.random() < self.mut_prob:
                    if fitlist[best][random.randint(0,63)]==0:
                        fitlist[best][random.randint(0,63)]=1
                    else:
                        fitlist[best][random.randint(0,63)]=0
                best+=1
##            print(fitlist)
            epoch+=1
            if epoch>=100:
                fts=99
           
##        res=fitlist
  
        if epoch<100:
            res=fitlist[resi]        
            resj=0
##            while resj <64:
            for elt in range(len(fitlist[resi])):
                if fitlist[resi][elt]==0:
                    res[elt]='+'
                else:
                    res[elt]='Q'
##                j+=1
##                resj+=1     
            best_fit=fts
            epoch_num=epoch
            visualization=res
        else:
            best_fit=None
            epoch_num=None
            visualization=None
            
            
        return best_fit, epoch_num, visualization
