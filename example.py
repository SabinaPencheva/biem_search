import arff
from biemsearch import biem_search
from biem.biem import biem
from openpyxl import Workbook

total_matches = 0

# Weighted relative accuracy evaluator as prescribed in exercise 1a
def wracc_evaluator(filter, data):
    global total_matches
    if total_matches == 0:
        for entry in data:
            if entry[-1] == '1':
                total_matches += 1
    matches_in_group = 0
    for index in filter[1]:
        if data[index][-1] == '1':
            matches_in_group += 1
    # WRAcc(S, l = 1) =
    #       p(S and l = 1)              - (p(S)                       * P(l = 1)                 )
    return (matches_in_group/len(data)) - ((len(filter[1])/len(data)) * (total_matches/len(data)))


data = arff.load(open('../SpeedDating1-filtered-nocommas-discrete.arff'))
results = biem_search(data['data'], data['attributes'], 10, 2, evaluator=wracc_evaluator)

wb = Workbook()
ws = wb.active
ws['A1'] = "Name"
ws['B1'] = "WRAcc"
ws['C1'] = "Matches"
ws['D1'] = "Coverage"

for (name, matches) in results:
    wracc = wracc_evaluator((name, matches), data['data'])
    coverage = len(matches)/len(data['data'])

    print("{0}: WRAcc {1:.2f}%, size {2:.2f}% of full data set".format(name, wracc*100, coverage*100))
    ws.append([name, wracc, len(matches), coverage])

wb.save("wracc.xlsx")
biem()