#!/usr/bin/env python3
# displays an organised table (that is right-justified) from a list of lists of strings

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def max_length(table):
    """list max length of strings"""
    colWidth = [0] * len(table)
    for i in range(len(table)):
        colWidth[i] = len(max(table[i], key=len)) + 1
    return colWidth

    """Less efficient version:"""
    # listMax = []
    # for j in range(len(table)):
    #     lengths = []
    #     for i in range(len(table[j])):
    #         lengths.append(len(table[j][i]))
    #     listMax.append(max(lengths))
    # return listMax


def newTable(table):
    """reorder lists"""
    newTable = []
    for i in range(len(table[0])):
        myListA = []
        for j in range(len(table)):
            myListA.append(table[j][i])
        newTable.append(myListA)
    return newTable


def main(table):
    colWidths = max_length(table)
    tableList = newTable(table)
    for i in range(len(tableList)):
        items = ""
        for j in range(len(tableList[i])):
            items += " " + tableList[i][j].rjust(colWidths[j])
        print(items)


if __name__ == "__main__":
    main(tableData)
