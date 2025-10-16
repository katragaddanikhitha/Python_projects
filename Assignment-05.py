'''
Student Name: K. Nikhitha
Student Id: 00983208
course: CSCI6651 Introduction to Python Programming
Git Repository: https://github.com/katragaddanikhitha/Python_projects

'''
def main():
    # Given cipher text
    cipher_text = "L#dp#kdylqj#d#juhdw#wlph#lq#FVFL/9984$##Surihvvru#Dqwrqhwwl#lv#d#Frrs#Ndw$"

    # Convert to lowercase for frequency analysis
    text_lower = cipher_text.lower()

    # Step 1: Count frequency manually
    freq_list = []
    for ch in text_lower:
        found = False
        for pair in freq_list:
            if pair[0] == ch:
                pair[1] += 1
                found = True
                break
        if not found:
            freq_list.append([ch, 1])

    # Step 2: Convert list of lists to list of tuples
    freq_list = [(pair[0], pair[1]) for pair in freq_list]

    # Step 3: Sort frequency descending by count
    n = len(freq_list)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if freq_list[j][1] > freq_list[i][1]:
                freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

    # Step 4: Display frequency analysis
    print(f"\nCipher Text = {cipher_text}")
    print(f"\nCharacter Frequency Analysis (character, count):")
    for ch, count in freq_list:
        display_char = "Space" if ch == " " else ch
        print(f"{display_char} count: {count}")
    print("-" * 50)

    # Step 5: Try all Caesar Cipher shifts (brute-force)
    print("\nTrying all Caesar Cipher shifts:")
    for shift in range(26):
        result = ""  # Store decrypted result for this shift

        # Lists of uppercase and lowercase letters
        uppercase_letters = [chr(i) for i in range(65, 91)]
        lowercase_letters = [chr(i) for i in range(97, 123)]

        # Decrypt character by character
        for char in cipher_text:
            if char in uppercase_letters:
                pos = uppercase_letters.index(char)
                new_pos = (pos - shift) % 26
                result += uppercase_letters[new_pos]
            elif char in lowercase_letters:
                pos = lowercase_letters.index(char)
                new_pos = (pos - shift) % 26
                result += lowercase_letters[new_pos]
            else:
                result += char  # Keep symbols/numbers unchanged

        print(f"Shift {shift}: {result}")

if __name__ == "__main__":
    main()
