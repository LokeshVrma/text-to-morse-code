data = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

keys = list(data.keys())
vals = list(data.values())

print("             Text To Morse Code")
user_choice = input("Press M to morse text: ").lower()

if user_choice == "m":
    user_input = input("Enter Some Text: ")
    user_input_without_whitespace = user_input.replace(" ", "")
    user_input_list = list(user_input_without_whitespace)
    # print(user_input_list)


    morse_code = ""
    morse_code_list = []

    for word in user_input_list:
        morse_code += data[word]
        morse_code_list.append(data[word])

    print(f"Morse Code is: {morse_code}")
    ch = input("Do You want to Decode it? y/n" ).lower()

    if ch == "y":
        org_text = ""
        for code in morse_code_list:
            org_text += (keys[vals.index(code)])

        print(f"Original Text is: {org_text}")
    else:
        print("Bye!")

