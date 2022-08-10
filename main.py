import random

def convert_list_to_str(list):
    str1= " "

    return (str1.join(list))



print("-"*30)
print("Bienvenido al juego del ahorcado")
print("-"*30)

with open("./words.txt",encoding="utf-8") as f:
    words = [i.replace('\n','') for i in f]

random_word = list(words[random.randint(0,len(words))])

lines = list("_"*len(random_word))

print(convert_list_to_str(lines))

final_word = ""
for i in random_word:
    final_word += i


tries = 8

while tries > 0:
    selected_letter = input(f"Adivina la palabra... tienes {tries} intentos")
    if selected_letter in random_word:
        for idx, letter in enumerate(random_word):
            if selected_letter == letter:
                lines[idx] = letter
    else:
        tries -= 1
    print(convert_list_to_str(lines))

    if "_" not in lines:
        print("Ganaste!!!, la palabra es "+ final_word)
        break

if tries == 0:
    print(f"Perdiste"" :( ..... La palabra era " + final_word)