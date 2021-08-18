#! python 3
# Chapter 6 practise project

tableData = [
    ['Lily', 'Toto', 'Bruce', "Alphonse"],
    ['Charlie', 'Buddy', 'Wormz', 'Roo'],
    ['Justine', 'Theresa', 'Ruby', 'Henry']
]

def printTable(table):
    colWidth = [0] * len(tableData) # creates a list of 0s equal to the number of lists in tableData
    # This makes it so we can take the len of the longest item in each list and ammend the 0 to the correct #

    for y in range(len(table)):
        for x in table[y]:
            if colWidth[y] < len(x):
                colWidth[y] = len(x)

    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidth[y]), end = ' ')
        print()
        x += 1

printTable(tableData)

## SO this works great, but I don't think I fully understand how to get here without help from stackoverflow
# so I definitely need to come back to this later and see if I still have a hard time with it.
# https://stackoverflow.com/questions/34488115/automate-the-boring-stuff-chapter-6-table-printer-almost-done
