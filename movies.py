import popcorn  #import popcorn file to work with movies.py
import media    #import media file to work with movies.py


# Create multiple instances of the class Movie.                   
ip_man = media.Movie("Ip Man",
                    "93%",
                    "https://www.rottentomatoes.com/m/ip_man",
                    "https://upload.wikimedia.org/wikipedia/en/2/2f/Ipmanposter02.jpg",
                    "https://www.youtube.com/watch?v=1AJxXQ7xojE",
                    "R")

avatar = media.Movie("Avatar",
                     "83%",
                     "https://www.rottentomatoes.com/m/avatar",
                     "http://image.tmdb.org/t/p/original/bjVECh2nMOT2s2ThYOrmdTFVWeV.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io",
                     "PG-13")

ice_age = media.Movie("Ice Age",
                      "82%",
                      "https://www.rottentomatoes.com/m/ice_age",
                      "https://upload.wikimedia.org/wikipedia/en/3/3c/Ice_Age_%282002_film%29_poster.jpg",
                      "https://www.youtube.com/watch?v=cMfeWyVBidk",
                      "PG")

the_kings_speech = media.Movie("The Kings Speech",
                       "92%",
                       "https://www.rottentomatoes.com/m/the_kings_speech",        
                       "https://ia.media-imdb.com/images/M/MV5BMzU5MjEwMTg2Nl5BMl5BanBnXkFtZTcwNzM3MTYxNA@@._V1_SY1000_CR0,0,684,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=kYoSQkfrjfA",
                       "PG-13")

the_dark_knight = media.Movie("The Dark Knight",
                       "94%",
                       "https://www.rottentomatoes.com/m/the_dark_knight",       
                       "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                       "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                       "PG-13")

harry_potter = media.Movie("Harry Potter",
                       "82%",
                       "https://www.rottentomatoes.com/m/harry_potter_and_the_sorcerers_stone",    
                       "https://vignette.wikia.nocookie.net/harrypotter/images/0/0e/Philostone.jpg/revision/latest/scale-to-width-down/1000?cb=20180318153750",
                       "https://www.youtube.com/watch?v=VyHV0BRtdxo",
                       "PG")

big_fish = media.Movie("Big Fish",
                       "89%",
                       "https://www.rottentomatoes.com/m/1127787_big_fish?",
                       "https://upload.wikimedia.org/wikipedia/en/4/41/Big_Fish_movie_poster.png",
                       "https://www.youtube.com/watch?v=M3YVTgTl-F0",
                       "PG-13")

rush_hour = media.Movie("Rush Hour",
                       "78%",
                       "https://www.rottentomatoes.com/m/rush_hour",
                       "https://ia.media-imdb.com/images/M/MV5BYWM2NDZmYmYtNzlmZC00M2MyLWJmOGUtMjhiYmQ2OGU1YTE1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,678,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=JMiFsFQcFLE",
                       "PG-13")

wall_e = media.Movie("WALL-E",
                       "89%",
                       "https://www.rottentomatoes.com/m/wall_e",
                       "https://ia.media-imdb.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=8-_9n5DtKOc",
                       "G")

three_hundred = media.Movie("300",
                       "89%",
                       "https://www.rottentomatoes.com/m/300",
                       "https://ia.media-imdb.com/images/M/MV5BMjAzNTkzNjcxNl5BMl5BanBnXkFtZTYwNDA4NjE3._V1_.jpg",
                       "https://www.youtube.com/watch?v=UrIbxk7idYA",
                       "R")

mean_girls = media.Movie("Mean Girls",
                       "66%",
                       "https://www.rottentomatoes.com/m/mean_girls",
                       "https://ia.media-imdb.com/images/M/MV5BMjE1MDQ4MjI1OV5BMl5BanBnXkFtZTcwNzcwODAzMw@@._V1_SY1000_CR0,0,706,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=KAOmTMCtGkI",
                       "PG-13")

slumdog_millionaire = media.Movie("Slumdog Millionaire",
                       "90%",
                       "https://www.rottentomatoes.com/m/slumdog_millionaire",
                       "https://ia.media-imdb.com/images/M/MV5BZmNjZWI3NzktYWI1Mi00OTAyLWJkNTYtMzUwYTFlZDA0Y2UwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=AIzbwV7on6Q",
                       "R")

#List instance name of every movie to be visible on website
movies = [
    ip_man,
    avatar,
    harry_potter,
    ice_age,    
    the_kings_speech,
    the_dark_knight,
    big_fish,
    rush_hour,
    wall_e,
    three_hundred,
    mean_girls,
    slumdog_millionaire    
]

#Opens popcorn file to dispaly movie trailer page
popcorn.open_movies_page(movies)
