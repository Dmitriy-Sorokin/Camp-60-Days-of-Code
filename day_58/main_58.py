import pandas
from surprise import Dataset, Reader

movies = pandas.read_csv("movies.csv")
credit = pandas.read_csv("credits.csv")
ratings = pandas.read_csv("ratings.csv")

print(movies.head())