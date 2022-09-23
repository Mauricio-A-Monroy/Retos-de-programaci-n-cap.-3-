from sys import stdin
import fractions
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def sumacplx(a,b):
    real=a[0]+b[0]
    img=a[1]+b[1]
    return real,img

def multicplx(a,b):
    real=(a[0]*b[0])-(a[1]*b[1])
    img=(a[0]*b[1])+(a[1]*b[0])
    return real,img

def acc(v,m):
    ans=[]
    for i in range(len(m)):
        sum=[]
        for j in range(len(v)):
            sum.append(multicplx(m[i][j],v[j]))
        aux=[sum[0]]
        for j in range(1,len(sum)):
            a=sumacplx(aux[0],sum[j])
            aux=[]
            aux.append(a)
        ans.append(aux)
    return ans

def m_x_m(m1,m2):
    ans=[]
    for i in range(len(m1)):
        aux=[]
        for j in range(len(m2)):
            comp=0
            for k in range(len(m2)):
                comp+=m1[i][k]*m2[k][j]
            aux.append(comp)
        ans.append(aux)
    return ans 

def m_x_v(m,v):
    ans=[]
    for i in range(len(m)):
        comp=0
        for j in range(len(v)):
            comp+=m[i][j]*v[j]
        ans.append(comp)
    return ans

#Programa que calcula la cantidad de canícas en cada vertice despues de una cantidad de clics.
def marble_exp():
    """El usuario debe ingresar el tamaño  una matriz booleana, luego números "0" y "1" separados por un espacio en blanco, 
    la cantidad de números va a ser igual al del tamaño de la matriz, presionar enter después de ingresar cada fila,
    luego el estado inicial del sistema, representado como un vector de números naturales, separados por un espacio en blanco, 
    por último, debe escribir la cantidad de clics
    """
    n=int(stdin.readline().strip())
    matriz=[]
    for _ in range(n):
        aux=list(map(int,stdin.readline().strip().split()))
        matriz.append(aux)
    print(matriz)
    s_state=list(map(int,stdin.readline().strip().split()))
    clicks=int(stdin.readline().strip())
    for _ in range(clicks):
        s_state=m_x_v(matriz,s_state)
    print(s_state)
    
#Programa que calcula la cantidad de canícas en cada vertice despues de una cantidad de clics.
def marble_exp_frac():
    """El usuario debe ingresar el tamaño  una matriz, luego las fracciones separadas por un espacio en blanco, 
    la cantidad de fracciones va a ser igual al del tamaño de la matriz, presionar enter después de ingresar cada fila,
    luego el estado inicial del sistema, representado como un vector de números naturales, separados por un espacio en blanco, 
    por último, debe escribir la cantidad de clics
    """
    n=int(stdin.readline().strip())
    matriz=[]
    for _ in range(n):
        aux=stdin.readline().strip().split()
        aux=[float(fractions.Fraction(x)) for x in aux]
        matriz.append(aux)
    s_state=stdin.readline().strip().split()
    s_state=[float(fractions.Fraction(x)) for x in s_state]
    clicks=int(stdin.readline().strip())
    for _ in range(clicks):
        s_state=m_x_v(matriz,s_state)
    print(s_state)

def multislit_exp():
    """El usuario debe ingresar el número de rendijas, presionar enter e ingresar el número de objetivos, 
    luego ingresar la probabilidad que tiene una bala de llegar a un objetivo desde una rendija, 
    debe indicar el primer y último objetivo que puede alcanzar una bala después de pasar por una rendija, es decir, 
    para la primera rendija la bala puede alcanzar desde el primer objetivo hasta el tercer objetivo, 
    el usuario debe ingresar “1 3”, después de esto las probabilidades que tiene la bala de cada objetivo, 
    debe ingresar una probabilidad y luego presionar enter.  
    """
    n_slit=int(stdin.readline().strip())
    n_targ=int(stdin.readline().strip())
    matriz=[]
    matriz.append([0]*(1+n_targ+n_slit))
    for i in range(1,n_slit+1):
        matriz.append([0]*(1+n_targ+n_slit))
        matriz[i][0]=float(1/n_slit)
    for i in range(n_slit+1,1+n_targ+n_slit):
        matriz.append([0]*(1+n_targ+n_slit))
        matriz[i][i]=1
    for i in range(1,n_slit+1):
        s,f=stdin.readline().strip().split()
        for j in range(n_slit+int(s),n_slit+int(f)+1):
            matriz[j][i]=float(fractions.Fraction(stdin.readline().strip()))
    matriz=m_x_m(matriz,matriz)
    vector=[]
    vector.append([0]*(1+n_targ+n_slit))
    vector[0]=1
    vector=m_x_v(matriz,vector)
    for i in range(len(matriz)):
        print(matriz[i])
    print("")
    print(vector)

#Programa que calcula la cantidad de canícas en cada vertice despues de una cantidad de clics.
def marble_exp_cmpx():
    """La entrada de esta función consta de un n que es el tamaño de la matriz, las siguientes n líneas 
    constan de n números complejos representados como tuplas cartesianas de la siguiente forma "a,b c,d e,f ...", 
    luego un vector de n números complejos representados como tuplas cartesianas (se debe ingresar como se mencionó anteriormente) 
    y por último la cantidad de clics
    """
    n=int(stdin.readline().strip())
    matriz=[]
    for _ in range(n):
        aux=stdin.readline().strip().split()
        for i in range(n):
            aux[i]=(int(aux[i][0]),int(aux[i][2]))
        matriz.append(aux)
    s_state=stdin.readline().strip().split()
    for i in range(n):
        s_state[i]=(int(s_state[i][0]),int(s_state[i][2]))
    clicks=int(stdin.readline().strip())
    for _ in range(clicks):
        s_state=acc(s_state,matriz)
    print(s_state)

#función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados
def graf():
    """El usuario debe incresar las componentes del vector de la siguiente forma: (1,2) (3,4), las cuales representan el vector
    [1+2i,3+4i], tener en cuenta que el vector debe estar normalizado"""
    arr = stdin.readline().strip().split()
    counts = {}
    for i in range(1, len(arr) + 1):
        counts[str(i)] = (int(arr[i - 1][1])) ** 2 + (int(arr[i - 1][1])) ** 2
    print(counts)

