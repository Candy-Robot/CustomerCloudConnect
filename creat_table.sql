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

CREATE TABLE test_excel (
    customer_code VARCHAR(255) PRIMARY KEY,
    customer_manager VARCHAR(255),
    company_name VARCHAR(255),
    data_score FLOAT
);

CREATE TABLE sales_penalty_detail (
    customer_code VARCHAR(50) PRIMARY KEY COMMENT '客户代码',
    data_score FLOAT COMMENT '数采分',
    startup_days INT COMMENT '启动天数',
    effective_upload_ratio FLOAT COMMENT '有效上传比率',
    upload_ratio_penalty FLOAT COMMENT '有效上传比扣分',
    upload_ratio_penalty_time DATE COMMENT '有效上传比扣分时间',
    upload_ratio_recovery_time DATE COMMENT '有效上传比恢复时间',
    sales_days INT COMMENT '销售天数',
    average_sales_duration FLOAT COMMENT '平均销售时长',
    sales_duration_penalty FLOAT COMMENT '销售时长扣分',
    sales_duration_penalty_time DATE COMMENT '销售时长扣分时间',
    sales_duration_recovery_time DATE COMMENT '销售时长恢复时间',
    warning_count INT COMMENT '预警数量',
    warning_penalty FLOAT COMMENT '预警扣分',
    warning_penalty_time DATE COMMENT '预警扣分时间',
    warning_recovery_time DATE COMMENT '预警恢复时间',
    centralized_sales_count INT COMMENT '集中销售数量',
    centralized_sales_penalty FLOAT COMMENT '集中销售扣分',
    centralized_sales_penalty_time DATE COMMENT '集中销售扣分时间',
    centralized_sales_recovery_time DATE COMMENT '集中销售恢复时间',
    delayed_upload_count INT COMMENT '延迟上传数量',
    delayed_upload_penalty FLOAT COMMENT '延迟上传扣分',
    delayed_upload_penalty_time DATE COMMENT '延迟上传扣分时间',
    delayed_upload_recovery_time DATE COMMENT '延迟上传恢复时间'
);

CREATE TABLE inventory_penalty_detail (
    customer_code VARCHAR(50) PRIMARY KEY COMMENT '客户ID主键',
    inventory_accuracy FLOAT COMMENT '库存准确性',
    inventory_count INT COMMENT '盘库次数',
    inspection_accuracy FLOAT COMMENT '检查准确率',
    inspection_count INT COMMENT '检查次数',
    inventory_penalty FLOAT COMMENT '盘库扣分',
    inventory_penalty_time DATE COMMENT '盘库扣分时间',
    inventory_penalty_recovery_time DATE COMMENT '盘库扣分恢复时间',
    inventory_sales_ratio FLOAT COMMENT '存销比',
    inventory_sales_penalty FLOAT COMMENT '存销比扣分',
    inventory_sales_penalty_time DATE COMMENT '存销比扣分时间',
    inventory_sales_penalty_recovery_time DATE COMMENT '存销比扣分恢复时间',
    negative_inventory INT COMMENT '负库存',
    negative_inventory_penalty FLOAT COMMENT '负库存扣分',
    negative_inventory_penalty_time DATE COMMENT '负库存扣分时间',
    negative_inventory_penalty_recovery_time DATE COMMENT '负库存扣分恢复时间',
    manual_inventory_changes_count INT COMMENT '人为修改库存次数',
    manual_inventory_changes_penalty FLOAT COMMENT '人为修改库存扣分',
    manual_inventory_changes_penalty_time DATE COMMENT '人为修改库存扣分时间',
    manual_inventory_changes_penalty_recovery_time DATE COMMENT '人为修改库存扣分恢复时间'
);

CREATE TABLE data_score_and_upload_time (
    customer_code VARCHAR(50) PRIMARY KEY COMMENT '客户ID',
    data_score FLOAT COMMENT '数采分，表示客户在各个方面的绩效综合得分。',
    last_upload_time DATETIME COMMENT '最近上传时间。'
);


CREATE TABLE inventory_penalty_detail (
    customer_code VARCHAR(50) PRIMARY KEY,
    inventory_accuracy FLOAT,
    inventory_count INT,
    inspection_accuracy FLOAT,
    inspection_count INT,
    inventory_penalty FLOAT,
    inventory_penalty_time DATE,
    inventory_penalty_recovery_time DATE,
    inventory_sales_ratio FLOAT,
    inventory_sales_penalty FLOAT,
    inventory_sales_penalty_time DATE,
    inventory_sales_penalty_recovery_time DATE,
    negative_inventory INT,
    negative_inventory_penalty FLOAT,
    negative_inventory_penalty_time DATE,
    negative_inventory_penalty_recovery_time DATE,
    manual_inventory_changes_count INT,
    manual_inventory_changes_penalty FLOAT,
    manual_inventory_changes_penalty_time DATE,
    manual_inventory_changes_penalty_recovery_time DATE
);

CREATE TABLE sales_penalty_detail (
    customer_code VARCHAR(50) PRIMARY KEY,
    data_score FLOAT,
    startup_days INT,
    effective_upload_ratio FLOAT,
    upload_ratio_penalty FLOAT,
    upload_ratio_penalty_time DATE,
    upload_ratio_recovery_time DATE,
    sales_days INT,
    average_sales_duration FLOAT,
    sales_duration_penalty FLOAT,
    sales_duration_penalty_time DATE,
    sales_duration_recovery_time DATE,
    warning_count INT,
    warning_penalty FLOAT,
    warning_penalty_time DATE,
    warning_recovery_time DATE,
    centralized_sales_count INT,
    centralized_sales_penalty FLOAT,
    centralized_sales_penalty_time DATE,
    centralized_sales_recovery_time DATE,
    delayed_upload_count INT,
    delayed_upload_penalty FLOAT,
    delayed_upload_penalty_time DATE,
    delayed_upload_recovery_time DATE
);