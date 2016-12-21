from .base import AbstractEvaluator


class WraccEvaluator(AbstractEvaluator):
    def name(self):
        return "WRAcc"

    def __init__(self, data):
        super().__init__(data)
        self.total_matches = 0
        self.total_nonmatches = 0
        for entry in data:
            if entry[-1] == "clic":
                self.total_matches += 1
            else:
                self.total_nonmatches += 1

    def evaluate(self, subgroup):
        if len(subgroup[2]) == 0:
            return 0
        matches_in_group = 0
        nonmatches_in_group = 0
        for index in subgroup[2]:
            if self.is_match(index):
                matches_in_group += 1
            else:
                nonmatches_in_group += 1
        p = matches_in_group
        n = nonmatches_in_group
        P = self.total_matches
        N = self.total_nonmatches
        # hwra' =
        return ((p+n)/(P+N)) * ((p / (p+n)) - (P / (P+N)))