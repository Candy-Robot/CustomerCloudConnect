# customer_info（客户信息）

## 表目的

`main_table` 旨在作为数据库中存储客户基本信息的主要表格。该表包含客户代码、市场部门、客户经理、公司名称、运营商、客户级别、终端层级等关键属性的详细信息。

### MySQL表文档：

#### 表名：customer_information

| 字段名                 | 数据类型     | 描述                         |
| ---------------------- | ------------ | ---------------------------- |
| customer_code          | VARCHAR(50)  | 主键，每个客户的唯一标识符。 |
| market_department      | VARCHAR(50)  | 客户的市场部                 |
| customer_manager       | VARCHAR(50)  | 客户经理。                   |
| company_name           | VARCHAR(100) | 客户公司名称。               |
| operator               | VARCHAR(50)  | 经营者                       |
| level                  | VARCHAR(20)  | 客户档位。                   |
| terminal_hierarchy     | VARCHAR(50)  | 客户的终端层级               |
| is_sample_customer     | VARCHAR(20)  | 表示客户是否为样本客户       |
| data_collection_method | VARCHAR(50)  | 数据采集方法                 |
| store_name             | VARCHAR(100) | 客户店铺名称                 |
| address                | VARCHAR(255) | 客户地址                     |
| data_type              | VARCHAR(50)  | 数采类型                     |
| location_interval      | INT          | 数采户所在区间               |

## sql语句

~~~sql
CREATE TABLE customer_information (
    customer_code VARCHAR(50) PRIMARY KEY COMMENT '客户唯一标识符，主键',
    market_department VARCHAR(50) COMMENT '客户的市场部',
    customer_manager VARCHAR(50) COMMENT '客户经理',
    company_name VARCHAR(100) COMMENT '客户公司的名称',
    operator VARCHAR(50) COMMENT '经营者',
    level VARCHAR(20) COMMENT '客户档位',
    terminal_hierarchy VARCHAR(50) COMMENT '客户的终端层级',
    is_sample_customer VARCHAR(20) COMMENT '表示客户是否为样本客户',
    data_collection_method VARCHAR(50) COMMENT '数据采集方法',
    store_name VARCHAR(100) COMMENT '客户店铺名称',
    address VARCHAR(255) COMMENT '客户地址',
    data_type VARCHAR(50) COMMENT '数采类型',
    location_interval INT COMMENT '数采户所在区间'
);
~~~

