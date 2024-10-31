
-- This file creates tables and populates the tables from the csv files :
    
-- 1 Customer Table
CREATE TABLE Customer (
    panID character(10) PRIMARY KEY,
    first text,
    last text,
    gender varchar(6),
    job text,
    dob DATE
);

COPY Customer (panID, first, last, gender, job, dob)
FROM 'D:/study zone/prep_job/projects/Credit_Card_Fraud/project/CSVs & Scripts/Customer.csv'
DELIMITER ','
CSV HEADER;

-- 2 CC Table
CREATE TABLE CC (
    cc_num text PRIMARY KEY,
    panID character(10),
    FOREIGN KEY (panID) REFERENCES Customer(panID)
);

COPY CC (cc_num, panID)
FROM 'D:/study zone/prep_job/projects/Credit_Card_Fraud/project/CSVs & Scripts/CC.csv'
DELIMITER ','
CSV HEADER;

-- 3 Category Table
CREATE TABLE Category (
    category_id character(10) PRIMARY KEY,
    category_name text
);

COPY Category (category_id, category_name)
FROM 'D:\study zone\prep_job\projects\Credit_Card_Fraud\project\CSVs & Scripts\Category.csv'
DELIMITER ','
CSV HEADER;

-- 4 Merchant Table
CREATE TABLE Merchant (
    merchant_id character(10) PRIMARY KEY,
    merchant_name text
);

COPY Merchant (merchant_id, merchant_name)
FROM 'D:\study zone\prep_job\projects\Credit_Card_Fraud\project\CSVs & Scripts\Merchant.csv'
DELIMITER ','
CSV HEADER;

--5 Merchant_Category Table
CREATE TABLE Merchant_Category (
    id integer PRIMARY KEY,
    category_id character(10),
    merchant_id character(10)
);

COPY Merchant_Category (id,category_id, merchant_id)
FROM 'D:/study zone/prep_job/projects/Credit_Card_Fraud/project/CSVs & Scripts/Merchant_Category.csv'
DELIMITER ','
CSV HEADER;

--6 Transactions Tabale
CREATE TABLE Transactions (
    trans_num character(32) PRIMARY KEY,
    cc_num text,
    amount float(2),
    trans_date_time TIMESTAMP,
    merchant_id character(10),
    category_id character(10),
    fraud integer CHECK (fraud IN (0,1)),
    FOREIGN KEY (merchant_id) REFERENCES Merchant(merchant_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

COPY Transactions(trans_num,cc_num,amount,trans_date_time,merchant_id,category_id,fraud)
FROM 'D:\study zone\prep_job\projects\Credit_Card_Fraud\project\CSVs & Scripts\Transactions.csv'
DELIMITER ','
CSV HEADER;
