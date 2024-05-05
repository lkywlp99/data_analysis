import pandas as pd

class DataReader:
    @staticmethod
    def read_data(source, **kwargs):
        if source.endswith('.csv'):
            return pd.read_csv(source, **kwargs)
        elif source.endswith('.xlsx'):
            return pd.read_excel(source, **kwargs)
        elif source.endswith('.xls'):
            return pd.read_excel(source, **kwargs)
        elif source.endswith('.json'):
            return pd.read_json(source, **kwargs)
        else:
            raise ValueError('Unsupported data source format')
