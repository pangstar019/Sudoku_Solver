from restrict import *
from input import *


if __name__ == '__main__':
    while True:
        matrix = inputpuzzle()
        if matrix != False:
            break 

    newmatrix = []
    for i, row in enumerate(matrix):
        line = []
        for j, value in enumerate(row):
            
            if value != 0:
                line.append(value)
            else:
                line.append([1,2,3,4,5,6,7,8,9])
        newmatrix.append(line)

    counter = 0

    while True:

        newmatrix = rowrestrict(newmatrix)
        newmatrix = squarerestrict(newmatrix)
        newmatrix = transpose(newmatrix)
        counter += 1
        if issolved(newmatrix) == True:
            if counter % 2 == 1:
                newmatrix = transpose(newmatrix)
            break
    
    print(f'\n\nThe puzzle is solved after {counter} steps:')
    print('-'*150)
    for i, row in enumerate(newmatrix):
        print(row)
    print('\n\n')
