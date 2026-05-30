with open("data.txt", "a") as file:
    file.write("Hello, M Saqib Khan\n")

with open("data.txt", "a") as file:
    file.write("Hello, World!")


with open("data.txt", "r") as file:
    content = file.read()
    print(content)

    