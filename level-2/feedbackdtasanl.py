n = int(input())

ratings = []
categories = []

for _ in range(n):
    line = input().strip()
    parts = line.split(',', 2)
    ratings.append(int(parts[0]))
    categories.append(parts[1])

base_order = ['praise', 'feature', 'bug', 'complaint']

# ── 1. Rating Distribution ────────────────────────────────────────────────
print("=== Rating Distribution ===")
for star in range(5, 0, -1):
    count = ratings.count(star)
    if count == 0:
        print(str(star) + ": (" + str(count) + ")")
    else:
        bar = "\u2588" * count
        print(str(star) + ": " + bar + " (" + str(count) + ")")

print("")

# ── 2. Category Breakdown ─────────────────────────────────────────────────
print("=== Category Breakdown ===")

if n == 0:
    display_order = ['bug', 'feature', 'praise', 'complaint']
else:
    display_order = sorted(base_order,
                           key=lambda c: (-categories.count(c), base_order.index(c)))

for cat in display_order:
    count = categories.count(cat)
    if count == 0:
        print(cat + ": (" + str(count) + ")")
    else:
        bar = "\u2588" * count
        print(cat + ": " + bar + " (" + str(count) + ")")

print("")

# ── 3. Sentiment Summary ──────────────────────────────────────────────────
print("=== Sentiment Summary ===")
print("Total feedback: " + str(n))

if n == 0:
    print("Average rating: 0.0")
    print("Most common category: none")
    print("Highest rating: none")
    print("Lowest rating: none")
else:
    average = sum(ratings) / len(ratings)
    avg_str = "{:.1f}".format(average)
    print("Average rating: " + avg_str)

    max_count = max(categories.count(c) for c in base_order)
    top_cats = [c for c in base_order if categories.count(c) == max_count]

    if len(top_cats) == 1:                          # len() with parentheses, NOT len[]
        print("Most common category: " + top_cats[0] + " (" + str(max_count) + ")")
    else:
        tied = ', '.join(top_cats)
        print("Most common category: " + tied + " (" + str(max_count) + " each)")

    highest = max(ratings)
    lowest = min(ratings)
    highest_count = ratings.count(highest)
    lowest_count = ratings.count(lowest)

    h_word = "time" if highest_count == 1 else "times"
    l_word = "time" if lowest_count == 1 else "times"

    print("Highest rating: " + str(highest) + " (" + str(highest_count) + " " + h_word + ")")
    print("Lowest rating: " + str(lowest) + " (" + str(lowest_count) + " " + l_word + ")")