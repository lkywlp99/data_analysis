from .abstract_operators import DataTransformOperator
import numpy as np

class TransformBetween(DataTransformOperator):
    def apply(self, data, key, values):
        return data[(data[key] >= np.min(values)) & (data[key] <= np.max(values))]

class TransformAdjacentPeriodComparison(DataTransformOperator):
    def apply(self, data, key, values, attributes):
        period1_values, period2_values = values
        attribute_name = attributes[0]

        period1_data = data[(data[key] >= period1_values[0]) & (data[key] <= period1_values[1])]
        period2_data = data[(data[key] >= period2_values[0]) & (data[key] <= period2_values[1])]
        
        period1_sum = period1_data[attribute_name].sum()
        period2_sum = period2_data[attribute_name].sum()
        
        # Returning a dictionary to indicate that this is a final result, not a DataFrame.
        return {"result": period2_sum - period1_sum}

from pandas import to_datetime

class TransformBetween(DataTransformOperator):
    def apply(self, data, key, values):
        # 将值转换为日期类型进行比较
        min_date = to_datetime(values[0], format='%Y%m%d')
        max_date = to_datetime(values[1], format='%Y%m%d')
        data[key] = to_datetime(data[key], format='%Y%m%d')
        return data[(data[key] >= min_date) & (data[key] <= max_date)]

class DateRange(DataTransformOperator):
    def apply(self, data, key, values):
        start_date = to_datetime(values[0], format='%Y%m%d')
        end_date = to_datetime(values[1], format='%Y%m%d')
        # 使用正确的方式赋值，避免SettingWithCopyWarning
        data.loc[:, key] = to_datetime(data[key], format='%Y%m%d')
        return data.loc[(data[key] >= start_date) & (data[key] <= end_date)]

@operation_registry.register('date_range')
class TransformDateRange(Operation):
    def execute(self, data, key, values):
        start_date, end_date = values
        data[key] = pd.to_datetime(data[key], format='%Y%m%d')
        return data[(data[key] >= start_date) & (data[key] <= end_date)]