import csv


def parseCSV(path):
    file = open(path)
    reader = csv.reader(file)
    data = []
    attributes = []
    for index, row in enumerate(reader):
        row = list(map(lambda x: None if x == '' else x, row))
        if index == 0:
            for col in row:
                attributes.append((col, set()))
        else:
            data.append(row)
            for i, col in enumerate(row):
                attributes[i][1].add(col)
    attributes = list(map(lambda x: (x[0], list(x[1])), attributes))
    return data, attributes