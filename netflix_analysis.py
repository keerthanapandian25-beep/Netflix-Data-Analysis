import pandas as pd
import numpy as np

print("pandas version:",pd.__version__)
print("numpy version:",np.__version__)

df = pd.read_csv("project/netflix_data_100-1.csv")
df["type"]=df["type"].str.strip()
print(df[df["type"] == "movie"][["title","type", "duration"]])
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["type"].value_counts())
print(df["release_year"].value_counts().sort_index())
print(df["rating"].value_counts())
print(df["country"].value_counts())
print(df.groupby(["country" , "type"]).size())
print(df.groupby(["release_year" , "type"]).size())
print(df["duration"].value_counts())
print(df[df["type"]=="movie"]["duration"].value_counts())
print(df["type"].unique())
print((df["type"]== "movie").sum())
print(df["type"].map(repr).unique())
print(repr(df["type"].iloc[0]))
print(df[["title", "type", "duration"]].head(10))
movies = df[df["type"] == "Movie"]
print(movies[["title", "duration"]].head())
movies["duration_min"] = movies["duration"].str.replace(" min", "").astype(int)
print(movies[["title", "duration_min"]].head())
#arithmetic clculation movie duration
print(movies["duration_min"].mean())       #avg duration 129 minutes
print(movies["duration_min"].min())        #duration 80 minutes 
print(movies["duration_min"].max())        #duration 178 minutes
#find max duration movie
print(movies.loc[movies["duration_min"].idxmax(), ["title", "duration_min"]])  #the umbrella academy
tv_shows = df[df["type"] == "TV Show"]
#tv shows seasons calculate
print(tv_shows[["title", "duration"]].head())
#seasons count string datatype change into int
tv_shows["seasons"] = tv_shows["duration"].str.replace(" Seasons", "").astype(int)
print(tv_shows[["title", "seasons"]].head())
#calculate average seasons
print(tv_shows["seasons"].mean())    #3.0
print("Minimum seasons:", tv_shows["seasons"].min())    #1
print("Maximum seasons:", tv_shows["seasons"].max())    #5
#find show name
print(tv_shows.loc[tv_shows["seasons"].idxmax(), ["title", "seasons"]])
#shows by number of seasons
print(tv_shows["seasons"].value_counts().sort_index())
#calculate how many movies and shows in the dataset
print(df["type"].value_counts())

print(df["type"].value_counts(normalize=True) * 100)
print(df["country"].value_counts())
print(df.groupby(["country","type"]).size())
print(df.groupby(["release_year", "type"]).size())
print(df["duration"].value_counts())

movies = df[df["type"] == "Movie"].copy()

movies["duration_minutes"] = movies["duration"].str.replace(" min", "").astype(int)

print("Minimum movie duration:", movies["duration_minutes"].min())
print("Maximum movie duration:", movies["duration_minutes"].max())
print("Average movie duration:", movies["duration_minutes"].mean())

tv_shows = df[df["type"] == "TV Show"].copy()

tv_shows["seasons"] = tv_shows["duration"].str.replace(" Seasons", "").astype(int)

print("Minimum seasons:", tv_shows["seasons"].min())
print("Maximum seasons:", tv_shows["seasons"].max())
print("Average seasons:", tv_shows["seasons"].mean())

print(tv_shows[tv_shows["seasons"] == tv_shows["seasons"].max()][["title", "seasons"]])
print(df.groupby(["rating","type"]).size())

print(df["rating"].value_counts())
print(df.groupby(["country","rating"]).size())
print(df.groupby(["country", "release_year"]).size())
print(df["release_year"].value_counts().sort_values(ascending=False))

# ---------------- KEY FINDINGS ----------------

print("KEY FINDINGS")
print("1. Dataset contains 100 titles.")
print("2. There are 50 Movies and 50 TV Shows.")
print("3. The dataset contains 10 titles from each country.")
print("4. Movie duration ranges from 80 to 178 minutes.")
print("5. Average movie duration is 129 minutes.")
print("6. TV Shows have 1 to 5 seasons.")
print("7. Average number of TV Show seasons is 3.")
print("8. 9 TV Shows have the maximum of 5 seasons.")
print("9. The dataset contains 6 different ratings.")
print("10. The highest number of titles in a release year is 7.")