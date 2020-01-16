import randNumGen
import array2pt


rowsArray = []
colsArray = []

for i in range(20):

    num = randNumGen.RandGen()
    
    if i < 10:
        rowsArray.append(num)

    elif i >= 10:
        colsArray.append(num)

theArray = []


for r in rowsArray:
    tempArray = []

    for c in colsArray:
        actualSum = r + c

        while(True):
            # inputSum = int(input(str(r) + " + " + str(c) + " = "))
            inputSum = actualSum

            if inputSum == actualSum:
                tempArray.append(actualSum)
                break

            else:
                print("COME ON, MAN!")

    theArray.append(tempArray)


# for i in theArray:
#     print(i)


# Horizontal Sum
def ArrayAdder(array):

    i = 1
    actualSum = array[0]
    while(i < len(array)):

        tempSum = actualSum + array[i]

        while(True):
            # inputSum = int(input(str(actualSum) + " + " + str(array[i]) + " = "))
            inputSum = tempSum

            if inputSum == tempSum:
                break

            else:
                print("COME ON, MAN!")

        actualSum = tempSum

        i += 1


    return actualSum


print("===============================================================")
for array in theArray:
    horiSum = ArrayAdder(array)
    array.append(horiSum)


# for i in theArray:
    # print(i)


print("===============================================================")

bottomArray = ["TOTALS"]
for i in range(len(theArray)):

    VerticalArray = []
    for row in theArray:
        VerticalArray.append(row[i])

    veriSum = ArrayAdder(VerticalArray)
    bottomArray.append(veriSum)

bottomArray.append("++")
# print(bottomArray)



colsArray.insert(0, "++")
colsArray.append("TOTALS")
# print(colsArray)


for rows, sumsArray in zip(rowsArray, theArray):
    sumsArray.insert(0, rows)


theArray.insert(0, colsArray)
theArray.append(bottomArray)


# for i in theArray:
#     print(i)

array2pt.TheArray2PT(theArray)
        
