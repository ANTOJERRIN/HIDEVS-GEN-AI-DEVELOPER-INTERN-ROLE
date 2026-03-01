# Write your solution here

class Feedback:
    # Class variable
    total_feedbacks = 0
    
    def __init__(self, text, rating, category):
        # Initialize instance variables
        self.text = text
        self.rating = rating
        self.category = category
        
        # Increment class variable
        Feedback.total_feedbacks += 1
    
    def get_summary(self):
        # Return first 30 chars + '...' if longer
        if len(self.text) > 30:
            return self.text[:30] + "..."
        else:
            return self.text
    
    def is_positive(self):
        # Return True if rating ≥ 4
        return self.rating >= 4
    
    @classmethod
    def get_total(cls):
        # Return total feedbacks
        return cls.total_feedbacks


# Main program (DO NOT MODIFY)
def main():
    n = int(input())
    feedbacks = []
    
    for i in range(n):
        text = input()
        rating = int(input())
        category = input()
        feedbacks.append(Feedback(text, rating, category))
    
    for i, fb in enumerate(feedbacks, 1):
        summary = fb.get_summary()
        positive = fb.is_positive()
        print(f"Feedback {i}: {summary} (Positive: {positive})")
    
    print(f"Total feedbacks: {Feedback.get_total()}")

if __name__ == "__main__":
    main()