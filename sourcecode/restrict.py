def rowrestrict(matrix):
    for i, row in enumerate(matrix):
        rowrestriction = []
        for j, value in enumerate(row):
            if isinstance(value, int):
                rowrestriction.append(value)
            elif len(value) == 1:
                num = int(''.join(str(x) for x in value))
                rowrestriction.append(num)
                row[j] = num
        for j, value in enumerate(row):
            if isinstance(value, list):
                value = list(set(value).difference(rowrestriction))
                row[j] = value
        matrix[i] = row
    return matrix

def squarespecific(j, row, value):
    if isinstance(value, int):
        sqrestrict = value
    elif len(value) == 1:
        num = int(''.join(str(x) for x in value))
        sqrestrict = num
        row[j] = num
    elif len(value) > 1:
        sqrestrict = None
    return sqrestrict, row

def squarerestriction(matrix):
    sq1restriction = []; sq2restriction = []; sq3restriction = []
    sq4restriction = []; sq5restriction = []; sq6restriction = []
    sq7restriction = []; sq8restriction = []; sq9restriction = []
    
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if i < 3:
                if j < 3:
                    [restriction, newrow] = squarespecific(j, row, value)
                    if restriction != None:
                        sq1restriction.append(restriction)
                    matrix[i] = newrow
                if 3 <= j and j < 6:
                    [restriction, newrow] = squarespecific(j, row, value)
                    if restriction != None:
                        sq2restriction.append(restriction)
                    row = newrow
                if 6 <= j:
                    [restriction, newrow] = squarespecific(j, row, value)
                    if restriction != None:
                        sq3restriction.append(restriction)
                    matrix[i] = newrow
            if 3 <= i and i < 6:
                if j < 3:
                    [restriction, newrow] = squarespecific(j, row, value)
                    if restriction != None:
                        sq4restriction.append(restriction)
                    matrix[i] = newrow
                if 3 <= j and j < 6:
                    [restriction, newrow] = squarespecific(j, row, value)
                    if restriction != None:
                        sq5restriction.append(restriction)
                    matrix[i] = newrow
                if 6 <= j:
                    [restriction, newrow] = squarespecific(j, row, value)
                    if restriction != None:
                        sq6restriction.append(restriction)
                    matrix[i] = newrow
            if 6 <= i:
                if j < 3:
                    [restriction, newrow] = squarespecific(j, row, value)
                    if restriction != None:
                        sq7restriction.append(restriction)
                    matrix[i] = newrow
                if 3 <= j and j < 6:
                    [restriction, newrow] = squarespecific(j, row, value)
                    if restriction != None:
                        sq8restriction.append(restriction)
                    matrix[i] = newrow
                if 6 <= j:
                    [restriction, newrow] = squarespecific(j, row, value)
                    if restriction != None:
                        sq9restriction.append(restriction)
                    matrix[i] = newrow
    return sq1restriction, sq2restriction, sq3restriction, sq4restriction, sq5restriction, sq6restriction, sq7restriction, sq8restriction, sq9restriction

def squarerestrict(matrix):
    [
        sq1restriction, sq2restriction, sq3restriction, 
        sq4restriction, sq5restriction, sq6restriction, 
        sq7restriction, sq8restriction, sq9restriction
    ] = squarerestriction(matrix)
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if i < 3:
                if j < 3:
                    if isinstance(value, list):
                        value = list(set(value).difference(sq1restriction))
                        row[j] = value
                    matrix[i] = row
                if 3 <= j and j < 6:
                    if isinstance(value, list):
                        value = list(set(value).difference(sq2restriction))
                        row[j] = value
                    matrix[i] = row
                if 6 <= j:
                    if isinstance(value, list):
                        value = list(set(value).difference(sq3restriction))
                        row[j] = value
                    matrix[i] = row
            if 3 <= i and i < 6:
                if j < 3:
                    if isinstance(value, list):
                        value = list(set(value).difference(sq4restriction))
                        row[j] = value
                    matrix[i] = row
                if 3 <= j and j < 6:
                    if isinstance(value, list):
                        value = list(set(value).difference(sq5restriction))
                        row[j] = value
                    matrix[i] = row
                if 6 <= j:
                    if isinstance(value, list):
                        value = list(set(value).difference(sq6restriction))
                        row[j] = value
                    matrix[i] = row
            if 6 <= i:
                if j < 3:
                    if isinstance(value, list):
                        value = list(set(value).difference(sq7restriction))
                        row[j] = value
                    matrix[i] = row
                if 3 <= j and j < 6:
                    if isinstance(value, list):
                        value = list(set(value).difference(sq8restriction))
                        row[j] = value
                    matrix[i] = row
                if 6 <= j:
                    if isinstance(value, list):
                        value = list(set(value).difference(sq9restriction))
                        row[j] = value
                    matrix[i] = row
    return matrix

def transpose(matrix):
    newmatrix = []
    [r1, r2, r3, r4, r5, r6, r7, r8, r9] = map(list, matrix)
    for i in range(len(matrix)):
        row = [
            r1[i], r2[i], r3[i], r4[i], r5[i], r6[i], r7[i], r8[i], r9[i]
        ]
        newmatrix.append(row) 
    return newmatrix

def issolved(matrix):
    for i, row in enumerate(matrix):
        if not all(isinstance(value, int) for value in row):
            return False
    return True