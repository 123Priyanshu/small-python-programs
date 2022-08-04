def printTableRow(inputNum, rowNum):
    print(inputNum, 'x', rowNum, '=', inputNum*rowNum)
# Should print something like below if the inputNum is 2
# we get 2 from the inputNum
# we get 1 from rowNum
# 2 on the right hand side of = is the product of inputNum and rowNum


def printTable(inputNum):
    a = inputNum
    for a in range(0, 11):
        print(inputNum, 'x', a, '=', inputNum*a)

    # Should print something like below if the inputNum is 2
    # 2 X 1 = 2
    # 2 X 2 = 4
    # 2 X 10 = 20
printTableRow(5, 6)
printTable(2)

