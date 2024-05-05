from data_analyzer.data_analyzer import DataAnalyzer

def main():
    # 修正后的构造指令对象
    json_instructions = {
        "data_source": "data/data.xls",
        "transformations": [
            # {
            #     "name": "date_range",
            #     "params": {
            #         "key": "统计日期",
            #         "start": "20240424",
            #         "end": "20240430"
            #     }
            # },
            # {
            #     "name": "date_range",
            #     "params": {
            #         "key": "统计日期",
            #         "start": "20240417",
            #         "end": "20240423"
            #     }
            # }
        ],
        "analysis": {
            "name": "same_period_comparison",
            "params": {
                "attributes": ["成交件数"],
                "key": "统计日期",  # 确保这里的名字匹配 analysis_tasks.py 中期待的那个
                "date_ranges": [
                    ["20240424", "20240430"],
                    ["20240417", "20240423"]
                ]
            }
        }
    }
    
    # 更新类实例化方式，仅传递 json_instructions
    analyzer = DataAnalyzer(json_instructions)
    result = analyzer.analyze()
    
    # 输出分析结果
    print(result)

if __name__ == "__main__":
    main()