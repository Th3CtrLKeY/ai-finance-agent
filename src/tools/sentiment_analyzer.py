from transformers import pipeline

class SentimentAnalyzer:
    """
    A class to handle sentiment analysis using a pre-trained financial model
    """
    def __init__(self, model_name="ProsusAI/finbert"):
        """
        Initializes the sentiment analysis pipeline.
        The model is loaded only once when the class is instantiated.
        """
        print(f"Loading sentiment model '{model_name}'...")
        #device = 0 -> GPU device = -1 -> CPU
        self.sentiment_pipeline = pipeline("sentiment-analysis", model=model_name, device=0)
        print("Sentiment model loaded successfully.")

    def analyze(self, text):
        """
        Analyzes the sentiment of the given text.

        Args: 
            text (str): The text (e.g. a news headline) to analyze.

        Returns:
            dict: A dictionary containing the sentiment label and score.
        """
        try:
            result = self.sentiment_pipeline(text)[0]
            return result
        except Exception as e:
            print(f"Error during sentiment analysis: {e}")
            return {"label": "N/A", "score": 0.0}

#This block allows us to test the analyzer directly
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()

    #Test Cases
    positive_headline = "Tata Motors reports record profits and a 50% surge in EV sales."
    negative_headline = "Reliance Industries faces new regulatory hurdles, stock tumbles 5%."
    neutral_headline = "HDFC Bank is scheduled to announce quarterly earnings next Tuesday."
    
    print("\n--- Testing Sentiment Analyzer ---")
    
    result_pos = analyzer.analyze(positive_headline)
    print(f"Headline: '{positive_headline}'")
    print(f"Sentiment: {result_pos['label']} (Score: {result_pos['score']:.4f})\n")

    result_neg = analyzer.analyze(negative_headline)
    print(f"Headline: '{negative_headline}'")
    print(f"Sentiment: {result_neg['label']} (Score: {result_neg['score']:.4f})\n")

    result_neu = analyzer.analyze(neutral_headline)
    print(f"Headline: '{neutral_headline}'")
    print(f"Sentiment: {result_neu['label']} (Score: {result_neu['score']:.4f})\n")