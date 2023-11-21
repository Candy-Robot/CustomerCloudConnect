-- Main table
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

CREATE TABLE inventory_penalty_detail (
    customer_code VARCHAR(50) PRIMARY KEY COMMENT '客户ID主键',
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


CREATE TABLE test_excel (
    customer_code VARCHAR(255) PRIMARY KEY,
    customer_manager VARCHAR(255),
    company_name VARCHAR(255),
    data_score FLOAT
);