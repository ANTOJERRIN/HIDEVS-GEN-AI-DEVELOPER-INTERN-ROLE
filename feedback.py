# Write your solution here

# Implement the three functions
def clean_text(text):
    # Remove leading/trailing spaces and convert to lowercase
    return text.strip().lower()

def extract_keywords(text):
    # Return first 3 words as list
    words = text.split()
    return words[:3]

def calculate_sentiment(rating):
    # Return 'good' or 'bad' based on rating
    if rating >= 3:
        return "good"
    else:
        return "bad"

# Main program (DO NOT MODIFY)
def main():
    text = input()
    rating = int(input())
    
    clean = clean_text(text)
    keywords = extract_keywords(clean)
    sentiment = calculate_sentiment(rating)
    
    print(f"Clean: {clean}")
    print(f"Keywords: {keywords}")
    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()