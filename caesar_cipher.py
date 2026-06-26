def caesar_cipher(text, shift, mode):
    result = ""
    
    # Ensure the shift stays within the 0-25 range
    shift = shift % 26
    
    # If we are decrypting, we invert the shift direction
    if mode == "decrypt":
        shift = -shift
        
    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            # ord() gets the ASCII value, 65 is 'A'
            ascii_offset = 65
            processed_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += processed_char
            
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            # 97 is 'a'
            ascii_offset = 97
            processed_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += processed_char
            
        else:
            # Leave spaces, numbers, and symbols untouched
            result += char
            
    return result

# --- Main Program Loop ---
print("=== Cybersecurity Tools: Caesar Cipher ===")

while True:
    choice = input("\nWould you like to (E)ncrypt, (D)ecrypt, or (Q)uit?: ").lower()
    
    if choice == 'q':
        print("Exiting tool. Stay secure!")
        break
        
    if choice in ['e', 'd']:
        user_message = input("Enter your message: ")
        
        # Validate that the shift is an integer
        try:
            user_shift = int(input("Enter the shift key (number): "))
        except ValueError:
            print("❌ Invalid shift key. Please enter a whole number.")
            continue
            
        if choice == 'e':
            encrypted_text = caesar_cipher(user_message, user_shift, mode="encrypt")
            print(f"\n🔒 Ciphertext: {encrypted_text}")
        else:
            decrypted_text = caesar_cipher(user_message, user_shift, mode="decrypt")
            print(f"\n🔓 Plaintext: {decrypted_text}")
    else:
        print("❌ Invalid option. Please select E, D, or Q.")