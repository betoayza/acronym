text = input("Welcome to Find the Acronym!\nEnter a phrase: [-1 to exit]: ")

while(text != "-1"):
    words_list = text.split()

    acronym = ""
    for i in range(0, len(words_list)):       
        acronym += words_list[i][0].capitalize()

    print("The acronym is:", acronym) 

    text = input("\nEnter other phrase: ")

print("Thanks, see on!")


