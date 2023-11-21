# inventory_penalty_detail（数采分库存部分）

## 目录

1. 表的用途
2. mysql表文档
3. [sql建表语句]()

## MySQL表文档：

### 表名：inventory_penalty_detail

| 字段名                           | 数据类型    | 描述                                                   |
| -------------------------------- | ----------- | ------------------------------------------------------ |
| customer_code                    | VARCHAR(50) | 主键，表示客户ID。                                     |
| inventory_accuracy               | FLOAT       | 库存准确性，表示客户的库存准确性评分。实时变动。       |
| inventory_count                  | INT         | 盘库次数，表示库存中的物品数量。                       |
| inspection_accuracy              | FLOAT       | 检查准确率，表示客户的检查准确性评分。                 |
| inspection_count                 | INT         | 检查次数，表示检查的数量。                             |
| inventory_penalty                | FLOAT       | 盘库扣分，表示由于库存准确性低而施加的惩罚。           |
| inventory_sales_ratio            | FLOAT       | 库存销售比率，表示库存与销售的比率。实时变动。         |
| inventory_sales_penalty          | FLOAT       | 库存销售比率惩罚，表示由于库存销售比率低而施加的惩罚。 |
| negative_inventory               | INT         | 负库存，表示库存中负库存的物品数量。**实时变动**。     |
| negative_inventory_penalty       | FLOAT       | 负库存扣分，表示由于负库存而施加的惩罚。               |
| manual_inventory_changes_count   | INT         | 人为修改库存次数，表示手动进行的库存更改次数。         |
| manual_inventory_changes_penalty | FLOAT       | 人为修改库存扣分，表示由于手动库存更改产生的扣分。     |

## sql建表语句

~~~sql
CREATE TABLE inventory_penalty_detail (
    customer_id VARCHAR(50) PRIMARY KEY COMMENT '客户ID，主键',
    inventory_accuracy FLOAT COMMENT '库存准确性',
    inventory_count INT COMMENT '盘库次数',
    inspection_accuracy FLOAT COMMENT '检查准确率',
    inspection_count INT COMMENT '检查次数',
    inventory_penalty FLOAT COMMENT '盘库扣分',
    inventory_sales_ratio FLOAT COMMENT '存销比',
    inventory_sales_penalty FLOAT COMMENT '存销比扣分',
    negative_inventory INT COMMENT '负库存',
    negative_inventory_penalty FLOAT COMMENT '负库存扣分',
    manual_inventory_changes_count INT COMMENT '人为修改库存次数',
    manual_inventory_changes_penalty FLOAT COMMENT '人为修改库存扣分'
);
~~~

