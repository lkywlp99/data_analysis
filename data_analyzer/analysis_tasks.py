import pandas as pd
from .operation import Operation
from .registry import operation_registry

# data_analyzer/analysis_tasks.py

@operation_registry.register('sum_computating')
class SumComputating(Operation):
    def execute(self, data, **kwargs):
        column = kwargs.get('column')
        return pd.DataFrame({column: data[column].sum()})

@operation_registry.register('maximum_computating')
class MaximumComputating(Operation):
    def execute(self, data, **kwargs):
        column = kwargs.get('column')
        idx_max = data[column].idxmax()
        max_value = data.loc[idx_max, column]
        return pd.DataFrame({column: max_value, 'index': idx_max})

@operation_registry.register('minimum_computating')
class MinimumComputating(Operation):
    def execute(self, data, **kwargs):
        column = kwargs.get('column')
        idx_min = data[column].idxmin()
        min_value = data.loc[idx_min, column]
        return pd.DataFrame({column: min_value, 'index': idx_min})

@operation_registry.register('mean_computating')
class MeanComputating(Operation):
    def execute(self, data, **kwargs):
        column = kwargs.get('column')
        return pd.DataFrame({column: data[column].mean()})

@operation_registry.register('same_period_comparison')
class SamePeriodComparison(Operation):
    def execute(self, data, **kwargs):
        attributes = kwargs.get('attributes')
        date_ranges = kwargs.get('date_ranges')
        date_column = kwargs.get('key')
        
        # Debug: Print the parameters received
        print(f"Date ranges: {date_ranges}")
        print(f"Date column to filter on: {date_column}")
        print(f"Attributes to calculate sum: {attributes}")

        # Convert the date column to datetime format
        data[date_column] = pd.to_datetime(data[date_column], format='%Y%m%d')
        
        # Debug: Print the head of the dataframe after date conversion
        print("Data head after date conversion:")
        print(data.head())

        # Filter data for the first date range
        start_date_range1 = pd.to_datetime(date_ranges[0][0], format='%Y%m%d')
        end_date_range1 = pd.to_datetime(date_ranges[0][1], format='%Y%m%d')
        period1_data = data[(data[date_column] >= start_date_range1) & (data[date_column] <= end_date_range1)]
        
        # Filter data for the second date range
        start_date_range2 = pd.to_datetime(date_ranges[1][0], format='%Y%m%d')
        end_date_range2 = pd.to_datetime(date_ranges[1][1], format='%Y%m%d')
        period2_data = data[(data[date_column] >= start_date_range2) & (data[date_column] <= end_date_range2)]
        
        # Debug: Print the filtered data for both periods
        print("Period 1 filtered data:")
        print(period1_data)
        print("Period 2 filtered data:")
        print(period2_data)
        
        # Calculate the sum for both periods
        period1_sum = period1_data[attributes[0]].sum() if not period1_data.empty else 0
        period2_sum = period2_data[attributes[0]].sum() if not period2_data.empty else 0

        # Debug: Print the sums for both periods
        print(f"Period 1 sum of {attributes[0]}: {period1_sum}")
        print(f"Period 2 sum of {attributes[0]}: {period2_sum}")

        # Calculate the difference and the percentage change
        difference = period1_sum - period2_sum
        percentage_change = (difference / period2_sum) * 100 if period2_sum else float('inf') 

        # Debug: Print the final calculation results
        print(f"Difference: {difference}")
        print(f"Percentage change: {percentage_change}%")

        return pd.DataFrame({
            'period1_sum': [period1_sum],
            'period2_sum': [period2_sum],
            'difference': [difference],
            'percentage_change': [percentage_change]
        })