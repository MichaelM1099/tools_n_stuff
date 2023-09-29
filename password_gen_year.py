def generate_wordlist(base_word, year):
    permutations = [
        f"{base_word.capitalize()}{year}",
        f"{base_word.capitalize()}{year}!",
        f"{base_word.capitalize()}{year}@",
        f"{base_word.capitalize()}{year}#",
    ]
    return permutations

if __name__ == '__main__':
    input_words = input("Enter the base words separated by commas: ").split(',')
    year = input("Enter the year: ")

    with open('wordlist.txt', 'w') as file:
        for word in input_words:
            word = word.strip()  # Remove leading/trailing spaces
            word_permutations = generate_wordlist(word, year)
            for item in word_permutations:
                file.write(item + '\n')
