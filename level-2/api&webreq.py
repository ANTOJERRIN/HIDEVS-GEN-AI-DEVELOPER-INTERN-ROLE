# Write your solution here

# Implement the two functions below
def mock_weather_api(city):
    weather_data = {
        'new york': {'temp': 15, 'condition': 'cloudy'},
        'london': {'temp': 10, 'condition': 'rainy'},
        'tokyo': {'temp': 22, 'condition': 'sunny'},
        'delhi': {'temp': 35, 'condition': 'hot'}
    }
    # Case-insensitive lookup
    return weather_data.get(city.lower(), {'temp': 20, 'condition': 'unknown'})


def analyze_feedback_with_context(feedback, city):
    weather_info = mock_weather_api(city)

    # Trim feedback to 100 chars
    if len(feedback) > 100:
        feedback_trimmed = feedback[:100] + "..."
    else:
        feedback_trimmed = feedback

    # Check keywords
    keywords = ['hot', 'cold', 'rain', 'sunny', 'weather']
    feedback_lower = feedback.lower()
    weather_mentioned = any(word in feedback_lower for word in keywords)

    # Build dictionary
    analysis = {
        'feedback': feedback_trimmed,
        'city': city,
        'weather': weather_info['condition'],
        'temperature': weather_info['temp'],
        'weather_mentioned': weather_mentioned
    }

    # Insights
    if weather_info['temp'] > 30 and 'hot' in feedback_lower:
        analysis['insight'] = 'Customer mentioning heat during hot weather - consider climate control feedback'
    elif weather_info['condition'] == 'rainy' and 'rain' in feedback_lower:
        analysis['insight'] = 'Weather likely affecting customer experience'

    return analysis


# Main program
if __name__ == "__main__":
    feedback = input().strip()
    city = input().strip()
    result = analyze_feedback_with_context(feedback, city)
    print(f"Analysis: {result}")