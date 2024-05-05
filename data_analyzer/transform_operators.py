# data_analyzer/transform_operators.py

import pandas as pd
from .operation import Operation
from .registry import operation_registry

@operation_registry.register('greater')
class TransformGreater(Operation):
    def execute(self, data, **kwargs):
        column = kwargs.get('column')
        value = kwargs.get('value')
        return data[data[column] > value]

@operation_registry.register('less')
class TransformLess(Operation):
    def execute(self, data, **kwargs):
        column = kwargs.get('column')
        value = kwargs.get('value')
        return data[data[column] < value]

@operation_registry.register('between')
class TransformBetween(Operation):
    def execute(self, data, **kwargs):
        column = kwargs.get('column')
        start = pd.to_datetime(kwargs.get('start'))
        end = pd.to_datetime(kwargs.get('end'))
        return data[(data[column] >= start) & (data[column] <= end)]

@operation_registry.register('date_range')
class TransformDateRange(Operation):
    def execute(self, data, **kwargs):
        print("Original data head:\n", data.head())  # 打印原始数据
        # 获得指定列，并确保其转换为日期时间类型
        key = kwargs.get('key')
        data[key] = pd.to_datetime(data[key], format='%Y%m%d')
        
        # 起始和结束的日期字符串被转换为 pandas Timestamp
        start_date = pd.to_datetime(kwargs.get('start'), format='%Y%m%d')
        end_date = pd.to_datetime(kwargs.get('end'), format='%Y%m%d')

        # 进行筛选
        condition = (data[key] >= start_date) & (data[key] <= end_date)
        filtered_data = data[condition]
        print("Filtered data head:\n", filtered_data.head())
        return filtered_data