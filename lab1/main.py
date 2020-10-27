import numpy as np
from numpy import random

#Zadanie1

arrayZeros = np.zeros(10)
print(arrayZeros)

#Zadanie2

arrayFives = np.array([5,5,5,5,5,5,5,5,5,5])
print(arrayFives)

#Zadanie3

arrayTenToFifty = np.arange(10,51,1)
print(arrayTenToFifty)

#Zadanie4

matrixZeroToEight = np.arange(0,9,1).reshape(3,3)
print(matrixZeroToEight)

#Zadanie5

matrixEye = np.eye(3)
print(matrixEye)

#Zadanie6

matrixGaussian = random.random((5,5))
print(matrixGaussian)

matrixGaussian2 = random.normal(1,2,(5,5))
print(matrixGaussian2)

#Zadanie7

matrixZeroToOne = np.arange(0.01,1.01,0.01).reshape(10,10)
print(matrixZeroToOne)

#Zadanie8

arrayLinSpace = np.linspace(0,1,20)
print(arrayLinSpace)

#Zadanie9

matrixRandom = np.random.randint(1, 25, 25).reshape(5,5)
print(matrixRandom)

print(matrixRandom.sum())
print(matrixRandom.mean())
print(np.std(matrixRandom))

arrayColumnsSum = matrixRandom.cumsum(0)
print(arrayColumnsSum)

k = arrayColumnsSum[4,:]

print(k)

#Zadanie10

matrixZeroToHundred = np.random.randint(0, 100, 25).reshape(5,5)
print(matrixZeroToHundred)

print(np.median(matrixZeroToHundred))
print(np.min(matrixZeroToHundred))
print(np.max(matrixZeroToHundred))

#Zadanie11

matrixToTranspose = np.random.randint(0,100,24).reshape(4,6)
print(matrixToTranspose)

print(np.transpose(matrixToTranspose))

#Zadanie12

matrix1 = np.random.randint(0,100,9).reshape(3,3)
matrix2 = np.random.randint(0,100,9).reshape(3,3)

print(np.add(matrix1,matrix2))

#Zadanie13

matrix3 = np.random.randint(0,100,6).reshape(2,3)
matrix4 = np.random.randint(0,100,8).reshape(4,2)

print(np.matmul(matrix4,matrix3))
print(np.multiply(matrix4,2))





