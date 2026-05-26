import itertools
import string

def generate_combinations(length):
    # Choose your character set (lowercase, digits, etc.)
    chars = string.ascii_lowercase + string.digits
    
    # Generate all possible combinations for a specific length
    for attempt in itertools.product(chars, repeat=length):
        password = ''.join(attempt)
        print(password) # Replace this with your 'check_password' function

# To try lengths 1 through 4
for i in range(1, 21):
    generate_combinations(i)
