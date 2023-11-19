# import xlrd
# 处理pandas的函数
import sys
sys.path.append('../')
import pandas as pd
from models import ExcelData


def load_excel(path):
    df = pd.read_excel(path)
    print(df.head())
    for index, row in df.iterrows():
        excel_data = ExcelData(
            customer_code = row.to_dict()['客户编码'], 
            market_department =  row.to_dict()['市场部'],
            customer_manager = row.to_dict()['客户经理'],
            company_name = row.to_dict()['企业名称']
            )
        print(excel_data)
        # db.session.add(excel_data)

if __name__ == '__main__':
    load_excel('uploads/1111.xlsx')
