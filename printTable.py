tableData = [['apples','banana', 'oranges','cherries'],
                ['Alice','Bob','Carol','David'],
                ['dogs','cats','moose','goose']]

def printTable():
    colWidth = [0] * len(tableData)
    # for j in range(0,5):
    for i in range(0,3):
        colWidth[i] = len(max(tableData[i],key=len))
    for j in range(0,4):
        print(tableData[0][j].rjust(colWidth[0]) + ' ' + tableData[1][j].rjust(colWidth[1]) + ' ' + tableData[2][j].rjust(colWidth[2]))
        # for i in range(0,3):
        #     print(tableData[i][j].rjust(colWidth[i]).rstrip('\n'))
printTable()
