# data_analyzer/data_analyzer.py

from .registry import operation_registry
from .data_reader import DataReader

class DataAnalyzer:
    def __init__(self, json_instructions):
        # 根据数据源路径载入数据
        self.data = DataReader.read_data(json_instructions["data_source"])
        # 存储转换和分析指令
        self.transformations = json_instructions.get("transformations", [])
        self.analysis = json_instructions.get("analysis", None)
    
    def analyze(self):
        # 遍历指令中的每一步转换
        for trans in self.transformations:
            # 获取转换操作的实例
            transform_operation = operation_registry.get_operation(trans["name"])
            # 对数据执行转换操作
            self.data = transform_operation.execute(self.data, **trans["params"])
        
        # 如果有分析任务，则逐一执行
        if self.analysis:
            # 获取分析任务的实例
            analysis_operation = operation_registry.get_operation(self.analysis["name"])
            # 对数据执行分析操作
            result = analysis_operation.execute(self.data, **self.analysis["params"])
            return result

        # 如果没有分析任务，则返回经过转换后的数据
        return self.data