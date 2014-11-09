"""
    Arkadiusz Gabrys
    arkadiusz.gabrys@fau.de
    qe83mepi

    AdvPTEx
"""

# ----------------------------
# main class
class Matrix:
        def __init__(self, rows, columns):
                if rows < 1 or columns < 1:
                        raise NameError("Wrong matrix size!")
                
                self.rows = rows
                self.columns = columns
                self.__matrix = [[0.0 for j in range(0, columns)] for i in range(0, rows)]

        def __getitem__(self, k):
                if k >= 0 and k < self.rows:
                        return self._Matrix__matrix[k]
                else:
                        raise NameError("Wrong matrix index!")

        def __mul__(self, other):
                if self.columns != other.rows:
                        raise NameError("Matrices can not be multiplied. Number of columns of the first matrix must be equal to number of rows of the second one!")

                # create new result matrix
                result = Matrix(self.rows, other.columns)

                for r in range(0, result.rows):
                        for c in range(0, result.columns):
                                for rc in range(0, self.columns):
                                        result._Matrix__matrix[r][c] += self._Matrix__matrix[r][rc] * other._Matrix__matrix[rc][c]

                return result

# ----------------------------
# helper functions
def getDimension(prompt):
        while True:
                try:
                        tmp = input(prompt)
                        if tmp <= 0:
                                print " ! Error: Dimension can't be zero or negative!"
                                continue

                        if tmp%1 != 0:
                                print " ! Error: Dimension can't be fraction!"
                                continue

                        tmp = int(tmp)
                except:
                        print " ! Error: Wrong type!"
                        continue
                else:
                        return tmp

def getInput(prompt):
        while True:
                try:
                        tmp = int(input(prompt))
                except:
                        print " ! Error: Wrong type!"
                        continue
                else:
                        return tmp
        

def writeMatrix(matrix):
        if not(isinstance(matrix, Matrix)):
                raise NameError("Given parameter is not a Matrix object!")

        for r in range(0, matrix.rows):
                for c in range(0, matrix.columns):
                        print "%d " % matrix[r][c],

                print #new line after each row

def fillMatrix(matrix):
        if not(isinstance(matrix, Matrix)):
                raise NameError("Given parameter is not a Matrix object!")

        for r in  range(0, matrix.rows):
                for c in range(0, matrix.columns):
                        matrix[r][c] = getInput("m[%i][%i]: " % (r, c))

                print #new line after each row

# ----------------------------
# user inputs and calculations

s1 = getDimension("s1: ")
s2 = getDimension("s2: ")
s3 = getDimension("s3: ")

m1 = Matrix(s1, s2)
m2 = Matrix(s2, s3)

print "m1[%d][%d]:" % (m1.rows, m1.columns)
fillMatrix(m1)

print "m2[%d][%d]:" % (m2.rows, m2.columns)
fillMatrix(m2)

m3 = m1 * m2
writeMatrix(m3)
