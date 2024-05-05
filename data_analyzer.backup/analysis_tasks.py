from .abstract_operators import DataAnalysisTask
from .transform_operators import DateRange
class SumComputating(DataAnalysisTask):
    def compute(self, data, attributes):
        return data[attributes[0]].sum()

class MaxComputating(DataAnalysisTask):
    def compute(self, data, attributes):
        idx_max = data[attributes[0]].idxmax()
        max_value = data[attributes[0]].loc[idx_max]
        return idx_max, max_value
        
class SamePeriodComparison(DataAnalysisTask):
    def compute(self, data, attributes, transform_instructions):
        # 变换操作的实例化
        transform_operator = DateRange()
        
        # 获取时间段
        period1_range = transform_instructions[0]['date_range']['values']
        period2_range = transform_instructions[1]['date_range']['values']

        # 应用时间段变换并计算每个时间段的总销量
        period1_data = transform_operator.apply(data, key="统计日期", values=period1_range)
        period2_data = transform_operator.apply(data, key="统计日期", values=period2_range)

        period1_sales = period1_data[attributes[0]].sum()
        period2_sales = period2_data[attributes[0]].sum()

        sales_increase = period1_sales - period2_sales
        if period2_sales != 0:
            sales_percentage_increase = (sales_increase / period2_sales) * 100
        else:
            sales_percentage_increase = float('inf')  # 如果上上周销量为0，则增长百分比为无穷大
        
        return {"sales_increase": sales_increase, "sales_percentage_increase": sales_percentage_increase}