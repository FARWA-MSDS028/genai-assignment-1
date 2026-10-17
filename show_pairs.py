"""Print the first few real/fake article pairs (adjacent rows) for Task 3.5."""
import csv

with open('data/txt_train.csv', encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))

# Pairs of real/fake articles are adjacent rows, so show rows (0, 1), (2, 3), (4, 5).
for i in range(0, 6, 2):
    for row in (rows[i], rows[i + 1]):
        print(f"[{row['label'].upper()}]")
        print(row['article'][:600])  # first 600 characters only
        print('-' * 60)
    print('=' * 60)