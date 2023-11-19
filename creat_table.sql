-- Main table
CREATE TABLE main_table (
    customer_code INT PRIMARY KEY,
    market_department VARCHAR(255),
    customer_manager VARCHAR(255),
    company_name VARCHAR(255),
    operator VARCHAR(255),
    level VARCHAR(255),
    terminal_hierarchy VARCHAR(255),
    is_sample_customer VARCHAR(255),
    data_collection_method VARCHAR(255),
    store_name VARCHAR(255),
    address VARCHAR(255),
    data_type VARCHAR(255),
    location_interval VARCHAR(255)
);

CREATE TABLE sub_table (
    customer_code INT PRIMARY KEY,
    data_score FLOAT,
    startup_days INT,
    effective_upload_ratio FLOAT,
    upload_ratio_penalty FLOAT,
    sales_days INT,
    average_sales_duration FLOAT,
    sales_duration_penalty FLOAT,
    inventory_accuracy FLOAT,
    inventory_count INT,
    inspection_accuracy FLOAT,
    inspection_count INT,
    inventory_penalty FLOAT,
    warning_count INT,
    warning_penalty FLOAT,
    inventory_sales_ratio FLOAT,
    inventory_sales_penalty FLOAT,
    negative_inventory FLOAT,
    negative_inventory_penalty FLOAT,
    manual_inventory_changes_count INT,
    manual_inventory_changes_penalty FLOAT,
    centralized_sales_count INT,
    centralized_sales_penalty FLOAT,
    delayed_upload_count INT,
    delayed_upload_penalty FLOAT,
    FOREIGN KEY (customer_code) REFERENCES main_table(customer_code)
);

CREATE TABLE test_excel (
    customer_code VARCHAR(255) PRIMARY KEY,
    customer_manager VARCHAR(255),
    company_name VARCHAR(255),
    data_score FLOAT
);