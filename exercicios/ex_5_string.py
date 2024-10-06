string = "Escreva um programa que inverta os caracteres de um string." # String a inverter

# string_invertida = string[::-1]

string_invertida = ""

for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

print(string_invertida)
