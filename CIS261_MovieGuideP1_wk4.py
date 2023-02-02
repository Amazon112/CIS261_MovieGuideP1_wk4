def display_menu():
    #Print available commands
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print("\n")
def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n") #if no of movie =0
        return
    else:
        i=1

        for movie in movie_list:
            print(str(i) + ". " +movie ) # i is printed like sl no
            i+=1
    print("\n")
def add(movie_list):

    name = input("Name: ")
    movie_list.append(name)
    print(name+ " was added.\n")


def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
        return
    else:
        movie = movie_list.pop(number-1)
    print(movie+" was deleted")


movie_list = ["Monty Python and the Holy Grail","On the Waterfront","Cat on a Hot Tin Roof"] #Initialize with 3 movie name

print("The Movie List Program")
display_menu()
while True:
    command = input("Command: ")
    if command == "list":
        list(movie_list)
    elif command == "add":
        add(movie_list)
    elif command == "del":
        delete(movie_list)
    elif command == "exit":
        break
    else:
        print("Not a valid command. Please try again.\n")
print("Bye!")

