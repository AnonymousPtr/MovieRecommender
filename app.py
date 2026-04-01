import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process

st.set_page_config(page_title="Movie Recommender", layout="centered")

# =========================================
# Load Model
# =========================================
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

tfidf_matrix = model["tfidf_matrix"]
movies = model["movies"]
indices = model["indices"]

movie_titles = movies["title"].tolist()


# =========================================
# Recommendation Function
# =========================================
def recommend_movies(title, top_n=10):

    if title not in indices.index:
        return []

    idx = indices[title]

    sim_scores = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix
    ).flatten()

    sim_indices = sim_scores.argsort()[::-1][1:top_n+1]

    return movies.iloc[sim_indices]["title"].tolist()


# =========================================
# Fuzzy Search
# =========================================
def fuzzy_search(query):

    matches = process.extract(
        query,
        movie_titles,
        limit=10
    )

    return [m[0] for m in matches]


# =========================================
# UI
# =========================================
st.title("🎬 Movie Recommendation System")

query = st.selectbox(
    "Start typing a movie name",
    movie_titles,
    index=None,
    placeholder="Search for a movie..."
)

# Directly use the selected movie
if query:

    st.markdown(f"### Recommendations for **{query}**")

    recs = recommend_movies(query)

    for i, movie in enumerate(recs, 1):
        st.write(f"{i}. {movie}")