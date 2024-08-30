def calculate_love_score(name1, name2):
    # Convert both names to lowercase to make the counting case-insensitive
    combined_names = (name1 + name2).lower()

    # Count the occurrences of the letters in the word "TRUE"
    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)

    # Count the occurrences of the letters in the word "LOVE"
    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    # Combine the counts to create a 2-digit love score
    love_score = int(str(true_count) + str(love_count))

    print(f"Love Score = {love_score}")
    return love_score


# Example usage
calculate_love_score("Kanye West", "Kim Kardashian")
