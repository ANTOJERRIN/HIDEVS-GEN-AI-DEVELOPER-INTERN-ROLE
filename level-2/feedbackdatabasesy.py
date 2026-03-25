import sqlite3

def setup_feedback_db():
    conn = sqlite3.connect('feedback_system.db')  # Fix 3: file DB, not :memory:
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        rating INTEGER CHECK(rating BETWEEN 1 AND 5),
        category TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    feedback_data = [
        ('Great product, easy to use', 5, 'praise'),
        ('Too many bugs, needs fixing', 2, 'bug'),
        ('Good but expensive', 4, 'complaint'),  # Fix 1: 5 → 4
        ('Love the new update', 5, 'praise'),
        ('Customer service was slow', 3, 'service')
    ]
    cursor.executemany(
        "INSERT INTO feedback (text, rating, category) VALUES (?, ?, ?)",
        feedback_data
    )

    cursor.execute("SELECT AVG(rating) FROM feedback")
    avg_rating = cursor.fetchone()[0]
    print(f"Average rating: {avg_rating:.1f}")

    print("\nFeedback by category:")
    cursor.execute("""
    SELECT category, COUNT(*)
    FROM feedback
    GROUP BY category
    ORDER BY category
    """)
    for category, count in cursor.fetchall():
        print(f"{category}: {count}")

    print("\nMost recent feedback:")
    cursor.execute("""
    SELECT text, rating
    FROM feedback
    ORDER BY id DESC
    LIMIT 2
    """)
    results = cursor.fetchall()
    for text, rating in results:  # Fix 2: iterate `results`, not cursor.fetchall()
        print(f"{text[:30]} (Rating: {rating})")

    conn.commit()
    conn.close()

setup_feedback_db()