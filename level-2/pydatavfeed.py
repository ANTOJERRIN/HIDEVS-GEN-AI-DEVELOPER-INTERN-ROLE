
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter

# Read Input
n = int(input())

ratings = []
categories = []

for _ in range(n):
    line = input().strip()
    parts = line.split(',', 2)
    rating = int(parts[0])
    category = parts[1]
    ratings.append(rating)
    categories.append(category)

# Pre-compute counts
rating_counts = Counter(ratings)
cat_counts = Counter(categories)

cat_order = ['praise', 'bug', 'feature', 'complaint']
cat_colors = {
    'praise':    '#4CAF50',
    'bug':       '#F44336',
    'feature':   '#2196F3',
    'complaint': '#FF9800',
}
present_cats = [c for c in cat_order if c in cat_counts]

# Figure layout
fig, axes = plt.subplots(1, 3, figsize=(16, 6))
fig.patch.set_facecolor('#1E1E2E')
fig.suptitle('Feedback Data Analysis', fontsize=18, fontweight='bold', color='white', y=1.01)

# ------------------------------------
# 1. Rating Distribution - Vertical Bar
# ------------------------------------
ax1 = axes[0]
ax1.set_facecolor('#2A2A3E')

x_vals = [1, 2, 3, 4, 5]
y_vals = [rating_counts.get(r, 0) for r in x_vals]
colors = ['#F44336', '#FF9800', '#FFC107', '#8BC34A', '#4CAF50']

bars = ax1.bar(x_vals, y_vals, color=colors, width=0.6, edgecolor='white', linewidth=0.5)

for bar, val in zip(bars, y_vals):
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.05,
        str(val),
        ha='center', va='bottom',
        color='white', fontsize=11, fontweight='bold'
    )

ax1.set_title('Rating Distribution', color='white', fontsize=13, pad=12)
ax1.set_xlabel('Rating (1-5)', color='#AAAACC', fontsize=10)
ax1.set_ylabel('Count', color='#AAAACC', fontsize=10)
ax1.set_xticks(x_vals)
ax1.set_xticklabels(['1', '2', '3', '4', '5'], color='white')
ax1.tick_params(colors='white')
ax1.spines['bottom'].set_color('#444466')
ax1.spines['top'].set_color('#444466')
ax1.spines['left'].set_color('#444466')
ax1.spines['right'].set_color('#444466')
ax1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax1.set_ylim(0, max(y_vals) + 1.2)

# ------------------------------------
# 2. Category Breakdown - Horizontal Bar
# ------------------------------------
ax2 = axes[1]
ax2.set_facecolor('#2A2A3E')

cat_vals = [cat_counts[c] for c in present_cats]
bar_colors = [cat_colors[c] for c in present_cats]

ax2.set_yticks(range(len(present_cats)))
ax2.set_yticklabels([c.capitalize() for c in present_cats], color='white')

hbars = ax2.barh(range(len(present_cats)), cat_vals, color=bar_colors, edgecolor='white', linewidth=0.5, height=0.5)

for bar, val in zip(hbars, cat_vals):
    ax2.text(
        bar.get_width() + 0.05,
        bar.get_y() + bar.get_height() / 2,
        str(val),
        va='center', ha='left',
        color='white', fontsize=11, fontweight='bold'
    )

ax2.set_title('Category Breakdown', color='white', fontsize=13, pad=12)
ax2.set_xlabel('Count', color='#AAAACC', fontsize=10)
ax2.tick_params(colors='white')
ax2.spines['bottom'].set_color('#444466')
ax2.spines['top'].set_color('#444466')
ax2.spines['left'].set_color('#444466')
ax2.spines['right'].set_color('#444466')
ax2.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax2.set_xlim(0, max(cat_vals) + 1.2)
ax2.invert_yaxis()

# ------------------------------------
# 3. Sentiment Summary - Stats Cards
# ------------------------------------
ax3 = axes[2]
ax3.set_facecolor('#2A2A3E')
ax3.axis('off')
ax3.set_title('Sentiment Summary', color='white', fontsize=13, pad=12)

total = n
average = sum(ratings) / total
most_common_cat, most_common_cnt = cat_counts.most_common(1)[0]
highest = max(ratings)
lowest = min(ratings)
highest_count = rating_counts[highest]
lowest_count = rating_counts[lowest]

def times(x):
    return "time" if x == 1 else "times"

stats = [
    ("Total Feedback",       str(total)),
    ("Average Rating",       str(round(average, 1)) + " / 5.0"),
    ("Most Common Category", most_common_cat.capitalize() + " (" + str(most_common_cnt) + ")"),
    ("Highest Rating",       str(highest) + " star (" + str(highest_count) + " " + times(highest_count) + ")"),
    ("Lowest Rating",        str(lowest) + " star (" + str(lowest_count) + " " + times(lowest_count) + ")"),
]

for i, (label, value) in enumerate(stats):
    y_pos = 0.85 - i * 0.17
    rect = mpatches.FancyBboxPatch(
        (0.02, y_pos - 0.06), 0.96, 0.13,
        boxstyle="round,pad=0.02",
        linewidth=1, edgecolor='#555577',
        facecolor='#3A3A5E',
        transform=ax3.transAxes, clip_on=False
    )
    ax3.add_patch(rect)
    ax3.text(0.08, y_pos + 0.025, label,
             transform=ax3.transAxes,
             fontsize=9, color='#AAAACC', va='center')
    ax3.text(0.08, y_pos - 0.015, value,
             transform=ax3.transAxes,
             fontsize=12, color='white', fontweight='bold', va='center')

# Save
plt.tight_layout(pad=2.0)
plt.savefig('feedback_analysis.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.show()
print("Chart saved as feedback_analysis.png")