from abc import ABC, abstractmethod


class AbstractEvaluator(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def name(self):
        raise NotImplemented()

    @abstractmethod
    def evaluate(self, subgroup):
        raise NotImplemented()

    def is_match(self, index):
        return self.data[index][-1] == 'clic'
