import arff # This should be liac-arff!
from biemsearch import biem_search
from biem.biem import biem
from openpyxl import Workbook

from evaluator.match_ratio import MatchRatioEvaluator
from evaluator.wracc import WraccEvaluator

# First check that we have the right arff library
if arff.__author__ != 'Renato de Pontes Pereira':
    raise ImportError('You may have imported the wrong arff parsing library, please download liac-arff')


def run_evaluator(evaluator, data, attributes):
    results = biem_search(data, attributes, 10, 2, evaluator)

    wb = Workbook()
    ws = wb.active
    ws['A1'] = "Name"
    ws['B1'] = evaluator.name()
    ws['C1'] = "Matches"
    ws['D1'] = "Coverage"

    for (name, matches) in results:
        wracc = evaluator.evaluate((name, matches))
        coverage = len(matches)/len(data)

        print("{0}: {1} {2:.2f}%, size {3:.2f}% of full data set".format(name, evaluator.name(), wracc*100, coverage*100))
        ws.append([name, wracc, len(matches), coverage])

    wb.save("{0}.xlsx".format(evaluator.name()))
    biem()

dataset = arff.load(open('../SpeedDating1-filtered-nocommas-discrete.arff'))
data = dataset['data']
attributes = dataset['attributes']

match_ratio = MatchRatioEvaluator(data, 0.1)
wracc = WraccEvaluator(data)

evaluators = [match_ratio, wracc]
for evaluator in evaluators:
    run_evaluator(evaluator, data, attributes)