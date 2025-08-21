import pandas as pd
import yfinance as yf


def get_stock_prices(portfolio_path: str) -> dict:
    """
    Retrieves the most recent closing price for each stock in a portfolio CSV.

    Args:
        portfolio_path (str): The string path to the portfolio.csv file.
                              The CSV must contain a 'StockSymbol' column.

    Returns:
        dict: A dictionary mapping stock symbols to their most recent closing price.
    """
    try:
        portfolio_df = pd.read_csv(portfolio_path)
    except FileNotFoundError:
        print(f"Warning: Portfolio file not found at '{portfolio_path}'.")
        return {}

    if 'StockSymbol' not in portfolio_df.columns:
        print(f"Warning: 'StockSymbol' column not found in '{portfolio_path}'.")
        return {}

    results = {}
    for symbol in portfolio_df['StockSymbol']:
        try:
            price = yf.Ticker(symbol).history(period='1d')['Close'].iloc[0]
            results[symbol] = price
        except IndexError:
            # Handles cases where a stock symbol is invalid, as yfinance returns
            # an empty DataFrame, causing an IndexError on .iloc[0].
            print(f"Warning: Could not retrieve price for '{symbol}'. It may be an invalid symbol.")

    return results


# This block allows us to test the function directly
if __name__ == "__main__":
    # The path to our data file, relative to the project's root directory
    portfolio_file = 'C:\\Users\\raghu\\Desktop\\Projects\\finance_project\\data\\portfolio.csv'
    prices = get_stock_prices(portfolio_file)

    if prices:
        print("\n--- Final Stock Prices ---")
        for symbol, price in prices.items():
            print(f"{symbol}: ₹{price}")