import pickle
import pandas as pd
import streamlit as st


# Load the data
data = pickle.load(open('movie_dict.pkl', mode='rb'))
movies = pd.DataFrame(data)
# print(movies)


# Load the similarity
similarity = pickle.load(open('similarity.pkl', mode='rb'))
print(similarity)


# Function to recommend a movie
def recommend(movie):
    
    recommended_movies = []

    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])[1:6]
    
    for movie in movie_list:
        recommended_movies.append(movies.iloc[movie[0]].title)

    return recommended_movies


# Streamlit Web-App

st.title('Movie Recommendation System')
selected_movie = st.selectbox("Please select a movie to get best recommendations: ", movies['title'].values)
btn = st.button('Recommend')


if btn:
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)




