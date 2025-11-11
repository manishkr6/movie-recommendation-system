import pickle
import streamlit as st
import requests

# ----------------------------
# Fetch movie poster function
# ----------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path


# ----------------------------
# Recommend movies function
# ----------------------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters


# ----------------------------
# Streamlit UI Design
# ----------------------------
st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎥", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        /* Main title */
        .main-title {
            text-align: center;
            font-size: 2.8em;
            color: #BB86FC;
            font-weight: bold;
            margin-bottom: 10px;
        }

        /* Subtitle */
        .sub-title {
            text-align: center;
            color: #B0B0B0;
            font-size: 1.1em;
            margin-bottom: 40px;
        }

        /* Movie Card */
        .movie-card {
            text-align: center;
            background-color: #1E1E1E;
            padding: 10px;
            border-radius: 12px;
            transition: 0.3s;
        }

        .movie-card:hover {
            background-color: #2A2A2A;
            transform: scale(1.03);
        }

        .movie-card img {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.4);
            width: 100%;
            height: 300px;
            object-fit: cover;
        }

        .movie-title {
            margin-top: 10px;
            font-weight: 600;
            color: #FFFFFF;
            text-shadow: 0 0 6px rgba(187,134,252,0.6);
            font-size: 1rem;
        }

        /* Footer (Your Name) */
        .footer {
            text-align: center;
            margin-top: 60px;
            color: #888;
            font-size: 1em;
        }

        .footer span {
            color: #BB86FC;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# App Title
# ----------------------------
st.markdown("<h1 class='main-title'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Find your next favorite movie — powered by Machine Learning!</p>", unsafe_allow_html=True)

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox("🎞️ Type or select a movie from the dropdown", movie_list)

# Show recommendations
if st.button('✨ Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    cols = st.columns(5)
    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.markdown(f"""
                <div class='movie-card'>
                    <img src='{poster}' alt='{name}'/>
                    <p class='movie-title'>{name}</p>
                </div>
            """, unsafe_allow_html=True)

# Footer - Your Name
st.markdown("<div class='footer'>🎥 Created with ❤️ by <span>Manish Kumar</span></div>", unsafe_allow_html=True)
