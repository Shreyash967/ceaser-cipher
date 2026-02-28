alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' '
]
def encrypt(text,shift):
    encrypted_text= ""
    for i in range (len(text)):
        if text[i] not in alphabet_list:
            encrypted_text += text[i]
        elif text[i] in alphabet_list:
            shifted_amount=alphabet_list.index(text[i]) + shift
            shifted_amount %= len(alphabet_list)
            encrypted_text+=alphabet_list[shifted_amount]
        else:
            pass
    print(f"Encrypted Message : {encrypted_text}")

def decrypt(text,shift):
    decrypted_text= ""
    for i in range (len(text)):
        if text[i] not in alphabet_list:
            decrypted_text += text[i]
        elif text[i] in alphabet_list:
            shifted_amount = alphabet_list.index(text[i]) - shift
            shifted_amount %= len(alphabet_list)
            decrypted_text += alphabet_list[shifted_amount]
        else:
            pass
    print(f"Decrypted Message : {decrypted_text}")

print("""
  ____                                  ____ _       _               
 / ___|__ _  ___  ___  __ _ _ __       / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__|     | |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |     _  | |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\__,_|_|    (_)  \____|_| .__/|_| |_|\___|_|   
                                              |_|                    
""")
should_condition=True
while should_condition:
    direction = input("Type Encode To encrypt The Msg or type Decode To decrypt the received msg\n :").lower()
    text = input("Enter Your message (Don't Give space in between) \n :").lower()
    shift = int(input("Enter your shift\n :"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input")
    restart = input("Press 'Y' if you want to continue or 'N' to exit\n :").lower()
    if restart != "y":
        print("Thank You")
        should_condition = False


