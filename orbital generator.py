import csv


def rowByRow(file, inputDelimiter):
    """takes in a csv file, reads it in line by line, and creates a list of lists of all of the data"""
    output = []
    line_count = 0
    with open(file) as inputFile:
        lineReader = csv.reader(inputFile, delimiter = inputDelimiter)
        for row in lineReader:
            temp = []
            for column in row:
                temp.append(column)
            output.append(temp)
    return output

def orbitalGenerator (atomicNumber, orbitalChart):
    """takes in an atomic number with the orbital chart(1 col to orbital name, one column to number of electrons) and
    gives the string of orbitals"""
    electronCounter = 0
    orbitalindex = 0
    orbitalstring = ''
    diff = 0
    while electronCounter < int(atomicNumber):
        orbitalstring = orbitalstring + orbitalChart[orbitalindex][0]
        if int(atomicNumber) - int(electronCounter) > int(orbitalChart[orbitalindex][1]):
            orbitalstring = orbitalstring + orbitalChart[orbitalindex][1] + ' '
            electronCounter += int(orbitalChart[orbitalindex][1])
        else:
            diff = int(atomicNumber)- electronCounter
            orbitalstring = orbitalstring + str(diff) + ' '
            electronCounter += diff
        orbitalindex += 1
    return orbitalstring


# ask user for periodic element
elementNumber = input('what is the atomic number of your element?')


# generating table of elements
elements = rowByRow('SimplifiedPeriodicTableofElements.csv', ',')

# generating table of orbitals
orbitals = rowByRow('Orbitals.csv', ',')

print(elements[int(elementNumber)][1] + ' is ' +  orbitalGenerator(elementNumber, orbitals))


