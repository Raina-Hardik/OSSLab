import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def pltq1(nValues = 256):
    values = np.linspace(-np.pi, np.pi, nValues, endpoint=True)
    cosine, sine = np.cos(values), np.sin(values)
    plt.plot(values, cosine)
    plt.plot(values, sine)
    plt.show()

def pltq2():
    values = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    cosine, sine = np.cos(values), np.sin(values)
    # Create a figure of size 8values6 inches, 80 dots per inch
    plt.figure(figsize=(8, 6), dpi=80)
    # Create a new subplot from a grid of 1values1
    plt.subplot(1, 1, 1)
    # Plot cosine with a blue continuous line of width 1 (pivaluesels)
    plt.plot(values, cosine, color="blue", linewidth=1.0, linestyle="-")

    # Plot sine with a green continuous line of width 1 (pivaluesels)
    plt.plot(values, sine, color="green", linewidth=1.0, linestyle="-")
    # Set values ticks
    plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
    plt.yticks(np.linspace(-4, 4, 9, endpoint=True))
    # Set y limits
    plt.ylim(-1.0, 1.0)
    # Set y ticks
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    # Save figure using 72 dots per inch
    plt.savefig("evaluesercise_2.png", dpi=72)
    plt.show()

def pltq3():
    values = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    cosine, sine = np.cos(values), np.sin(values)
    plt.plot(values, cosine, color="blue", linewidth=2.5, linestyle="-", label="cosine")
    plt.plot(values, sine, color="red", linewidth=2.5, linestyle="-", label="sine")
    plt.legend(loc='upper left')
    plt.show()

def pltq4(n = 256):
    values = np.linspace(-np.pi, np.pi, n, endpoint=True)
    Y = np.sin(2 * values)
    plt.plot(values, Y + 1, color='blue', alpha=1.00)
    plt.plot(values, Y - 1, color='blue', alpha=1.00)
    plt.show()
    
def pltq5(n =1024):
    values = np.random.normal(0,1,n)
    Y = np.random.normal(0,1,n)
    plt.scatter(values,Y)
    plt.show()

def pltq6(n = 12):
    values = np.arange(n)
    Y1 = (1 - values / float(n)) * np.random.uniform(0.5, 1.0, n)
    plt.bar(values, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.show()
    Y2 = (1 - values / float(n)) * np.random.uniform(0.5, 1.0, n)
    plt.bar(values, -Y2, facecolor='#ff9999', edgecolor='white')
    plt.show()

def pltq7(nValues = 256):
    values = [ -np.pi, -np.pi/4, -np.pi/2]
    values += [values*-1 for values in values]
    values.append(0)
    values.sort()
    cosine, sine = np.cos(values), np.sin(values)
    plt.plot(values, cosine)
    plt.plot(values, sine)
    plt.show()

def matplotlibQuestions():  
    pltq1()
    pltq2()
    pltq3()
    pltq4()
    pltq5()
    pltq6()
    pltq7()

# Scipy Questions

import scipy as sp
import numpy as np

def scipyQ1(filename = './test.txt'):
    arr = np.ones((4,4), 'uint8')
    print('ARR: WRITE: \n', arr)    
    np.savetxt(filename, arr, delimiter=',')
    
    arr2 = np.genfromtxt(filename, delimiter=',', dtype='uint8')
    print('ARR READ: \n', arr2)

def scipyQ2(num = 276489):
    return sp.special.cbrt(num)    
    
def scipyQ3():
    matrixA = np.array([[4,5],[3,2]])
    matrixB = matrixA.copy()
    print('Det A: ', sp.linalg.det(matrixA))
    print('Det B: ', sp.linalg.det(matrixB))

def scipyQ4():
    mat = np.array([[4,5],[3,2]])
    print('INV: \n', sp.linalg.inv(mat))
    
def scipyQ5():
    a = np.array([[5, 4], [6, 3]])
    w,v= np.linalg.eig(a)
    print('E-value:', w)
    print('E-vector', v)
    
def scipyQ6():
    sparseMatrixA = sp.sparse.csr_matrix((3, 4), dtype = np.int8).toarray()
    sparseMatrixB = sp.sparse.csr_matrix((3, 3), dtype = np.int8).toarray()
    print(sp.sparse.triu(sparseMatrixA))
    print(sp.sparse.tril(sparseMatrixB))
    
    
def scipyQuestions():   
    scipyQ1()
    print('Root: ', scipyQ2())
    scipyQ3()
    scipyQ4()
    scipyQ5()
    scipyQ6()
    
matplotlibQuestions()
scipyQuestions()