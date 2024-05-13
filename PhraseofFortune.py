import tkinter as tk
from tkinter import messagebox
import openpyxl
import random

class PhraseGuessingGameGUI:
    player1_game = None
    player2_game = None

    def __init__(self, master, player_name, phrases, bg_color):
        # Initialize the game instance
        self.master = master
        self.player_name = player_name
        self.phrases = phrases
        self.bg_color = bg_color
        self.rounds_to_win = 2
        self.player_wins = 0
        self.current_round = 0
        self.current_player = None
        self.random_topic = ""
        self.random_phrase = ""
        self.remaining_attempts = 0
        self.correct_guesses = set()
        self.wrong_guesses = set()
        self.game_ongoing = False

        # Initialize GUI elements
        self.phrase_label = None
        self.attempts_label = None
        self.guessed_letters_label = None
        self.wins_label = None
        self.reset_button = None
        self.lose_button = None

        # Additional attributes to keep track of wins
        self.wins = 0

    def create_widgets(self):
        # Create GUI elements for the game
        self.new_round()  # Initialize a new round

        # Display player information and topic
        tk.Label(self.master, text=f"Player: {self.player_name}", bg=self.bg_color).pack()
        tk.Label(self.master, text="Randomly picked topic:", bg=self.bg_color).pack()
        tk.Label(self.master, text=self.random_topic, bg=self.bg_color).pack()

        # Display the phrase
        self.phrase_label = tk.Label(self.master, text="", bg=self.bg_color)
        self.phrase_label.pack()

        # Letter input and submit button
        tk.Label(self.master, text="Guess a letter:", bg=self.bg_color).pack()
        self.letter_entry = tk.Entry(self.master)
        self.letter_entry.pack()
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_letter)
        self.submit_button.pack()

        # Display wrong guesses and remaining attempts
        self.guessed_letters_label = tk.Label(self.master, text="Wrong guesses: ", bg=self.bg_color)
        self.guessed_letters_label.pack()
        self.attempts_label = tk.Label(self.master, text="", bg=self.bg_color)
        self.attempts_label.pack()

        # Display player wins
        self.wins_label = tk.Label(self.master, text=f"Wins: {self.wins}", bg=self.bg_color)
        self.wins_label.pack()

        # Reset button
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        # Lose button
        self.lose_button = tk.Button(self.master, text="Lose", command=self.lose_round)
        self.lose_button.pack()

    def new_round(self):
        # Start a new round
        self.reset_phrases()
        self.remaining_attempts = 10
        self.correct_guesses = set()
        self.wrong_guesses = set()
        self.game_ongoing = True
        self.current_round += 1
        self.pick_random_phrase()
        self.update_phrase_label()
        self.update_attempts_label()
        self.update_guessed_letters_label()

    def reset_phrases(self):
        # Reset phrases for the current player
        self.random_topic = ""
        self.random_phrase = ""
        if self.phrase_label:
            self.phrase_label.config(text="")
        if self.attempts_label:
            self.attempts_label.config(text="")
        if self.guessed_letters_label:
            self.guessed_letters_label.config(text="")

    def pick_random_phrase(self):
        # Pick a random phrase from the list of phrases
        if self.phrases:
            self.random_topic, self.random_phrase = random.choice(self.phrases)
            self.random_phrase = self.random_phrase.replace(" ", "").upper()

    def display_phrase(self):
        # Display the phrase with guessed letters revealed
        displayed_phrase = ""
        for char in self.random_phrase:
            if char.isalpha() and char in self.correct_guesses:
                displayed_phrase += char
            else:
                displayed_phrase += "_"
        return displayed_phrase

    def check_letter(self):
        # Check the guessed letter against the random phrase
        if not self.game_ongoing:
            return

        guessed_letter = self.letter_entry.get().upper()
        self.letter_entry.delete(0, tk.END)

        if not guessed_letter.isalpha() or len(guessed_letter) != 1:
            messagebox.showerror("Error", "Please enter a single alphabetical letter.")
            return

        if guessed_letter in self.correct_guesses or guessed_letter in self.wrong_guesses:
            messagebox.showinfo("Already Guessed", f"You've already guessed the letter '{guessed_letter}'.")
            return

        if guessed_letter in self.random_phrase:
            # If the guessed letter is correct
            self.correct_guesses.add(guessed_letter)
            self.update_phrase_label()
            if set(self.random_phrase) == self.correct_guesses:
                # If the player guessed the phrase correctly
                self.game_ongoing = False
                self.wins += 1
                self.update_wins_label()
                if self.wins == self.rounds_to_win:
                    # If a player wins the game
                    self.ask_rematch()
                else:
                    messagebox.showinfo("Round Won", f"{self.current_player} has guessed the phrase correctly!")
                    self.new_round()
        else:
            # If the guessed letter is wrong
            self.remaining_attempts -= 1
            self.update_attempts_label()
            self.wrong_guesses.add(guessed_letter)
            self.update_guessed_letters_label()
            if self.remaining_attempts == 0:
                # If the player runs out of attempts
                self.game_ongoing = False
                messagebox.showinfo("Round Over",
                                    f"Sorry, {self.current_player} has run out of attempts.\nThe phrase was: {self.random_phrase}")
                # Other player wins if one player loses
                if self.current_player == "Player 1":
                    other_player_game = self.player2_game
                else:
                    other_player_game = self.player1_game
                self.current_player = other_player_game.player_name
                other_player_game.wins += 1
                other_player_game.update_wins_label()
                self.update_wins_label()
                if other_player_game.wins == other_player_game.rounds_to_win:
                    # If the other player wins the game
                    self.ask_rematch()
                else:
                    messagebox.showinfo("Round Won", f"{self.current_player} has won the round!")
                    other_player_game.new_round()

    def update_phrase_label(self):
        # Update the phrase display label
        if self.phrase_label:
            self.phrase_label.config(text=self.display_phrase())

    def update_attempts_label(self):
        # Update the attempts left label
        if self.attempts_label:
            self.attempts_label.config(text=f"Attempts left: {self.remaining_attempts}")

    def update_guessed_letters_label(self):
        # Update the wrong guesses label
        if self.guessed_letters_label:
            self.guessed_letters_label.config(text=f"Wrong guesses: {' '.join(self.wrong_guesses)}")

    def update_wins_label(self):
        # Update the player wins label
        if self.wins_label:
            self.wins_label.config(text=f"Wins: {self.wins}")

    def reset_game(self):
        # Reset the game state
        self.current_round = 0
        self.wins = 0
        self.new_round()

    def lose_round(self):
        # End the current round and give the other player a win
        self.game_ongoing = False
        if self.current_player == "Player 1":
            other_player_game = self.player2_game
        else:
            other_player_game = self.player1_game
        self.current_player = other_player_game.player_name
        other_player_game.wins += 1
        other_player_game.update_wins_label()
        self.update_wins_label()
        if other_player_game.wins == other_player_game.rounds_to_win:
            # If the other player wins the game
            self.ask_rematch()
        else:
            messagebox.showinfo("Round Won", f"{self.current_player} has won the round!")
            other_player_game.new_round()

    def ask_rematch(self):
        # Ask if players want a rematch after the game ends
        rematch = messagebox.askyesno("Rematch", "Do you want a rematch?")
        if rematch:
            self.reset_game()

