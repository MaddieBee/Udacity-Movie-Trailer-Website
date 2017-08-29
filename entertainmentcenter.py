import fresh_tomatoes
import media 

kill_bill = media.Movie("Kill Bill", 
                        "A Woman's Revenge On The People Who Attempted To Kill Her.",
                        "http://girlswithguns.org/wp-content/gallery/kill-bill-volume-1/killbill1-1.jpg", 
                        "https://www.youtube.com/watch?v=7kSuas6mRpk")



somethings_gotta_give = media.Movie("Something's Gotta Give",
                     "A Swinger With A Taste For Younger Women Falls In Love A Woman Closer To His Age",
                     "https://upload.wikimedia.org/wikipedia/en/7/7d/Somethings_gotta_give.jpg",
                     "https://www.youtube.com/watch?v=6zVzIaEuXS4")

hannibal = media.Movie("Hannibal",
                       "Hannibal Lecter returns, this time In Italy",
                       "https://upload.wikimedia.org/wikipedia/en/9/9b/Hannibal_movie_poster.jpg",
                       "https://www.youtube.com/watch?v=Lr3OavheNu0")

uncle_buck = media.Movie("Uncle Buck",
                         "When A Family Emergency Arises, The Only One Available To Watch The Kids Is Their Lazy, Unemployed Uncle.",
                         "https://upload.wikimedia.org/wikipedia/en/8/8c/Uncle_buck.jpg",
                         "https://www.youtube.com/watch?v=zXEzA1egFL4")

bridget_jones_diary = media.Movie("Bridget Jones's Diary",
                         "An awkward, accident prone single woman tries to find love",
                         "https://upload.wikimedia.org/wikipedia/en/1/17/BridgetJonesDiaryMoviePoster.jpg",
                         "https://www.youtube.com/watch?v=EtB2FwwaMT0")
 
the_nutty_professor = media.Movie("The Nutty Professor",
                         "An Obese Scientist Develops A Way To Lose Weight.",
                         "https://upload.wikimedia.org/wikipedia/en/7/7f/Nutty_professor_ver1.jpg",
                         "https://www.youtube.com/watch?v=o3wJ-jzZqBw")
  
  

movies = [kill_bill, somethings_gotta_give, hannibal, uncle_buck, bridget_jones_diary, the_nutty_professor]

fresh_tomatoes.open_movies_page(movies) 