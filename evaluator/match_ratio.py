from .base import AbstractEvaluator


class MatchRatioEvaluator(AbstractEvaluator):
    def name(self):
        return "Match ratio"

    def __init__(self, data, cutoff):
        super().__init__(data)
        self.cutoff = cutoff

    def evaluate(self, subgroup):
        if len(subgroup[1]) / len(self.data) < self.cutoff:
            return 0
        score = 0
        for index in subgroup[1]:
            if self.is_match(index):
                score += 1
        return score / len(subgroup[1])
