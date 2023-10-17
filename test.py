import random #import random so we can use random integers in our matrices
import time #import time to track the time


def generate_matrix(row, col): #function to generate matrices
    return [[random.randint(1, 100) for a in range(col)] for b in range(row)]
    # the code above basically says generate a random number between 1 and 100
    # for each colum and each rown in the matrix


def multiply_matrices(matrix1, matrix2): #function to multiplty the two matrices
    resultmatrix = [[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))] #creates an array for the resulting array after multiplying
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                resultmatrix[i][j] += matrix1[i][k] * matrix2[k][j]
    # the code above iterates over the colums and rows of both matrices one and two and multiplies them
    return resultmatrix

start_time = time.time() #record time taken to run code

size = 2
    # for size = 2, my matrices are starting off with 2 columns and 2 rows
    # and below when the genrate_matrix function is called, the size is put in as the rows and columns parameters
while size <= 100:
    #100 rows and columns
    matrix1 = generate_matrix(size, size) #calls first function to generate first matrix
    matrix2 = generate_matrix(size, size) #calls first function to generate second matrix
    result_matrix = multiply_matrices(matrix1, matrix2) #calls second fucntion to multiply both matrices
    if size == 2 or size == 20 or size == 40 or size == 60 or size == 80 or size == 100 : # this is to show the times at different values of n
        lapse_time = time.time() # records time at each value of n
        lapsed_time = lapse_time - start_time 
        print(f"The time at matrix size {size} is: {lapsed_time:.6f} seconds") # prints time at the various values of n
    size += 1 # increase the size of the matrices by one

end_time = time.time() # records the time to mark end of the program
execution_time = end_time - start_time # total execution time of the entire program

print(f"Total Execution Time: {execution_time:.6f} seconds") # prints the execution time
 