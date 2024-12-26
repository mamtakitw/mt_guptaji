import tkinter as tk
from tkinter import messagebox
from PyDictionary import PyDictionary
from googletrans import Translator, LANGUAGES
import random
import threading

dictionary = PyDictionary()
translator_service = Translator()

def cls():
    pass  # This function is not needed in a GUI context

def main_menu():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("Literary Hub")
    root.configure(bg='lightblue')

    tk.Label(root, text="WELCOME HUMAN", font=("Helvetica", 24, "bold"), bg='lightblue').pack(pady=(30, 10))
    tk.Label(root, text="How would you like to waste your time today?", font=("Helvetica", 16), bg='lightblue').pack(pady=10)

    button_frame = tk.Frame(root, bg='lightblue')
    button_frame.pack(pady=20)
    
    buttons = [
        ("Play Hangman", hangman_game),
        ("Play Word Scramble", word_scramble),
        ("Dictionary", dictionary_feature),
        ("Translator", translator)
    ]
    
    for (text, command) in buttons:
        tk.Button(button_frame, text=text, command=command, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)

def hangman_game():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("Hangman")
    
    guessed_word = []
    guesses = ""
    wrong_guesses = []
    turns = 10
    words = [
        "Forrest Gump",
        "Hangman Project",
        "The Godfather",
        "The Green Mile",
        "Hotel Rwanda",
        "Goodfellas",
        "Scarface",
        "The Terminal",
        "Million Dollar Baby",
        "Driving Miss Daisy",
        "Catch Me If You Can",
        "Chinatown",
        "The Departed",
        "Dances with Wolves",
        "Ford v Ferrari",
        "Little Women",
        "A Star Is Born",
        "Dear Basketball"
    ]
    word = random.choice(words).upper()

    def update_display():
        display_word = ""
        failed = 0
        for char in word:
            if char in guesses:
                display_word += char + " "
            elif char == " ":
                display_word += '/ '
            else:
                display_word += "_ "
                failed += 1
        word_label.config(text=display_word.strip())
        if failed == 0:
            result_label.config(text="You WON! :)")
            guess_button.config(state=tk.DISABLED)
        if turns_label.cget("text") == "Turns left: 0":
            result_label.config(text=f"Game is OVER, you LOST :o\nThe word was '{word}'.")
            guess_button.config(state=tk.DISABLED)

    def guess_letter():
        nonlocal turns, guesses
        guess = guess_entry.get().upper()
        guess_entry.delete(0, tk.END)
        if not guess.isalpha() or len(guess) != 1:
            messagebox.showerror("Invalid input", "Please enter a single letter. Numbers are invalid.")
            return
        if guess in guessed_word:
            messagebox.showinfo("Duplicate input", "You have already guessed that letter.")
            return
        guessed_word.append(guess)
        guesses += guess
        if guess not in word:
            turns -= 1
            wrong_guesses.append(guess)
            turns_label.config(text=f"Turns left: {turns}")
            wrong_guesses_label.config(text=f"Wrong guesses: {', '.join(wrong_guesses)}")
        update_display()

    word_label = tk.Label(root, font=("Helvetica", 18), bg='lightblue')
    word_label.pack(pady=10)
    guess_entry = tk.Entry(root, font=("Helvetica", 14))
    guess_entry.pack(pady=10)
    guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Helvetica", 14), bg='lightgray')
    guess_button.pack(pady=10)
    turns_label = tk.Label(root, text=f"Turns left: {turns}", font=("Helvetica", 14), bg='lightblue')
    turns_label.pack(pady=10)
    wrong_guesses_label = tk.Label(root, text="Wrong guesses: ", font=("Helvetica", 14), bg='lightblue')
    wrong_guesses_label.pack(pady=10)
    result_label = tk.Label(root, font=("Helvetica", 16), bg='lightblue')
    result_label.pack(pady=10)
    tk.Button(root, text="Back to Main Menu", command=main_menu, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    tk.Button(root, text="Play Again", command=hangman_game, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    
    update_display()

def word_scramble():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("Word Scramble")
    
    words = ["python", "scramble", "literature", "enthusiast", "dictionary", "challenge", "programming", "interface", "algorithm"]
    word = random.choice(words)
    scrambled_word = "".join(random.sample(word, len(word)))

    def check_answer():
        user_input = entry.get().strip().lower()
        if not user_input:
            result.set("Please enter a word.")
            return
        if user_input == word:
            result.set("Correct!")
        else:
            result.set("Try again!")

    def show_hint():
        result.set(f"Hint: The first letter is '{word[0]}'")

    def show_answer():
        result.set(f"The correct answer is: {word}")

    tk.Label(root, text=f"Unscramble the word: {scrambled_word}", font=("Helvetica", 16), bg='lightblue').pack(pady=20)
    entry = tk.Entry(root, font=("Helvetica", 14))
    entry.pack(pady=10)
    tk.Button(root, text="Submit", command=check_answer, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    result = tk.StringVar()
    tk.Label(root, textvariable=result, font=("Helvetica", 14), bg='lightblue').pack(pady=10)
    tk.Button(root, text="Hint", command=show_hint, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    tk.Button(root, text="Show Answer", command=show_answer, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    tk.Button(root, text="Back to Main Menu", command=main_menu, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    tk.Button(root, text="Play Again", command=word_scramble, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)

def dictionary_feature():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("Dictionary")

    def lookup_word():
        word = entry.get()
        if not word:
            messagebox.showerror("Invalid input", "Please enter a word.")
            return
        result_label.config(text="Looking up...")
        def fetch_data():
            try:
                meaning = dictionary.meaning(word)
                synonym = dictionary.synonym(word)
                antonym = dictionary.antonym(word)
                result = f"Meaning: {meaning}\nSynonyms: {synonym}\nAntonyms: {antonym}" if meaning else "Word not found"
                result_label.config(text=result)
            except Exception as e:
                result_label.config(text=f"Error: {e}")
        threading.Thread(target=fetch_data).start()

    tk.Label(root, text="Enter a word:", font=("Helvetica", 16), bg='lightblue').pack(pady=10)
    entry = tk.Entry(root, font=("Helvetica", 14))
    entry.pack(pady=10)
    tk.Button(root, text="Look up", command=lookup_word, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    result_label = tk.Label(root, font=("Helvetica", 14), bg='lightblue', wraplength=500)
    result_label.pack(pady=10)
    tk.Button(root, text="Back to Main Menu", command=main_menu, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    tk.Button(root, text="Use Again", command=dictionary_feature, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)

def translator():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("Translator")

    def translate_word():
        word = entry.get()
        lang = lang_entry.get()
        if not word or not lang:
            messagebox.showerror("Invalid input", "Please enter a word and a language code.")
            return
        result_label.config(text="Translating...")
        def fetch_translation():
            try:
                translation = translator_service.translate(word, dest=lang)
                result_label.config(text=f"Translation: {translation.text}")
            except Exception as e:
                result_label.config(text=f"Error: {e}")
        threading.Thread(target=fetch_translation).start()

    tk.Label(root, text="Enter a word:", font=("Helvetica", 16), bg='lightblue').pack(pady=10)
    entry = tk.Entry(root, font=("Helvetica", 14))
    entry.pack(pady=10)
    tk.Label(root, text="Enter language code (ur, ar, hi, it, es, ko, ja, zh-cn):", font=("Helvetica", 14), bg='lightblue').pack(pady=10)
    lang_entry = tk.Entry(root, font=("Helvetica", 14))
    lang_entry.pack(pady=10)
    tk.Button(root, text="Translate", command=translate_word, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    result_label = tk.Label(root, font=("Helvetica", 14), bg='lightblue')
    result_label.pack(pady=10)
    tk.Button(root, text="Back to Main Menu", command=main_menu, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)
    tk.Button(root, text="Use Again", command=translator, font=("Helvetica", 14), bg='lightgray', width=20, height=2).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='lightblue')
    main_menu()
    root.mainloop()