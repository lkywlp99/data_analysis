# abstract_operators.py
from abc import ABC, abstractmethod
import pandas as pd

class DataTransformOperator(ABC):
    @abstractmethod
    def apply(self, data: pd.DataFrame, **kwargs) -> pd.DataFrame:
        pass

class DataAnalysisTask(ABC):
    @abstractmethod
    def compute(self, data: pd.DataFrame, **kwargs):
        pass
