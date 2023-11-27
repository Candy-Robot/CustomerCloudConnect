# sales_penalty_detail（数采分销售部分明细）

## 目录

1. 表的用途
2. [字段说明]()
3. [sql建表语句]()

## 1. 表的用途

`sub_table` 是一个存储与客户（在 `main_table` 中表示）相关的各项评分和惩罚数据的表。这些数据用于评估客户在不同方面的绩效，例如销售、库存准确性、上传延迟等。

## 2. MySQL表文档：

#### 表名：sales_penalty_detail

| 字段名                    | 数据类型    | 描述                                               |
| ------------------------- | ----------- | -------------------------------------------------- |
| customer_code             | VARCHAR(50) | 主键，客户代码，与 `main_table` 中的客户代码关联。 |
| data_score                | FLOAT       | 数采分，表示客户在各个方面的绩效综合得分。         |
| startup_days              | INT         | 启动天数，表示客户的业务启动时间。                 |
| effective_upload_ratio    | FLOAT       | 有效上传比率，表示有效数据上传的比率。             |
| upload_ratio_penalty      | FLOAT       | 有效上传比扣分，表示由于上传比率低而施加的惩罚。   |
| sales_days                | INT         | 销售天数，表示客户的销售活动天数。                 |
| average_sales_duration    | FLOAT       | 平均销售时长，表示客户的平均销售活动持续时间。     |
| sales_duration_penalty    | FLOAT       | 销售时长扣分，表示由于销售时长低而施加的惩罚。     |
| warning_count             | INT         | 预警数量，表示销售周环比。                         |
| warning_penalty           | FLOAT       | 预警扣分，表示由于收到警告而施加的惩罚。           |
| centralized_sales_count   | INT         | 集中销售数量，表示通过中央销售的物品数量。         |
| centralized_sales_penalty | FLOAT       | 集中销售扣分，表示由于集中销售而施加的惩罚。       |
| delayed_upload_count      | INT         | 延迟上传数量，表示数据上传延迟的次数。             |
| delayed_upload_penalty    | FLOAT       | 延迟上传扣分，表示由于延迟上传而施加的惩罚。       |

## 3. sql建表语句

~~~sql
CREATE TABLE sales_penalty_detail (
    customer_code VARCHAR(50) PRIMARY KEY COMMENT '客户代码',
    data_score FLOAT COMMENT '数采分',
    startup_days INT COMMENT '启动天数',
    effective_upload_ratio FLOAT COMMENT '有效上传比例',
    upload_ratio_penalty FLOAT COMMENT '有效上传比例扣分',
    sales_days INT COMMENT '销售天数',
    average_sales_duration FLOAT COMMENT '日均销售时长',
    sales_duration_penalty FLOAT COMMENT '销售时长扣分',
    warning_count INT COMMENT '预警次数',
    warning_penalty FLOAT COMMENT '预警扣分',
    centralized_sales_count INT COMMENT '集中销售次数',
    centralized_sales_penalty FLOAT COMMENT '集中销售次数扣分',
    delayed_upload_count INT COMMENT '延迟上传次数',
    delayed_upload_penalty FLOAT COMMENT '延迟上传次数扣分',
    FOREIGN KEY (customer_code) REFERENCES customer_information(customer_code)
);
~~~





