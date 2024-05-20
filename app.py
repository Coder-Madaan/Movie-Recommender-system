import streamlit as st
import pandas as pd
import pickle

movies_dict = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_dict)


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Please select a movie from the dropdown button", movies['title'].values)
recommendations=recommend(selected_movie_name)


if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie_name)
    for i in recommended_movie_names:
        st.write(i)
