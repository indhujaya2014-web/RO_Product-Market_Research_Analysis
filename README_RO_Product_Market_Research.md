# 💧RO Product & Market Research Analysis – India

## Project Overview

**RO Product & Market Research Analysis** is a data analytics and market intelligence project focused on industrial and commercial Reverse Osmosis (RO) products available in India.

The project combines publicly available product research with **Python, Pandas, NumPy, Streamlit, Excel, and Power BI** to research products, compare pricing and capacity, analyze manufacturers/suppliers, and identify potential market opportunities.

### Objectives

- Identify common RO capacities in the Indian market.
- Analyze price variation by capacity.
- Compare price per LPH.
- Compare manufacturers and suppliers.
- Analyze disclosed technical specifications.
- Identify potential Indian OEM/manufacturing candidates.
- Identify market gaps and possible opportunities.
- Present findings through an interactive Streamlit dashboard and Power BI dashboard.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and aggregation |
| NumPy | Numerical operations and capacity bands |
| Streamlit | Interactive dashboard |
| Excel | Research and analytical workbook |
| Power BI | Business intelligence dashboard |
| DAX | Power BI calculations |
| Git/GitHub | Version control |

---

## Dataset

The research dataset contains **20 publicly listed industrial/commercial RO products**.

Key fields:

| Field | Description |
|---|---|
| Product/Model | Product or model name |
| Manufacturer/Supplier | Company or supplier |
| RO Capacity (LPH) | Rated capacity |
| Price (INR) | Publicly listed indicative price |
| Purification Stages | Treatment stages where disclosed |
| RO Membrane Specification | Membrane details |
| Pump Specification | Pump details |
| Power Supply | Electrical requirement |
| Power Consumption | Published power requirement |
| Storage Capacity | Storage/tank capacity |
| Warranty | Published warranty |
| Main Application | Target use case |
| Location | Supplier/manufacturer location |
| Supplier Type | Manufacturer, supplier, trader, etc. |
| Source URL | Original public source |

---

## Project Files

```text
RO-Product-Market-Research/
│
├── RO_Product_Market_Research_Clean.csv
├── RO_Product_Market_Research_India.xlsx
├── ro_market_analysis.py
├── RO_Product_Market_Research_Report.docx
├── RO_Product_Market_Research_PowerBI.zip
├── README_RO_Product_Market_Research.md
│
└── ro_analysis_outputs/
    ├── capacity_summary.csv
    ├── manufacturer_summary.csv
    └── ro_research_analysis_ready.csv
```

---

# 🚀 Streamlit Interactive Dashboard

The main application is:

```text
ro_market_analysis.py
```

Run it with:

```bash
streamlit run ro_market_analysis.py
```

The dashboard title is:

> **💧 Indian Commercial & Industrial RO Market Research Analysis**

The application provides an interactive business intelligence interface for evaluating product specifications, pricing trends, capacity distribution, and manufacturer positioning.

---

## Methodology

### Research

Products were collected from publicly available manufacturer, supplier, and B2B marketplace listings.

### Data Cleaning

The Python workflow:

- Converts capacity and price to numeric values.
- Standardizes missing specifications as `Not disclosed`.
- Calculates price per LPH.
- Creates capacity bands.
- Creates manufacturer summaries.
- Calculates correlations.
- Calculates specification completeness.

### Price per LPH

```text
Price per LPH = Product Price / RO Capacity
```

This allows products with different capacities to be compared on a normalized basis.

---

## Key Findings

### Most Common Capacities

| Capacity | Products |
|---:|---:|
| 500 LPH | 6 |
| 1000 LPH | 4 |
| 250 LPH | 3 |
| 2000 LPH | 3 |
| 200 LPH | 1 |
| 3000 LPH | 1 |
| 5000 LPH | 1 |
| 6000 LPH | 1 |

The **500 LPH segment** is the most represented in this sample.

### Capacity and Price

The observed capacity-price correlation is approximately:

```text
0.85
```

This indicates a strong positive relationship within the researched sample: higher-capacity systems generally have higher absolute listed prices.

