# 📈 AI Financial Analyst Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_DEPLOYED_APP_URL_HERE)

An intelligent agent that delivers real-time financial briefings for user-selected stocks by orchestrating multiple tools and synthesizing data with a Large Language Model.

---

### ✨ App Demo

*(Pro Tip: Record a short GIF of your app in action using a tool like Giphy Capture or ScreenToGif and embed it here. It's highly effective!)*



---

### ## 🚀 Overview

This project was built to solve the problem of information overload for retail investors. The agent automates the tedious process of gathering and analyzing market data by:
1.  Fetching real-time stock prices.
2.  Aggregating the latest news from financial markets.
3.  Performing sentiment analysis on news headlines using a specialized NLP model.
4.  Using a powerful LLM (Gemini 1.5 Pro) to synthesize all the information into a professional, human-readable report.

---

### ## ⚙️ System Architecture

The agent uses a modular, multi-tool design. The main orchestrator (`agent.py`) dynamically calls specialized tools to gather information before synthesizing the final report.

*(Create a simple diagram using a free tool like [diagrams.net](https://app.diagrams.net), export it as a PNG, add it to your `assets` folder, and embed it here.)*

![System Architecture Diagram](assets/architecture.png)

---

### ## 🛠️ Tech Stack

- **Backend & Orchestration:** Python, LangChain (conceptual)
- **AI/ML:** Google Gemini 1.5 Pro, Hugging Face Transformers (FinBERT)
- **Data Handling:** Pandas, yfinance API, NewsAPI
- **Frontend & Deployment:** Streamlit, Streamlit Community Cloud
- **Development:** Git, GitHub, VS Code

---

### ## 📦 Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/financial-agent.git](https://github.com/YOUR_USERNAME/financial-agent.git)
    cd financial-agent
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    - Create a `.env` file in the root directory.
    - Add your API keys to the `.env` file:
      ```
      NEWS_API_KEY="YOUR_NEWS_API_KEY"
      GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
      ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

---

### ## 🔮 Future Improvements

- [ ] **Historical Data Visualization:** Integrate Plotly to display interactive charts of stock performance over time.
- [ ] **Expanded Data Sources:** Incorporate sentiment from Twitter/X for a more holistic view.
- [ ] **Personalized Alerts:** Add a feature to send email alerts if the sentiment for a stock changes dramatically.
