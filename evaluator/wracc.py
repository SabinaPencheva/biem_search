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
        matches_in_group = 0
        nonmatches_in_group = 0
        for index in subgroup[2]:
            if self.is_match(index):
                matches_in_group += 1
            else:
                nonmatches_in_group += 1
        # WRAcc(S, l = 1) =
        #       p(S and l = 1)               - (p(S)                        * P(l = 1)                       )
        len_data = len(self.data)
        #return (matches_in_group / len_data) - ((len(subgroup[1]) / len_data) * (self.total_matches / len_data))
        return (matches_in_group/self.total_matches) - (nonmatches_in_group / self.total_nonmatches)