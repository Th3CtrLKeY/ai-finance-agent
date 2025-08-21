import requests

def get_company_news(company_name, api_key, num_articles=5):
    """
    Fetches a specified number of recent news articles for a company.

    Args:
        company_name (str): The name of the company to search for.
        api_key (str): The API key for NewsAPI.org.
        num_articles (int): The number of articles to fetch.

    Returns:
        list: A list of dictionaries, each containing an article's title and url.
    """
    base_url = 'https://newsapi.org/v2/everything'
    params = {
        'q': company_name,
        'language': 'en',
        'pageSize': num_articles,
        'sortBy': 'relevancy'
    }

    headers = {
        'X-Api-Key': api_key
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error fetching news: Status code {response.status_code}")
            return []

        data = response.json()
        articles = data.get("articles", [])
        
        # Extract just the title and url from each article
        cleaned_articles = [
            {"title": article["title"], "url": article["url"]} 
            for article in articles
        ]
        
        return cleaned_articles

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return []



# This block allows us to test the function directly
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    # Get the API key
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    if not NEWS_API_KEY:
        print("Error: NEWS_API_KEY not found in .env file.")
    else:
        # Test with a sample company
        company = "Tata Motors"
        news = get_company_news(company, NEWS_API_KEY)

        if news:
            print(f"\n--- Top 5 News Articles for {company} ---")
            for i, article in enumerate(news, 1):
                print(f"{i}. {article['title']}")
                print(f"   Link: {article['url']}\n")