| 市场部 | 客户经理 | 企业名称 | 经营者 | 客户编码 | 档位 | 终端层级 | 是否样本户 | 数采方式 | 店招名称 | 地址 | 数采类型 | 所在区间 | 数采分 | 开机天数 | 有效上传比例 | 有效上传比例扣分 | 销售天数 | 日均销售时长 | 销售时长扣分 | 盘库准确率 | 盘库次数 | 检查准确率 | 检查次数 | 盘库扣分 | 预警次数 | 预警扣分 | 存销比 | 存销比扣分值 | 负库存 | 负库存扣分项 | 人为修改库存次数 | 人为修改库存次数扣分 | 集中销售次数 | 集中销售次数扣分 | 延迟上传次数 | 延迟上传次数扣分 |
| ------ | -------- | -------- | ------ | -------- | ---- | -------- | ---------- | -------- | -------- | ---- | -------- | -------- | ------ | -------- | ------------ | ---------------- | -------- | ------------ | ------------ | ---------- | -------- | ---------- | -------- | -------- | -------- | -------- | ------ | ------------ | ------ | ------------ | ---------------- | -------------------- | ------------ | ---------------- | ------------ | ---------------- |
|        |          |          |        |          |      |          |            |          |          |      |          |          |        |          |              |                  |          |              |              |            |          |            |          |          |          |          |        |              |        |              |                  |                      |              |                  |              |                  |

市场部	客户经理	企业名称	经营者	客户编码	档位	终端层级	是否样本户	数采方式	店招名称	地址	数采类型	所在区间	数采分	开机天数	有效上传比例	有效上传比例扣分	销售天数	日均销售时长	销售时长扣分	盘库准确率	盘库次数	检查准确率	检查次数	盘库扣分	预警次数	预警扣分	存销比	存销比扣分值	负库存	负库存扣分项	人为修改库存次数	人为修改库存次数扣分	集中销售次数	集中销售次数扣分	延迟上传次数	延迟上传次数扣分



```
pythonCopy code
class CustomerInformation(db.Model):
    __tablename__ = 'customer_information'

    customer_code = db.Column(db.String(50), primary_key=True)  # 客户唯一标识符，主键
    market_department = db.Column(db.String(50))  # 客户的市场部
    customer_manager = db.Column(db.String(50))  # 客户经理
    company_name = db.Column(db.String(100))  # 客户公司的名称
    operator = db.Column(db.String(50))  # 经营者
    level = db.Column(db.String(20))  # 客户档位
    terminal_hierarchy = db.Column(db.String(50))  # 客户的终端层级
    is_sample_customer = db.Column(db.String(20))  # 表示客户是否为样本客户
    data_collection_method = db.Column(db.String(50))  # 数据采集方法
    store_name = db.Column(db.String(100))  # 客户店铺名称
    address = db.Column(db.String(255))  # 客户地址
    data_type = db.Column(db.String(50))  # 数采类型
    location_interval = db.Column(db.Integer)  # 数采户所在区间
    
   在excel表里面的字段为：
    市场部	客户经理	企业名称	经营者	客户编码	档位	终端层级	是否样本户	数采方式	店招名称	地址	数采类型	所在区间	数采分	开机天数	有效上传比例	有效上传比例扣分	销售天数	日均销售时长	销售时长扣分	盘库准确率	盘库次数	检查准确率	检查次数	盘库扣分	预警次数	预警扣分	存销比	存销比扣分值	负库存	负库存扣分项	人为修改库存次数	人为修改库存次数扣分	集中销售次数	集中销售次数扣分	延迟上传次数	延迟上传次数扣分
    
    请将这些字段填充进下面的代码中：
                # 将数据存储到数据库
                for index, row in df.iterrows():
                    newRecordCount += 1
                    excel_data = test_excel(
                        customer_code = row.to_dict()['客户编码'], 
                        # market_department =  row.to_dict()['市场部'],
                        customer_manager = row.to_dict()['客户经理'],
                        company_name = row.to_dict()['企业名称'],
                        data_score = row.to_dict()['数采分'],
                        # 最近上传时间
                        last_upload_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        # 第一次上传数据时，最近修改时间和恢复时间为空
                        # last_modified_time =      # 最近修改时间
                        # restore_time = db.Column(db.DateTime)   # 恢复时间
                    )   
                    db.session.add(excel_data)
```