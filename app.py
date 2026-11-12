import streamlit as st
import joblib
import pickle


st.title('Movie Recommendation System')

with open("movies.pickle", "rb") as m:
    movies = pickle.load(m)
    
similarity = joblib.load("similarity.joblib")
    
movies_name = movies['title'].values

selected_movie = st.selectbox("Enter movie name", movies_name)

def recommend(selected_movie):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    recommendations = similarity[movie_index]
    
    recommended_movies = []
    
    movie_list  = sorted(enumerate(recommendations), reverse=True, key= lambda x:x[1])[1:6]

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies

if st.button("Recommend"):
    r = recommend(selected_movie)
    st.write("Recommended movies are: ")
    
    for i in r:
        st.write(i)