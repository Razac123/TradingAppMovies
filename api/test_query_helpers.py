# %%
from database import SessionLocal
from query_helpers import *

# Créer une session
db = SessionLocal()

#movie = get_movie(db, movie_id=1)
#print(movie.title, movie.genres)

#movies = get_movies(db, limit=7)
#for film in movies:
#    print(f"ID : {film.movieId}, Titre : {film.title}, Genres : {film.genres}") 
 
#rating = get_rating(db, movie_id=1, user_id=1)
#print(f"User ID : {rating.userId}, Movie ID : {rating.movieId}, Rating : {rating.rating}, Timestamp : {rating.timestamp}")  

#resultat none: car aucune donnée ne correspond aux critères, 
#tag = get_tag(db, user_id=2, movie_id=60000, tag_text="funny") 
#print(tag)
#print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}, Timestamp : {tag.timestamp}")    

#tag = get_tag(db, user_id=2, movie_id=60756, tag_text="funny") 
#print(tag)
#print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}, Timestamp : {tag.timestamp}")    
      
#tester le nombre d'évaluation
#n_movies = get_movie_count(db)
#print(f"Nombre total de films : {n_movies}")

#tester le nombre d'évaluation
n_movies = get_rating_count(db)
print(f"Nombre total d'évaluations : {n_movies}")

    
db.close()

# %%
