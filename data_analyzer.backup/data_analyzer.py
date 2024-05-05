import pandas as pd
from .operator_registry import registry

class DataAnalyzer:
    def __init__(self, data_path, json_instructions):
        self.data = pd.read_excel(data_path)
        self.instructions = json_instructions

    def execute_transformations(self, data):
        transformations = self.instructions.get('transform', [])
        for transform in transformations:
            operation = list(transform.keys())[0]
            operator = registry.get_transform(operation)
            if operator is None:
                raise ValueError(f"Transform operation '{operation}' is not supported.")
            
            result_or_data = operator.apply(data, **transform[operation])
            if isinstance(result_or_data, dict):  # A dictionary indicates a final result.
                return result_or_data
            else:
                data = result_or_data
        return data
        
    def execute(self):
        # Execute transformations
        transformation_result = self.execute_transformations(self.data)

        # Check if a final result was already obtained from transformations
        if isinstance(transformation_result, dict):
            return transformation_result["result"]

        # Execute analysis task
        task_name = self.instructions.get('task')
        if task_name:
            task = registry.get_task(task_name)
            if task is None:
                raise ValueError(f"Analysis task '{task_name}' is not supported.")
            attributes = self.instructions.get('attributes')
            result = task.compute(transformation_result, attributes=attributes)
            return result
        else:
            raise ValueError("No analysis task specified in instructions.")