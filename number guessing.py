import tkinter as tk
import random

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guess the Number")

        # Create a secret number
        self.secret_number = random.randint(1, 100)

        # Create a label to display the message
        self.message_label = tk.Label(self.window, text="Guess a number between 1 and 100!")
        self.message_label.pack()

        # Create an entry field for the user's guess
        self.guess_entry = tk.Entry(self.window)
        self.guess_entry.pack()

        # Create a button to submit the guess
        self.guess_button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        # Create a label to display the result
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        # Create a label to display the number of attempts
        self.attempts_label = tk.Label(self.window, text="Attempts: 0")
        self.attempts_label.pack()

        # Initialize the number of attempts
        self.attempts = 0

    def check_guess(self):
        # Get the user's guess
        user_guess = int(self.guess_entry.get())

        # Check if the number of attempts has reached the limit
        if self.attempts >= 8:
            self.result_label.config(text="You've reached the maximum number of attempts! Game over.")
            self.guess_button.config(state="disabled")  # Disable the guess button
        else:
            # Increment the number of attempts
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")

            # Check if the guess is correct
            if user_guess == self.secret_number:
                self.result_label.config(text=" Congratulations! You guessed it!")
                self.guess_button.config(state="disabled")  # Disable the guess button
            elif user_guess > self.secret_number:
                self.result_label.config(text="Your guess is too high! Try again.")
            else:
                self.result_label.config(text="Your guess is too low! Try again.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Game()
    game.run()