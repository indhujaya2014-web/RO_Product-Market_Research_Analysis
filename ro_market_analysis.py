from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st

# ============================================================
# RO PRODUCT & MARKET RESEARCH ANALYSIS - INDIA (STREAMLIT APP)
# Run via terminal: streamlit run ro_market_analysis.py
# ============================================================

st.set_page_config(
    page_title="RO Market Research Dashboard",
    page_icon="💧",
    layout="wide",
)

INPUT = "RO_Product_Market_Research_Clean.csv"
OUT = Path("ro_analysis_outputs")
OUT.mkdir(exist_ok=True)


@st.cache_data
def load_data(file_path):
  df = pd.read_csv(file_path)
  df["Price (INR)"] = pd.to_numeric(df["Price (INR)"], errors="coerce")
  df["RO Capacity (LPH)"] = pd.to_numeric(
      df["RO Capacity (LPH)"], errors="coerce"
  )
  df["Price per LPH (INR)"] = df["Price (INR)"] / df["RO Capacity (LPH)"]

  df["Capacity Range"] = pd.cut(
      df["RO Capacity (LPH)"],
      bins=[0, 500, 1000, 2000, 5000, 10000, np.inf],
      labels=[
          "<=500 LPH",
          "501-1000 LPH",
          "1001-2000 LPH",
          "2001-5000 LPH",
          "5001-10000 LPH",
          ">10000 LPH",
      ],
  )
  return df


# Check if file exists, else display error message
if not Path(INPUT).exists():
  st.error(
      f"Dataset file '{INPUT}' not found. Please upload or place it in the"
      " working directory."
  )
  st.stop()

df = load_data(INPUT)

# ============================================================
# STREAMLIT SIDEBAR & FILTERS
# ============================================================
st.sidebar.title("🔍 Market Filters")
selected_suppliers = st.sidebar.multiselect(
    "Select Manufacturer / Supplier",
    options=df["Manufacturer/Supplier"].unique(),
    default=df["Manufacturer/Supplier"].unique(),
)

capacity_filter = st.sidebar.slider(
    "Filter by Max RO Capacity (LPH)",
    int(df["RO Capacity (LPH)"].min()),
    int(df["RO Capacity (LPH)"].max()),
    (
        int(df["RO Capacity (LPH)"].min()),
        int(df["RO Capacity (LPH)"].max()),
    ),
)

# Apply filters
filtered_df = df[
    (df["Manufacturer/Supplier"].isin(selected_suppliers))
    & (df["RO Capacity (LPH)"].between(capacity_filter[0], capacity_filter[1]))
]

# ============================================================
# MAIN DASHBOARD HEADER
# ============================================================
st.title("💧 Indian Commercial & Industrial RO Market Research Analysis")
st.markdown(
    "Interactive business intelligence dashboard evaluating product"
    " specifications, pricing trends, and manufacturer positioning."
)

# Top KPI Summary Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Products Analyzed", len(filtered_df))
col2.metric(
    "Average Listed Price",
    f"₹{filtered_df['Price (INR)'].mean():,.0f}"
    if not filtered_df.empty
    else "₹0",
)
col3.metric(
    "Max RO Capacity",
    f"{filtered_df['RO Capacity (LPH)'].max():,.0f} LPH"
    if not filtered_df.empty
    else "0 LPH",
)
col4.metric("Active Manufacturers", filtered_df["Manufacturer/Supplier"].nunique())

st.divider()

# ============================================================
# TABULAR & VISUAL INSIGHTS
# ============================================================
tab1, tab2, tab3 = st.tabs(
    ["📊 Market Visualizations", "📋 Summary Tables", "🔍 Raw Dataset Explorer"]
)

with tab1:
  st.subheader("Price vs. RO Capacity Distribution")
  if not filtered_df.empty:
    # Scatter plot using Streamlit native chart
    st.scatter_chart(
        filtered_df,
        x="RO Capacity (LPH)",
        y="Price (INR)",
        color="Manufacturer/Supplier",
        size="Price (INR)",
    )
  else:
    st.warning("No data available for the selected filters.")

  col_a, col_b = st.columns(2)

  with col_a:
    st.subheader("Average Price by Exact Capacity")
    if not filtered_df.empty:
      avg_by_cap = (
          filtered_df.groupby("RO Capacity (LPH)")["Price (INR)"]
          .mean()
          .reset_index()
      )
      st.bar_chart(avg_by_cap.set_index("RO Capacity (LPH)"))

  with col_b:
    st.subheader("Manufacturer Price Comparison")
    if not filtered_df.empty:
      m_comp = (
          filtered_df.groupby("Manufacturer/Supplier")["Price (INR)"]
          .mean()
          .reset_index()
      )
      st.bar_chart(
          m_comp.set_index("Manufacturer/Supplier"), color="#2ca02c"
      )

with tab2:
  st.subheader("Capacity Range Summary Table")
  capacity_summary = (
      filtered_df.groupby("Capacity Range", observed=False)
      .agg(
          Products=("Product/Model", "count"),
          Avg_Price_INR=("Price (INR)", "mean"),
          Median_Price_INR=("Price (INR)", "median"),
          Min_Price_INR=("Price (INR)", "min"),
          Max_Price_INR=("Price (INR)", "max"),
          Avg_Price_per_LPH=("Price per LPH (INR)", "mean"),
      )
      .reset_index()
  )
  st.dataframe(capacity_summary, use_container_width=True)

  st.subheader("Manufacturer Performance Summary")
  manufacturer_summary = (
      filtered_df.groupby("Manufacturer/Supplier")
      .agg(
          Products=("Product/Model", "count"),
          Max_Capacity_LPH=("RO Capacity (LPH)", "max"),
          Avg_Price_INR=("Price (INR)", "mean"),
          Supplier_Type=("Supplier Type", "first"),
          Location=("Location", "first"),
      )
      .reset_index()
      .sort_values("Avg_Price_INR", ascending=False)
  )
  st.dataframe(manufacturer_summary, use_container_width=True)

with tab3:
  st.subheader("Filtered Raw Dataset")
  st.dataframe(filtered_df, use_container_width=True)

  # Export CSV button
  csv_data = filtered_df.to_csv(index=False).encode("utf-8")
  st.download_button(
      label="Download Filtered Data as CSV",
      data=csv_data,
      file_name="filtered_ro_market_data.csv",
      mime="text/csv",
  )

# ============================================================
# EXPORT BATCH FILES SILENTLY IN BACKGROUND
# ============================================================
capacity_summary_full = (
    df.groupby("Capacity Range", observed=False)
    .agg(
        Products=("Product/Model", "count"),
        Avg_Price_INR=("Price (INR)", "mean"),
        Median_Price_INR=("Price (INR)", "median"),
        Min_Price_INR=("Price (INR)", "min"),
        Max_Price_INR=("Price (INR)", "max"),
        Avg_Price_per_LPH=("Price per LPH (INR)", "mean"),
    )
    .reset_index()
)
manufacturer_summary_full = (
    df.groupby("Manufacturer/Supplier")
    .agg(
        Products=("Product/Model", "count"),
        Max_Capacity_LPH=("RO Capacity (LPH)", "max"),
        Avg_Price_INR=("Price (INR)", "mean"),
        Supplier_Type=("Supplier Type", "first"),
        Location=("Location", "first"),
    )
    .reset_index()
)

capacity_summary_full.to_csv(OUT / "capacity_summary.csv", index=False)
manufacturer_summary_full.to_csv(OUT / "manufacturer_summary.csv", index=False)
df.to_csv(OUT / "ro_research_analysis_ready.csv", index=False)