def  leer_archivo():
    #sopadeletras={}
    '''
    sopad=[[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    [26,27,28,29,30]
    ]
    '''
    j=0
    fsopa=open('SOP.DAT','r')
    for indice,linea in enumerate(fsopa):
        #print(indice)
        if indice==0:
            x=int(linea[0])
            y=int(linea[2])
            #sopad = [['']*y]*x
            sopad = [[0 for h in range(y)] for k in range(x)] 
            
        
        elif indice>0 and indice<=x:
            
            i=0
            for i in range(len(linea)-1):
                print(j,i)
                letra=linea[i]
                sopad[j][i]=letra
            j=j+1
            #print(j)
        #else:
            #continue
    for i in range(0,x):
        for j in range(0,y):
            print(sopad[i][j], end=' ')
        print('\n')
        
def main():
    leer_archivo()
    

if __name__ == "__main__":
    main()

