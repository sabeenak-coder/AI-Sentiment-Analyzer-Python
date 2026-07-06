from textblob import TextBlob

print("=" * 40)
print("     AI SENTIMENT ANALYZER")
print("=" * 40)

while True:
    text = input("\nEnter a sentence (or type 'exit' to quit): ")

    if text.lower() == "exit":
        print("Thank you for using AI Sentiment Analyzer!")
        break

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    print("\nSentiment Score:", polarity)

    if polarity > 0:
        print(" Positive Sentiment")
    elif polarity < 0:
        print(" Negative Sentiment")
    else:
        print(" Neutral Sentiment")