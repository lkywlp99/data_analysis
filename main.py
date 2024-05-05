from data_analyzer.data_analyzer import DataAnalyzer

def main():
    json_instructions = {
        "task": "maximum_computating",
        "attributes": ["成交件数"],
        "transform": [
            {
                "between": {
                    "key": "统计日期",
                    "values": ["20240401", "20240430"]
                }
            }
        ]
    }

    data_path = 'data/data.xls'

    analyzer = DataAnalyzer(data_path, json_instructions)
    idx_max, max_value = analyzer.execute()
    
    print(f"The best sales day in April was on {analyzer.data.loc[idx_max, '统计日期']} with {max_value} items sold.")
    

if __name__ == "__main__":
    main()