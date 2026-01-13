import random

# -------------------------------
# Load words from file
# -------------------------------
def load_words(filename):
    try:
        with open(filename, "r") as file:
            words = [word.strip().lower() for word in file if word.strip()]
        return words
    except FileNotFoundError:
        print("Word file not found!")
        return []

# -------------------------------
# Choose word based on difficulty
# -------------------------------
def choose_word(words, difficulty):
    if difficulty == "easy":
        filtered = [w for w in words if len(w) <= 5]
    elif difficulty == "medium":
        filtered = [w for w in words if 6 <= len(w) <= 8]
    else:
        filtered = [w for w in words if len(w) > 8]

    return random.choice(filtered)

# -------------------------------
# Display current word state
# -------------------------------
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# -------------------------------
# Main game logic
# -------------------------------
def play_game():
    words = load_words("words.txt")
    if not words:
        return

    print("\n🎮 WELCOME TO HANGMAN 🎮")
    print("Choose difficulty: easy / medium / hard")

    difficulty = input("Enter difficulty: ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Invalid choice. Enter again: ").lower()

    word = choose_word(words, difficulty)
    guessed_letters = set()
    lives = 6
    score = 0

    print("\nGame started! Guess the word.\n")

    while lives > 0:
        print("Word:", display_word(word, guessed_letters))
        print(f"Lives left: {lives}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single alphabet only.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct guess!\n")
            score += 10
        else:
            print("❌ Wrong guess!\n")
            lives -= 1
            score -= 5

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 CONGRATULATIONS! YOU WON 🎉")
            print(f"The word was: {word}")
            print(f"Your score: {score}")
            return

    print("\n💀 GAME OVER 💀")
    print(f"The word was: {word}")
    print(f"Your final score: {score}")

# -------------------------------
# Replay option
# -------------------------------
def main():
    while True:
        play_game()
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("\nThanks for playing! 👋")
            break

# -------------------------------
# Program entry point
# -------------------------------
if __name__ == "__main__":
    main()
