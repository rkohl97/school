import tkinter as tk
import openpyxl
import random


def read_phrases_from_excel(file_name):
    phrases_with_topics = []
    try:
        workbook = openpyxl.load_workbook(file_name)
        sheet = workbook.active
        for row in sheet.iter_rows(values_only=True):
            if row:  # Ensure row is not empty
                topic = row[0]  # Assuming topic is in the first column
                phrases = row[1:]  # Assuming phrases start from the second column
                for phrase in phrases:
                    if phrase:  # Ensure phrase is not empty
                        phrases_with_topics.append((topic, phrase))
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return phrases_with_topics


def pick_random_phrase(phrases_with_topics):
    if phrases_with_topics:
        return random.choice(phrases_with_topics)
    else:
        return ("No topics found", "No phrases found")


def display_gui(random_topic, random_phrase):
    root = tk.Tk()
    root.title("Random Phrase Picker")

    topic_label = tk.Label(root, text="Randomly picked topic:")
    topic_label.pack()
    topic_value = tk.Label(root, text=random_topic)
    topic_value.pack()

    phrase_label = tk.Label(root, text="Randomly picked phrase:")
    phrase_label.pack()
    phrase_value = tk.Label(root, text=random_phrase)
    phrase_value.pack()

    root.mainloop()


if __name__ == "__main__":
    file_name = "listofphrases.xlsx"
    phrases_with_topics = read_phrases_from_excel(file_name)
    random_topic, random_phrase = pick_random_phrase(phrases_with_topics)
    display_gui(random_topic, random_phrase)
