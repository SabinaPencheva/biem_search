from .base import AbstractEvaluator

#1 - Non-matches in the subgroup / Non-matches in training set

class SpecificityEvaluator(AbstractEvaluator):
    def name(self):
        return "Specificity"

    def __init__(self, data):
        super().__init__(data)
        self.total_non_matches = 0
        for entry in data:
            if entry[-1] == '0':
                self.total_non_matches += 1

    def evaluate(self, subgroup):
        non_matches_in_group = 0
        for index in subgroup[1]:
            if not self.is_match(index):
                non_matches_in_group += 1
        return 1 - (non_matches_in_group / self.total_non_matches)