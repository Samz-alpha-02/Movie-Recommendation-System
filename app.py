import pickle
import pandas as pd
import streamlit as st
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Streamlit app header and loading data
st.header('Movie Recommendation System', divider='rainbow')

# Load movie_dict.pkl
movies_dict = pickle.load(open('model/movie_dict.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

cv = CountVectorizer(max_features=10000, stop_words='english')

vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)

# Load similarity.pkl
#similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Dropdown to select movie
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    num_cols = 3  # Number of columns
    col_width = 200  # Width of each column
    spacing = 20  # Space between movie items
    
    
    # Iterate through recommendations and display
    for i in range(0, len(recommended_movie_names), num_cols):
        row_data = recommended_movie_names[i:i+num_cols]
        row_posters = recommended_movie_posters[i:i+num_cols]
        
        col1, col2, col3 = st.columns(num_cols)
        
        for col_idx, (name, poster) in enumerate(zip(row_data, row_posters)):
            with eval(f'col{col_idx + 1}'):
                st.write(name)
                st.image(poster, width=col_width)

        if i + num_cols < len(recommended_movie_names):
            st.write('<div style="margin-bottom:{}px;"></div>'.format(spacing), unsafe_allow_html=True)