def read_phrases_from_excel(file_name):
    # Read phrases from an Excel file
    phrases_with_topics = []
    try:
        workbook = openpyxl.load_workbook(file_name)
        sheet = workbook.active
        for row in sheet.iter_rows(values_only=True):
            if row:
                topic = row[0]
                phrases = row[1:]
                for phrase in phrases:
                    if phrase:
                        phrases_with_topics.append((topic, phrase.upper()))
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file_name}' not found.")
    return phrases_with_topics

def main():
    # Main function to run the game
    file_name = "listofphrases.xlsx"  # Make sure this file exists
    phrases = read_phrases_from_excel(file_name)
    if phrases:
        root = tk.Tk()
        root.title("Phrase of Fortune")  # Set the title of the window

        # Create GUI frames for players
        frame1 = tk.Frame(root, bg="blue")
        frame1.pack(side=tk.LEFT, padx=10)
        PhraseGuessingGameGUI.player1_game = PhraseGuessingGameGUI(frame1, "Player 1", phrases, "blue")
        PhraseGuessingGameGUI.player1_game.current_player = "Player 1"
        PhraseGuessingGameGUI.player1_game.create_widgets()

        frame2 = tk.Frame(root, bg="red")
        frame2.pack(side=tk.RIGHT, padx=10)
        PhraseGuessingGameGUI.player2_game = PhraseGuessingGameGUI(frame2, "Player 2", phrases, "red")
        PhraseGuessingGameGUI.player2_game.current_player = "Player 2"
        PhraseGuessingGameGUI.player2_game.create_widgets()

        root.mainloop()

if __name__ == "__main__":
    main()
