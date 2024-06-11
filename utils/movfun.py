movies = []

def create_movie_list():
    pass

def show_movies():
    return movies

def add_movie(title, director, year, rating):
    movies.append({
        'title':title, 
        'director':director,
        'year':year,
        'rating':rating,
        'watched':False
        })
    
def movie_watched(title):
    for movie in movies:
        if movie.get('title') == title:
            movie['watched'] = True

            
find_choice = """
Enter:
t -> title
d -> director
y -> year
r -> rating
q -> come out of searching
your choice: 
"""
def find_movie():
    find_input = input(find_choice)
    while find_input != 'q':
        if find_input == 't':
            title = input("Enter the title: ")
            for movie in movies:
                seen = 'Yes' if movie['watched'] else 'No'
                tl = str(movie.get("title"))
                check = tl.find(title)
                if check != -1:
                    print(f"{movie['title']} directed by {movie['director']} in {movie['year']} imdb rating: {movie['rating']} - watched: {seen}")
        
        elif find_input == 'd':
            director = input("Enter the director name: ")
            for movie in movies:
                seen = 'Yes' if movie['watched'] else 'No'
                dr = str(movie.get("director"))
                check = dr.find(director)
                if check != -1:
                    print(f"{movie['title']} directed by {movie['director']} in {movie['year']} imdb rating: {movie['rating']} - watched: {seen}")
        elif find_input == 'y':
            year = input("Enter the year: ")
            for movie in movies:
                seen = 'Yes' if movie['watched'] else 'No'
                if movie.get('year') == year:
                    print(f"{movie['title']} directed by {movie['director']} in {movie['year']} imdb rating: {movie['rating']} - watched: {seen}")
                    
        elif find_input == 'r':
            rating = input("Enter the rating: ")
            for movie in movies:
                seen = 'Yes' if movie['watched'] else 'No'
                if movie.get('rating') == rating:
                    print(f"{movie['title']} directed by {movie['director']} in {movie['year']} imdb rating: {movie['rating']} - watched: {seen}")

        find_input = input(find_choice)
        

def delete_movie(title):
    global movies
    movies = [movie for movie in movies if movie.get('title') != title]

update_choice = """
Enter:
t->title
d->director
y->year
r->rating
q-> update done
Your choice: """   
def update_movie(title):
    for movie in movies:
        if movie.get('title') == title:
            update_input = input(update_choice)
            while update_input != 'q':
                if update_input == 't':
                    movie['title'] = input("Enter the new title for the movie: ")
                elif update_input == 'd':
                    movie['director'] = input("Enter the new director for the movie: ")
                elif update_input == 'y':
                    movie['year'] = input("Enter the new year for the movie: ")
                elif update_input == 'r':
                    movie['rating'] = input("Enter the new rating for the movie: ")
                update_input = input(update_choice)
                
def clear_all_movies():
    movies.clear()
