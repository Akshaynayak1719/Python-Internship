# Secret Code Generator
# Function to encode a message
def encode_message(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = ord('A') if char.isupper() else ord('a')  # Handle uppercase and lowercase
            encoded_message += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encoded_message += char  # Keep spaces and punctuation unchanged
    return encoded_message

# Function to decode a message
def decode_message(message, shift):
    return encode_message(message, -shift)  # Decoding is just encoding with a negative shift

# Function to handle the menu and user choices
def menu():
    while True:
        print("\nSecret Code Generator")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            message = input("Enter the message to encode: ")
            shift = get_valid_shift()
            encoded_message = encode_message(message, shift)
            print(f"Encoded message: {encoded_message}")
        
        elif choice == '2':
            message = input("Enter the message to decode: ")
            shift = get_valid_shift()
            decoded_message = decode_message(message, shift)
            print(f"Decoded message: {decoded_message}")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

# Function to validate and return the shift number
def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter the shift number: "))
            return shift
        except ValueError:
            print("Please enter a valid integer for the shift.")

# Main function
if _name_ == "_main_":
    menu()
