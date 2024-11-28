def write_input():
    with open ("Ukoly/Ukol_2/04_files.txt", mode = "a", encoding= "utf-8") as file:
        text = input("zadejte text:")
        file.write(text)
write_input()