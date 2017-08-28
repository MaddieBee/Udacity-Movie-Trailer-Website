# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:58:19 2017

@author: Shesb
"""

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

cruel_intentions = media.Movie("Cruel Intentions",
                         "Two Wealthy Teenagers Play A Game With Love And Seduction.",
                         "https://upload.wikimedia.org/wikipedia/en/9/9c/Cruel_intentions_ver1.jpg",
                         "https://www.youtube.com/watch?v=SCFR2vpMIQU")
 
the_nutty_professor = media.Movie("The Nutty Professor",
                         "An Obese Scientist Develops A Way To Lose Weight.",
                         "https://upload.wikimedia.org/wikipedia/en/7/7f/Nutty_professor_ver1.jpg",
                         "https://www.youtube.com/watch?v=o3wJ-jzZqBw")
  
  

movies = [kill_bill, somethings_gotta_give, hannibal, uncle_buck, cruel_intentions, the_nutty_professor]

fresh_tomatoes.open_movies_page(movies) 
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__module__)