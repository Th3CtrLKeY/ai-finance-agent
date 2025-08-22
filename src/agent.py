
import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
from .tools.sentiment_analyzer import SentimentAnalyzer

# Import our custom tools
from .tools.price_fetcher import get_stock_prices
from .tools.news_fetcher import get_company_news

def run_agent():
    """
    The main function to run the financial agent.
    """
    # --- 1. Configuration and Setup ---
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    sentiment_analyzer = SentimentAnalyzer()
    # print("Starting the financial Agent...")
    
    portfolio_path = 'data/portfolio.csv'
    news_api_key = os.getenv("NEWS_API_KEY")

    # print("🚀 Starting the Financial Agent...")

    # --- 2. Data Gathering using Tools ---
    # print("   - Reading portfolio...")
    try:
        portfolio_df = pd.read_csv(portfolio_path)
    except FileNotFoundError:
        print(f"Error: Portfolio file not found at {portfolio_path}")
        return

    # print("   - Fetching latest stock prices...")
    stock_prices = get_stock_prices(portfolio_path)
    
    all_news = []
    # print("   - Fetching company news...")
    for index, row in portfolio_df.iterrows():
        company_name = row['CompanyName']
        news = get_company_news(company_name, news_api_key, num_articles=3)

        for new in news:
            sentiment = sentiment_analyzer.analyze(new['title'])
            new['sentiment'] = sentiment


        all_news.append({"company": company_name, "articles": news})

    # --- 3. Data Synthesis using LLM ---
    # print("   - Synthesizing report with Gemini...")

    # Create a detailed prompt for the LLM
    prompt = f"""
    You are a senior financial analyst providing a daily briefing.
    It is currently {pd.Timestamp.now().strftime('%A, %B %d, %Y at %I:%M %p IST')}.

    Here is the latest data, including sentiment analysis scores for each news headline:

    Current Stock Prices:
    {stock_prices}

    Recent News with Sentiment Scores:
    {all_news}

    Please generate a concise, professional report. Based on the provided sentiment scores and news, analyze each company's outlook. Your report must include:
    1.  **Overall Market Summary:** A brief, one-paragraph overview synthesizing the sentiment across all companies.
    2.  **Per-Stock Analysis:** For each company, provide:
        - The company name and its current stock price.
        - A one-sentence summary of the news, directly referencing the aggregated sentiment (e.g., "The sentiment is overwhelmingly positive...").
    3.  **Disclaimer:** A brief, standard financial disclaimer.

    Format the entire output in Markdown.
    """

    try:
        response = model.generate_content(prompt)
        report = response.text
    except Exception as e:
        report = f"Error generating report from Gemini: {e}"

    # --- 4. Final Output ---
    # print("\n" + "="*50)
    # print("📊 Your Daily Financial Briefing")
    # print("="*50 + "\n")
    return report


if __name__ == "__main__":
    final_report = run_agent()
    print(final_report)