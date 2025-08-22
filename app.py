import streamlit as st
from src.agent import run_agent

#Page Configuration
st.set_page_config(
    page_title="AI Financial Analyst Agent",
    page_icon="🤖",
    layout="wide",

)

#App Title and Description
st.title("AI Financial Analyst Agent")
st.write(
    "Welcome! This agent provides a daily financial briefing for your stock portfolio. "
    "It fetches real-time stock prices, gathers the latest news, analyzes sentiment, "
    "and uses a Large Language Model to generate a professional report."
)
st.markdown("---")

#"Generate" button
if st.button("Genrate Today's Financial Briefing", type="primary"):
    with st.spinner("🤖 Your agent is thinking... Fetching prices, reading news, and analyzing sentiment. Please wait a moment."):
        try:
            #Call the agents main function
            report = run_agent()

            #display the report
            st.markdown("---")
            st.subheader("Your generated Financial Report")
            st.markdown(report)
            st.success("Report generated successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

else:
    st.info("Click the 'Generate' button to get started.")