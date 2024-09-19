use frr_dw;
CREATE TABLE Dim_State (
    state_id INT PRIMARY KEY AUTO_INCREMENT,
    state_name VARCHAR(255) NOT NULL
);
CREATE TABLE Dim_Industry (
    industry_id INT PRIMARY KEY AUTO_INCREMENT,
    industry_name VARCHAR(255) NOT NULL
);
CREATE TABLE Dim_Date (
    date_id INT PRIMARY KEY AUTO_INCREMENT,
    year INT NOT NULL,
    quarter INT NOT NULL,
    month INT NOT NULL,
    day INT NOT NULL
);
CREATE TABLE Dim_Company (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(255) NOT NULL,
    industry_id INT NOT NULL,
    state_id INT NOT NULL,
    company_status VARCHAR(50),     
    date_founded DATE,
    size VARCHAR(50),                
    age INT,
    
    FOREIGN KEY (industry_id) REFERENCES Dim_Industry(industry_id),
    FOREIGN KEY (state_id) REFERENCES Dim_State(state_id)
);

CREATE TABLE Fact_Financial_Performance (
    performance_id INT PRIMARY KEY AUTO_INCREMENT,
    company_id INT NOT NULL,
    date_id INT NOT NULL,
    total_assets DECIMAL(18,2),
    current_assets DECIMAL(18,2),
    total_liabilities DECIMAL(18,2),
    net_sales DECIMAL(18,2),
    gross_profit DECIMAL(18,2),
    total_operating_expenses DECIMAL(18,2),
    depreciation_and_amortization DECIMAL(18,2),
    ebit DECIMAL(18,2),
    ebitda DECIMAL(18,2),
    net_income DECIMAL(18,2),
    market_value DECIMAL(18,2),
    retained_earnings DECIMAL(18,2),
    total_revenue DECIMAL(18,2),
    cost_of_goods_sold DECIMAL(18,2),  
    inventory DECIMAL(18,2),            
    total_receivables DECIMAL(18,2),    
    total_long_term_debt DECIMAL(18,2), 
    total_current_liabilities DECIMAL(18,2), 

    -- Derived Metrics (KPIs)
    current_ratio DECIMAL(10,2),
    quick_ratio DECIMAL(10,2),
    debt_to_equity_ratio DECIMAL(10,2),
    gross_margin DECIMAL(10,2),
    operating_margin DECIMAL(10,2),
    ebitda_margin DECIMAL(10,2),
    net_profit_margin DECIMAL(10,2),
    return_on_assets DECIMAL(10,2),
    return_on_equity DECIMAL(10,2),
    price_to_earnings DECIMAL(10,2),
    price_to_sales DECIMAL(10,2),
    revenue_growth DECIMAL(10,2),
    profit_growth DECIMAL(10,2),
    equity_multiplier DECIMAL(10,2),
    retention_ratio DECIMAL(10,2),

    -- Foreign Keys
    FOREIGN KEY (company_id) REFERENCES Dim_Company(company_id),
    FOREIGN KEY (date_id) REFERENCES Dim_Date(date_id)
);

