import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Simple Dashboard",
    page_icon="📊",
    layout="wide"
)

# Generate Sample Data
np.random.seed(0)
data = {
    'Month': np.repeat(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 3),
    'Category': np.tile(['A', 'B', 'C'], 5),
    'Sales': np.random.randint(100, 500, size=15)
}
df = pd.DataFrame(data)

# Main Title
st.title("Simple Dashboard")

# Sidebar Controls
with st.sidebar:
    st.title("Dashboard Controls")
    category_filter = st.multiselect("Select Categories", df['Category'].unique(), default=df['Category'].unique())

# Main Content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Sample Dashboard on Sales")
    filtered_df = df[df['Category'].isin(category_filter)]
    fig = px.bar(filtered_df, x='Month', y='Sales', color='Category', barmode='group')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Key Statistics")
    total_sales = filtered_df['Sales'].sum()
    avg_sales = filtered_df['Sales'].mean()
    st.metric("Total Sales", f"${total_sales:,.0f}")
    st.metric("Average Sales", f"${avg_sales:,.0f}")
