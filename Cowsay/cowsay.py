#words = userText.split() Utilizado para quebrar o texto em várias linhas quando for muito grande. Split é método dividir que basicamente faz com que transforme o texto em uma lista de strings com cada palavra separadamente, ele pega onde tem espaço vázio e quebra a linha sem cortar uma palavra ao meio e separa palavra por palavra.

userText = input("Digite uma fala para a vaquinha: ")
words = userText.split()

if len(words) > 8:
    firstLine = " ".join(words[:len(words)//2 + 1])
    secondLine = " ".join(words[len(words)//2 + 1:])
    line = (len(firstLine) + 4) * "-"
    padding = (len(firstLine) - len(secondLine)) * " "
    content = "| " + firstLine + " |\n| " + secondLine + padding + " |"
else:
    line = (len(userText) + 4) * "-"
    content = "| " + userText + " |"
    

container = [line, content, line]

for item in container:
    print(item)

#Lista de Strings - ARRAY DE 5 LINHAS
cow = ["          \\  ^__^",
"           \\ (oo)\\________",
"             (__)\\        )\\/\\",
"                  ||----w |",
"                  ||     ||"]

for item in cow:
    print(item)