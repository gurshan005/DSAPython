"""
-------------------------------------------------------
task 2
-------------------------------------------------------
Author:  gurshan bhogal
ID:      999999999
Email:   bhog2062@wlu.ca
Section: CP164 B
__updated__ = "2021-01-12"
-------------------------------------------------------
"""
from Movie_utilities import get_by_year
from src.Movie_utilities import read_movie

with open('movies.txt', 'r') as file: 
    
    movies = read_movie(file)

year = int(input("year"))

vmovies = get_by_year(movies, 1964)

print(vmovies)