### Price per LPH

Price per LPH generally decreases as capacity increases in the sample, suggesting potential economies of scale.

However, price should not be evaluated using capacity alone because membrane, pump, material, pretreatment, automation, installation, warranty, and other configuration factors can materially affect cost.

---

## Capacity-Based Price Analysis

| Capacity Segment | Products | Average Listed Price |
|---|---:|---:|
| ≤500 LPH | 10 | ₹96,700 |
| 501–1,000 LPH | 4 | ₹260,000 |
| 1,001–2,000 LPH | 3 | ₹383,333 |
| 2,001–5,000 LPH | 2 | ₹562,500 |
| 5,001–10,000 LPH | 1 | ₹1,100,000 |

These are **publicly listed prices from the research sample**, not official industry averages.

---

# Power BI Dashboard

## Dashboard Title

**INDIA RO PRODUCT & MARKET INTELLIGENCE**

### Subtitle

*Industrial & Commercial Reverse Osmosis Product Benchmark | Publicly Listed Market Sample*

## Page 1 – Market Overview

### KPI Cards

- Total Products
- Total Manufacturers/Suppliers
- Average Price
- Average Capacity
- Maximum Capacity

### Visuals

1. **Products by Capacity Band** – clustered column chart.
2. **Average Price by Capacity Band** – column chart.
3. **Price vs Capacity** – scatter plot.
4. **Product Mix by Capacity Band** – donut chart.

Recommended slicers:

- Capacity Band
- Supplier Type
- Location
- Price Segment
- Main Application

## Page 2 – Manufacturer & Competitor Analysis

Recommended visuals:

- Average Price by Manufacturer/Supplier
- Maximum Capacity by Supplier
- Supplier Capacity vs Price
- Supplier Type Mix
- Manufacturer comparison matrix

Matrix fields:

```text
Manufacturer/Supplier
Product Count
Maximum Capacity
Average Price
Average Price/LPH
Supplier Type
Location
```

## Page 3 – Product & Specification Analysis

Recommended visuals:

- Main Application treemap
- Specification Completeness by Supplier
- Product comparison table
- Source URL table

---

# Important DAX

## Total Products

```DAX
Total Products =
DISTINCTCOUNT('RO_Products'[Product/Model])
```

## Total Suppliers

```DAX
Total Suppliers =
DISTINCTCOUNT('RO_Products'[Manufacturer/Supplier])
```

## Average Price

```DAX
Average Price =
AVERAGE('RO_Products'[Price (INR)])
```

## Average Capacity

```DAX
Average Capacity =
AVERAGE('RO_Products'[RO Capacity (LPH)])
```

## Average Price per LPH

```DAX
Average Price per LPH =
AVERAGE('RO_Products'[Price per LPH (INR)])
```

## Capacity Band

```DAX
Capacity Band =
SWITCH(
    TRUE(),
    'RO_Products'[RO Capacity (LPH)] <= 500, "01 - ≤500 LPH",
    'RO_Products'[RO Capacity (LPH)] <= 1000, "02 - 501–1,000 LPH",
    'RO_Products'[RO Capacity (LPH)] <= 2000, "03 - 1,001–2,000 LPH",
    'RO_Products'[RO Capacity (LPH)] <= 5000, "04 - 2,001–5,000 LPH",
    'RO_Products'[RO Capacity (LPH)] <= 10000, "05 - 5,001–10,000 LPH",
    "06 - >10,000 LPH"
)
```

---

# Potential OEM / Manufacturing Candidates

Companies identified for further investigation include:

- Vinayaga Engineering
- KG & Sons
- RRR Enviro Systems
- PR Water Industries
- Innovative Engineering
- Riviera Solutions
- Ultra Watech Systems
- Asian Aqua Park
- Canadian Crystalline
- Royal Aqua Plus

These should be treated as **potential research candidates**, not confirmed OEM partners. Manufacturing capability, OEM/private-label capability, MOQ, certifications, service network, warranty, and commercial terms should be verified directly.

---

# Market Opportunities

The research suggests several areas for further investigation:

