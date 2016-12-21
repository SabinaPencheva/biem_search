from .base import AbstractEvaluator


class ChisquaredEvaluator(AbstractEvaluator):
    def name(self):
        return "ChiSquared"

    def __init__(self, data, cutoff):
        super().__init__(data)
        self.total_matches = 0
        self.total_nonmatches = 0
        self.cutoff = cutoff
        for entry in data:
            if entry[-1] == 'clic':
                self.total_matches += 1
            else:
                self.total_nonmatches += 1

    def evaluate(self, subgroup):
        if len(subgroup[2]) / len(self.data) < self.cutoff:
            return 0
        matches_in_group = 0
        nonmatches_in_group = 0
        for index in subgroup[2]:
            if self.is_match(index):
                matches_in_group += 1
            else:
                nonmatches_in_group += 1
        denominator1 = self.total_matches + self.total_nonmatches
        numerator1 = (matches_in_group * self.total_nonmatches - self.total_matches * nonmatches_in_group) ** 2
        devision1 = numerator1 / denominator1
        denominator2 = self.total_matches * self.total_nonmatches * (matches_in_group + nonmatches_in_group) * (self.total_matches + self.total_nonmatches - matches_in_group - nonmatches_in_group)
        numerator2 = (self.total_nonmatches + self.total_matches) ** 2
        devision2 = numerator2 / denominator2
        return devision1 * devision2