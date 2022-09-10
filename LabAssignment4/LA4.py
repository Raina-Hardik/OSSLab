import numpy as np

#1
print("Numpy: " + np.__version__)

lst1 = [int(item) for item in input("Enter the list items : ").split()]

lst2 = [item for item in input("Enter the list items : ").split()]

unique, frequency = np.unique(np.array(lst1), return_counts = True)

print("List 1 \nEle : Freq")
print(dict(zip(unique, frequency)))
print("Total: {}".format(len(unique)))

unique, frequency = np.unique(np.array(lst2), return_counts = True)
print("\n\nList 2 \nEle : Freq")
print(dict(zip(unique, frequency)))
print("Total: {}".format(len(unique)))

#2
print(np.sort(np.array([item for item in input("Enter the Binary: ").split()]))[::-1])

#3
def remIndex(string = '9920103079', index = 0):
    print(string + '->', end = '')
    return string[:index] + string[index+1:]
print(remIndex())

#4
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)

#5
print(np.in1d(np.array([item for item in input("Enter the Array: ").split()]), np.array([item for item in input("Enter the Array: ").split()])))

#6
print(np.setxor1d(np.array([item for item in input("Enter the Array: ").split()]), np.array([item for item in input("Enter the Array: ").split()])))

#7
print(np.column_stack((np.array([item for item in input("Enter the Array: ").split()]), np.array([item for item in input("Enter the Array: ").split()]))))

#8
dimension = int(input("Dimension: "))
print("Matrix: ")

matrix = np.array(list(map(int, input().split()))).reshape(dimension, dimension)

print("Rank         : " + str(np.linalg.matrix_rank(matrix)))
print("Trace        : " + str(matrix.trace()))
print("Determinant  : " + str(np.linalg.det(matrix)))
