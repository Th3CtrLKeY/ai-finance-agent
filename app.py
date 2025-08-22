import streamlit as st
from src.agent import run_agent
import pandas as pd

#Page Configuration
st.set_page_config(
    page_title="AI Financial Analyst Agent",
    page_icon="🤖",
    layout="wide",
)

#Sidebar for controls
with st.sidebar:
    st.header("⚙️ Controls")
    st.write("Select the stocks you want to analyze.")

    try:
        stock_list_df = pd.read_csv("data/nifty50_stocks.csv")

        selected_stocks = st.multiselect(
            'Select Stocks (up to 5)',
            options=stock_list_df['CompanyName'],
            max_selections=5
        )

        generate_button =st.button("Generate Financial Briefing", type ="primary")

    except FileNotFoundError:
        st.error("the stock list file is missing.")
        generate_button = False

#App Title and Description
st.title("📈 AI Financial Analyst Agent")
st.image("assets/header_image.jpg", use_container_width=True) #  Header Image

st.markdown("""
Welcome! This app is your personal AI financial analyst. It provides a real-time briefing for your selected stocks by:
- **Fetching** the latest stock prices.
- **Gathering** top news headlines.
- **Analyzing** market sentiment with FinBERT.
- **Synthesizing** a professional report with a Large Language Model.

**To get started, select up to 5 stocks from the sidebar on the left and click 'Generate'.**
""")

st.divider() #visual separator

#Stock selection UI
# try:
#     stock_list_df = pd.read_csv("data/nifty50_stocks.csv")
#     selected_stocks = st.multiselect(
#         "Select Stocks (up to 5)",
#         options=stock_list_df["CompanyName"],
#         max_selections=5
#         )


# Report Generation Logic
if generate_button:
    if selected_stocks:
        portfolio_df = stock_list_df[stock_list_df['CompanyName'].isin(selected_stocks)]
        
        with st.spinner("🤖 Your agent is analyzing the market... This may take a moment."):
            try:
                report = run_agent(portfolio_df)
                
                # Display the report inside a container with a border
                with st.container(border=True):
                    st.subheader("Your Generated Financial Report")
                    st.markdown(report)
                
                st.success("Report generated successfully!")
                
            except Exception as e:
                st.error(f"An error occurred while running the agent: {e}")
    else:
        st.warning("Please select at least one stock from the sidebar.")