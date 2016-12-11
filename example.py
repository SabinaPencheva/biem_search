import arff
from biemsearch import biem_search
from biem.biem import biem

data = arff.load(open('../SpeedDating1-filtered-nocommas-discrete.arff'))
results = biem_search(data['data'][:100], data['attributes'], 10, 2)
for (name, matches) in results[0]:
    total_matches = 0
    for entry in data['data']:
        if entry[-1] == "1":
            total_matches += 1
    print("{0}: {1}".format(name, (len(matches)/total_matches)))

biem()
