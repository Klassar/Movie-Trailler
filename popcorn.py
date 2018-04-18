import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Popcorn Trailers</title>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>

    <style type="text/css" media="screen">

        /************  Base Styles ************/ 
        html {
            padding: 0;
            margin: 0;
        }       
        body {
            padding: 3em 0 0.5em 0;
            margin: inherit;
            background-image: url("https://www-cdn01.tivo.com/sites/all/themes/tivo3/images/shows_two_discover.jpg");
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center; 
            background-size: cover;
        }
        h1,h2,h3,h4,h5,h6,p {
            padding: 0;
            margin: 0;
        }
        a,
        a:hover,
        a:focus {
            color: #fff;
        }        
        .movieTrailers-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        @media(min-width: 400px) {
            .movieTrailers-container {
                flex-flow: row wrap;
                justify-content: space-around;
                width: 90%;
                max-width: 1200px;
                margin: 0 auto;                
            }        
        }        
        .movie-tile {
            margin-bottom: 50px;
            padding-top: 50px;
            padding: 0 1em;
            transition: transform .1s ease-out;
            color: #fff;
        }
        .movie-tile:hover {
            transform: scale(1.1);
            cursor: pointer;
        }
        .movieTitle {
            position: relative;
            bottom: 55px;
            background: #32ab9b;
            padding: 0.5em;
            box-sizing: border-box;
            width: 90%;
            max-width: 220px;
            margin: 0 auto;
            text-align: center;
            margin-bottom: -41px;
            border-radius: 2px;
        }
        .detials-wrapper {
            padding-top: 1em;
        }
        .rating-container {
            width: 50%;
            float: left;
            transition: all .1s ease-out;
        }
        .rating-icon {
            width: 35px;
            height: 35px;
            margin-bottom: -7px;
        }
        .rating {
            display: inline;
            font-size: 23px;
        }
        .info-container {
            width: 50%;
            float: right;
            background: #f93109;
            margin-top: 4px;
            padding: 5px 0;
            border-radius: 100px;
            transition: all .1s ease-out;
        }
        .info {
            text-align: center;
        }
        .rating-container:active {
            transform: scale(0.8);
        }

        .container {
            display: none;
        }

        .modal {
            justify-content: center;
            align-content: center;
            align-self: center;
            align-items: center;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;          
        }

        #trailer .modal-dialog {
            width: 85vw;
            height: auto;
        }
        .hanging-close {
            position: absolute;
            top: 70px;
            left: 390px
            z-index: 9001;

            display: none;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;


        }

        .show {
            display: flex !important;
        }

        .hide {
            display: none !important;           
        }


        .showModal {
            position: fixed;
            display: flex;
            background: rgba(0, 0, 0, 0.6)
        }

        .hideModal {
            position: none;
            display: none;
        }

        
    </style>
    <script type="text/javascript" charset="utf-8">
        $(document).ready(function () {
            $(".modal").addClass("hideModal");           
        });
       

        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
            $(".modal").removeClass("showModal");
            $(".modal").addClass("hideModal");
        });

        $(document).on('click', '.movie-tile', function (event) {
            $(".modal").removeClass("hideModal");
            $(".modal").addClass("showModal");
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });       

        $(document).ready(function () {
          $(".movie-tile").hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });       

    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="movieTrailers-container">
      {movie_tiles}
    </div>

    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>   

  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img id="posterImage" src="{poster_image_url}" width="220" height="342">
        <h3 id="mt" class="movieTitle">{movie_title}</h3>
    <div class="detials-wrapper">
        <a id="rotten-tomatoes-link" href="{reviews_link}" target="_blank"><div class="rating-container">
            <img class="rating-icon" src="https://staticv2-4.rottentomatoes.com/static/images/icons/new-upright.png">
            <h3 class="rating">{audience_rating}</h3>
        </div></a>
        <div id="ic" class="info-container">
            <h3 class="info">{age_restriction}</h3>          
        </div>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            audience_rating=movie.rating,
            reviews_link=movie.link,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,                      
            age_restriction=movie.restriction
        )        
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('popcorn.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