### 1. Mid-Capacity Systems

The sample is concentrated around 500–1,000 LPH systems. Modular and standardized systems in this range could be investigated.

### 2. Specification Transparency

Many online listings do not disclose complete membrane, pump, power, warranty, or pretreatment information.

A more transparent product offering could clearly publish:

- Membrane brand/model
- Pump brand/model
- Recovery percentage
- Feed-water specification
- TDS range
- Power consumption
- Pretreatment
- Warranty
- Service interval
- Replacement costs

### 3. Total Cost of Ownership

Future analysis should consider:

```text
Purchase Price
+ Installation
+ Electricity
+ Membrane Replacement
+ Filter Replacement
+ Maintenance
+ Service
```

### 4. Modular Scalability

A modular architecture could allow customers to scale from approximately:

```text
500 LPH → 1000 LPH → 2000 LPH → 5000 LPH+
```

---

# Data Limitations

This is a **market screening study**, not a statistically representative census of the Indian RO market.

Important limitations:

1. Public online prices may differ from negotiated prices.
2. GST, installation, transportation, customization, and pretreatment may not be included.
3. Some technical specifications are not publicly disclosed.
4. Marketplace listings do not automatically prove that the seller manufactures every component.
5. The sample contains only 20 products.
6. Product prices, models, specifications, and availability can change over time.

---

# Reproduction

# ▶️ How to Run the Project

## 1. Install Python

Python 3.9+ is recommended.

```bash
python --version
```

## 2. Install Dependencies

For the Streamlit application:

```bash
pip install pandas numpy streamlit
```

For the complete analytical environment:

```bash
pip install pandas numpy streamlit matplotlib openpyxl
```

## 3. Place the Dataset

The application expects:

```text
RO_Product_Market_Research_Clean.csv
```

in the same working directory as:

```text
ro_market_analysis.py
```

Recommended structure:

```text
Project/
│
├── ro_market_analysis.py
└── RO_Product_Market_Research_Clean.csv
```

## 4. Run Streamlit

```bash
streamlit run ro_market_analysis.py
```

The local Streamlit application will open in the browser.

---

## Power BI

1. Open Power BI Desktop.
2. Select **Home → Get Data → Text/CSV**.
3. Import `RO_Product_Market_Research_Clean.csv`.
4. Rename the table to `RO_Products`.
5. Add the DAX calculations.
6. Build the dashboard according to the Power BI layout.
7. Set `Source URL` as **Web URL** data category.
8. Save the report as:

```text
RO_Product_Market_Research_India.pbix
```

---

# Deliverables

| Deliverable | File |
|---|---|
| Clean Dataset | `RO_Product_Market_Research_Clean.csv` |
| Excel Analysis | `RO_Product_Market_Research_India.xlsx` |
| Python Script | `ro_market_analysis.py` |
| Business Report | `RO_Product_Market_Research_Report.docx` |
| Power BI Package | `RO_Product_Market_Research_PowerBI_Ready.zip` |
| Documentation | `README_RO_Product_Market_Research.md` |

---

# Business Takeaway

The sample shows a strong relationship between RO capacity and absolute listed price, while larger systems generally show lower price per LPH. The market sample is particularly concentrated around 500 LPH and 1,000 LPH systems.

The research also highlights incomplete public technical information across many listings. Transparent specifications, standardized configurations, lifecycle-cost information, and clearly documented OEM/service capabilities could therefore be investigated as areas of differentiation.

These observations should be validated with additional supplier quotations, technical specifications, customer requirements, and broader market research before commercial decisions.

---

## Disclaimer

This project is intended for **educational, analytical, and market-research purposes**.

Prices and specifications are based on publicly available listings and should be independently verified with the relevant manufacturer or supplier before procurement or investment decisions.

Supplier classification in this project is not a legal or commercial certification of manufacturing status.

---

**Project:** RO Product & Market Research Analysis  
**Market:** India  
**Category:** Industrial & Commercial Reverse Osmosis Systems  
**Tools:** Python | Pandas | NumPy | Streamlit | Excel | Power BI | DAX
