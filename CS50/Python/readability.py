from cs50 import get_string

# Get input text from user
text = get_string("Text: ")

# Initialize counters
letters = 0
words = 1  # Start at 1 because last word won't have space after it
sentences = 0

# Loop through each character in the text
for c in text:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        words += 1
    elif c in ['.', '!', '?']:
        sentences += 1

# Calculate L and S for Coleman-Liau index
L = (letters / words) * 100
S = (sentences / words) * 100

# Compute grade level
index = round(0.0588 * L - 0.296 * S - 15.8)

# Output result based on grade
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
