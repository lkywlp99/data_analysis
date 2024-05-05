from .abstract_operators import DataAnalysisTask, DataTransformOperator
from .transform_operators import TransformAdjacentPeriodComparison, TransformBetween
from .analysis_tasks import SumComputating
from .analysis_tasks import SumComputating, MaxComputating

class OperatorRegistry:
    def __init__(self):
        self.transform_operators = {}
        self.analysis_tasks = {}
    
    def register_transform(self, name: str, operator: DataTransformOperator):
        self.transform_operators[name] = operator
    
    def register_task(self, name: str, task: DataAnalysisTask):
        self.analysis_tasks[name] = task
    
    def get_transform(self, name: str) -> DataTransformOperator:
        return self.transform_operators.get(name, None)
    
    def get_task(self, name: str) -> DataAnalysisTask:
        return self.analysis_tasks.get(name, None)

# Create a global registry instance that can be imported and used across the package
registry = OperatorRegistry()
registry.register_transform('between', TransformBetween())
registry.register_transform('adjacent_period_comparison', TransformAdjacentPeriodComparison())
registry.register_task('sum_computating', SumComputating())
registry.register_task('maximum_computating', MaxComputating())