import json
import os

while True:
    command = input().strip()
    if command == 'END':
        break

    if command.startswith('SAVE '):
        feedback_text = command[5:]
        with open('feedback.txt', 'a') as f:
            f.write(f'[FEEDBACK] {feedback_text}\n')
        print(f'Saved: {feedback_text}')

    elif command == 'LOAD':
        if not os.path.exists('feedback.txt'):
            print('No feedback found')
        else:
            with open('feedback.txt', 'r') as f:
                lines = f.read().splitlines()
            for line in lines:
                print(line)

    elif command == 'EXPORT':
        if not os.path.exists('feedback.txt'):
            feedbacks = []
        else:
            with open('feedback.txt', 'r') as f:
                feedbacks = f.read().splitlines()
        last_five = feedbacks[-5:]
        with open('export.json', 'w') as f:
            json.dump({'feedbacks': last_five}, f)   # fixed: was 'josn' (typo)
        print(f'Exported {len(last_five)} feedbacks')