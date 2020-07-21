# Program to multiply two matrices using nested loops
matrix1 =[]
matrix2 = []
result = []

#function for taking user input of matrix.
def matrixInput(R,C,matrix):
    print("Enter the entries rowwise:") 
    for i in range(R):
        a =[] 
        for j in range(C):
            a.append(int(input())) 
        matrix.append(a) 

#function to make resultant matrix
def matrixOutput(R,C,matrix): 
    for i in range(R):
        a =[] 
        for j in range(C):
            a.append(0) 
        matrix.append(a) 

#function to calculate product of two matrix
def prodOutput(X,Y,result):
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

#getting user's input for rows and columns for matrix 1. 
mat1_row = int(input ("Enter number of rows in matrix 1:"))
mat1_col = int(input ("Enter number of columns in matrix 1:"))

#getting user's input for rows and clumns for matrix 2.
mat2_row = int(input ("Enter number of rows in matrix 2:"))
mat2_col = int(input ("Enter number of columns in matrix 2:"))

# for m*n and n*p
if (mat1_col == mat2_row):
    print("For First Matrix:")
    matrixInput(mat1_row,mat1_col,matrix1)
    print("For Second Mtrix:")
    matrixInput(mat2_row,mat2_col,matrix2)
    print("Please verify both matrix :")
    print("matrix 1:",matrix1)
    print("matrix 2:",matrix2)
    a = input("press Y if correct else N:")
    if (a == 'Y'or a=='y'):
        matrixOutput(mat1_row,mat2_col,result)
        prodOutput(matrix1,matrix2,result)
        print(result)
    elif (a=='N' or a=='n'):
        print("please run the script once again")
        print("script is being terminated")
else:
    print("Please enter the same no of columns and row in both matrix")

    