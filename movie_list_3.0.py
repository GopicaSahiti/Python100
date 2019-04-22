
import pickle

FILENAME = "movies.bin"


def write_movies(movies):
    with open(FILENAME, "wb") as file:
        pickle.dump(movies, file)

def read_movies():
    movies = []
    with open(FILENAME, "rb") as file:
        movies = pickle.load(file)
    return movies

def list_movies (movies): 
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i+1) + ". " + movie[0] + "(" + str(movie[1]) + ")") 
    print ()

def add_movie (movies):
    name = input("Name:") 
    year = input("Year:")
    movie = []
    movie.append(name)
    movie.append(year)
    movies.append(movie) 
    write_movies(movies) 
    print(movie[0] + " was added. \n")

def delete_movie (movies):
    index = int(input ("Number: ")) 
    movie = movies.pop (index - 1) 
    write_movies(movies) 
    print(movie[0] + " was deleted. \n")

def display_menu():
    print("The Movie List program") 
    print() 
    print("COMMAND MENU") 
    print("list - List all movies") 
    print("add - Add a movie") 
    print("del - Delete a movie") 
    print("exit - Exit program") 
    print()

def main():
    display_menu() 
    movies = read_movies() 
    while True:
        command = input ("Command: ") 
        if command.lower() == "list":
            list_movies(movies) 
        elif command.lower() == "add":
            add_movie(movies) 
        elif command.lower() == "del":
            delete_movie(movies) 
        elif command.lower() == "exit":
            break 
        else:
            print("Not a valid command. Please try again.")
    print("Bye!")

if __name__ == "__main__":
    main()
