import requests

def get_movie_recommendations(genre):
    api_key = "movie2541" 
    url = f"http://www.omdbapi.com/?s=&type=movie&apikey={api_key}&t={genre}"
    response = requests.get(url)
    data = response.json()
    return data.get("Search", [])

def display_movie_details(movie):
    print("Title:", movie.get("Title"))
    print("Year:", movie.get("Year"))
    print("Genre:", movie.get("Genre"))
   

def main():
    genre = input("Enter your preferred movie genre: ")
    movies = get_movie_recommendations(genre)
    
    if movies:
        print(f"Here are some {genre} movie recommendations:")
        for movie in movies:
            display_movie_details(movie)
    else:
        print("No movies found for the given genre.")

if __name__ == "__main__":
    main()
