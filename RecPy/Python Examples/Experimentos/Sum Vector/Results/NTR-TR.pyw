#Soma de vetor 
#Vector Sum
# -*- coding: utf-8 -*-

import time as t
import sys
sys.setrecursionlimit(1000000)  

# **************** funcao em teste *******************

def sumVecTR(A, n, acc=0):
    if n==1:
        return acc
    return sumVecTR(A, n-1, acc + A[n])

# ****************************************************

def main():    

    #versao="2_7_16"
    versao="3_7_9"
    nome_funcao="sumVecTR"
    nomeArqResult="Results" +"_"+versao+"_"+nome_funcao+"_"+t.strftime("%Y%m%d_%H%M%S")+".csv"    
    resultsCSV = open(nomeArqResult, "w")
    resultsCSV.write("#Id;NomeFuncao;N;Tempo;Versao Python\n")    
    id=1    
    for n in range(10, 20,1):
        inicio=t.time()
        A=[0]*n
        for i in range(0,n):
            A[i]=i+1
        print(sumVecTR(A, n-1))
        fim = t.time()
        tempo=(fim - inicio)
        resultsCSV.write("%d;%s;%d;%s;%s\n" % (id,nome_funcao, n, tempo,versao))
        id=id+1
        resultsCSV.flush()
    resultsCSV.close()
    fim = t.time()
    print("Tempo de Execucao: ", (fim - inicio))

main()



