# Write your solution here

def analyze_feedback():

    # Read number of feedbacks
    n = int(input().strip())

    # Initialize data structures
    feedbacks = []

    # Read each feedback
    for _ in range(n):
        text = input().strip()
        rating = int(input().strip())
        category = input().strip()
        sentiment = input().strip()

        feedbacks.append({
            "text": text,
            "rating": rating,
            "category": category,
            "sentiment": sentiment
        })

    # Calculate statistics

    # Total feedbacks
    total_feedbacks = len(feedbacks)

    # Average rating
    total_rating = sum(f["rating"] for f in feedbacks)
    average_rating = round(total_rating / total_feedbacks, 2)

    # Most common category
    category_count = {}
    for f in feedbacks:
        cat = f["category"]
        category_count[cat] = category_count.get(cat, 0) + 1

    max_count = max(category_count.values())
    most_common_categories = [k for k, v in category_count.items() if v == max_count]
    most_common_category = sorted(most_common_categories)[0]

    # Sentiment counts
    sentiment_counts = {
        "positive": 0,
        "negative": 0,
        "neutral": 0
    }

    for f in feedbacks:
        sentiment_counts[f["sentiment"]] += 1

    # Average text length
    total_length = sum(len(f["text"]) for f in feedbacks)
    avg_text_length = round(total_length / total_feedbacks, 2)

    # Print result dictionary
    result = {
        "total_feedbacks": total_feedbacks,
        "average_rating": average_rating,
        "most_common_category": most_common_category,
        "sentiment_counts": sentiment_counts,
        "avg_text_length": avg_text_length
    }

    print(result)


analyze_feedback()