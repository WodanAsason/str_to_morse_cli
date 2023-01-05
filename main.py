import pandas as pd

# Basic morse CSV
morse_lookup = pd.read_csv('data/morse.csv', index_col=0)

# Assignment operator for brevity, to uppercase, strip spaces
while (user_input := input("Enter a string to convert (or q to quit):\n").upper().replace(' ', '')) != 'Q':
    # No special chars in morse
    if not user_input.isalnum():
        print("Only alphanumeric characters are allowed!")
        continue
    out = ''
    for letter in user_input:
        # Added spaces for legibility, wouldn't be there in a real use-case
        out += morse_lookup.loc[letter].code + ' '
    print(f"{user_input} to Morse is: {out}")
