from utils import movfun

user_choice = """"
Enter:
- 'a' to add new movie
- 'l' to list all movies
- 'w' to mark a movie as watched
- 'f' to find a movie
- 'u' to update a movie
- 'd' to delete a movie
- 'c' to clear all movies
- 'q' to quit
Your choice: 
"""

def prompt_add_movie():
    title = input("Enter the Movie title:")
    director = input("Enter the movie director:")
    year = input("Enter the movie release year: ")
    rating = input("Enter the movie rating: ")
    
    movfun.add_movie(title, director, year, rating)
    
def prompt_list_movies():
    for movie in movfun.show_movies():
        seen = 'Yes' if movie['watched'] else 'No'
        print(f"{movie['title']} directed by {movie['director']} in {movie['year']} imdb rating: {movie['rating']} - watched: {seen}")
    
def prompt_watched_movie():
    title = input('Enter the name of movie you watched: ')
    
    movfun.movie_watched(title)
    
def prompt_find_movie(): 
    movfun.find_movie()
    
def prompt_update_movie():
    title = input('Enter the name of movie you want to update: ')
    
    movfun.update_movie(title)
    
def prompt_delete_movie():
    title = input('Enter the name of movie you want to delete: ')

    movfun.delete_movie(title)
    
def prompt_clear_all_movies():
    movfun.clear_all_movies()
    
user_options={
    'a': prompt_add_movie,
    'l': prompt_list_movies,
    'w': prompt_watched_movie,
    'f': prompt_find_movie,
    'u': prompt_update_movie,
    'd': prompt_delete_movie,
    'c': prompt_clear_all_movies
    }
def menu():
    selection = input(user_choice)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command, Please try again!')
        selection = input(user_choice)
        
menu()
            
            
    
        
    
