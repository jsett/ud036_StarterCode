import fresh_tomatoes
import media

#create instances of all our movies
reservoir_dogs = media.Movie("Reservior Dogs",
    "Eight men eat breakfast before carrying out a diamond heist",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Reservoir_dogs_ver1.jpg/220px-Reservoir_dogs_ver1.jpg", # NOQA
    "https://www.youtube.com/watch?v=vayksn4Y93A")
kill_bill = media.Movie("Kill Bill",
    "A assassin must wreak vengeance on a team of assassins who betrayed her",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Kill_bill_vol_one_ver.jpg/220px-Kill_bill_vol_one_ver.jpg", # NOQA
    "https://www.youtube.com/watch?v=7kSuas6mRpk")
pulp_fiction = media.Movie("Pulp Fiction",
    "Hitmen Jules and Vincent must retrieve a briefcase for their boss",
    "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg", # NOQA
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
inglourious_basterds = media.Movie("Inglourious Basterds",
    "A team plans to assassinate Nazi leaders in WW2 Germany.",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg", # NOQA
    "https://www.youtube.com/watch?v=KnrRy6kSFF0")
sin_city = media.Movie("Sin City",
    "A film that explores the dark and miserable town, Basin City",
    "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Sincitypostercast.jpg/220px-Sincitypostercast.jpg", # NOQA
    "https://www.youtube.com/watch?v=T2Dj6ktPU5c")

#put all our movies into a list
movies = [reservoir_dogs,kill_bill,pulp_fiction,inglourious_basterds,sin_city]

#open movies in the web browser
fresh_tomatoes.open_movies_page(movies)
