import arff
from biemsearch import biem_search, default_eval
from biem.biem import biem

data = arff.load(open('../SpeedDating1-filtered-nocommas-discrete.arff'))
results = biem_search(data['data'], data['attributes'], 10, 1)
for (name, matches) in results:
    print("{0}: subgroup match correlation {1}, size {2} of full data set".format(name, default_eval((name, matches), data['data']), len(matches)/len(data['data'])))

biem()