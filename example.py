import arff
from biemsearch import biem_search
from biem.biem import biem

data = arff.load(open('../SpeedDating1-filtered-nocommas-discrete.arff'))
results = biem_search(data['data'][:100], data['attributes'], 10, 2)
for (name, matches) in results[0]:
    print("{0}: {1}".format(name, (len(matches)/len(data['data']))))

biem()
