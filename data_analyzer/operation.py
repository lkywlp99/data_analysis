from abc import ABC, abstractmethod
import pandas as pd

class Operation(ABC):
    @abstractmethod
    def execute(self, data: pd.DataFrame, **kwargs) -> pd.DataFrame:
        pass
