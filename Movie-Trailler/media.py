#Import high level python module //webbrowser
import webbrowser    #Allows use of open() function to open a web browser

class Movie():    #This class provdies a way to store movie info

    #Initializes instances of the class Movie_Media
    def __init__(self, movie_title, audience_rating, reviews_link,
                 poster_image, trailer_youtube, age_restriction):
        self.title = movie_title
        self.rating = audience_rating
        self.link = reviews_link
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.restriction = age_restriction

    #Initialize the play trailer function within class Movie_Media
    def play_trailer(self):
        #Uses webbrowsers open() function to display specifc youtube trailer
        webbrowser.open(self.trailer_youtube_url)
