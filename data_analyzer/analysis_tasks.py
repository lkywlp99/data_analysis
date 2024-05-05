from .abstract_operators import DataAnalysisTask

class SumComputating(DataAnalysisTask):
    def compute(self, data, attributes):
        return data[attributes[0]].sum()

class MaxComputating(DataAnalysisTask):
    def compute(self, data, attributes):
        idx_max = data[attributes[0]].idxmax()
        max_value = data[attributes[0]].loc[idx_max]
        return idx_max, max_value
