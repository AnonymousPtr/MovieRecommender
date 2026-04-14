# 🎬 VinCine — Movie Recommendation System

VinCine is an end-to-end movie recommendation system built using the MovieLens dataset.  
It explores and compares multiple recommendation techniques and deploys a real-time content-based recommender with an interactive UI.

---

## 🚀 Live Demo

👉 https://vincine.streamlit.app  

---

## 📌 Project Overview

This project implements and compares three major recommendation approaches:

- Content-Based Filtering
- Collaborative Filtering (User-User)
- Matrix Factorization (SVD)

The goal was to:
- Understand different recommendation strategies
- Evaluate their performance
- Deploy a practical and user-friendly system

---

##  Approach

### 1. Data Processing
- Dataset: MovieLens (ratings, movies, tags)
- Cleaned and merged datasets
- Combined features using:
  - Genres
  - User-generated tags

---

### 2. Models Implemented

#### 🔹 Content-Based Filtering
- Feature engineering: genres + tags
- TF-IDF vectorization
- Cosine similarity for recommendations

#### 🔹 Collaborative Filtering (User-User)
- User-item rating matrix
- Cosine similarity between users
- Weighted rating prediction

#### 🔹 Matrix Factorization (SVD)
- Decomposed user-item matrix using Singular Value Decomposition
- Captured latent features
- Reconstructed rating matrix for predictions

---

### 3. Evaluation Metrics

- RMSE (Root Mean Squared Error)
- Precision@10
- Recall@10

---

## 📊 Results Summary

| Model | RMSE | Precision@10 | Recall@10 |
|------|------|-------------|-----------|
| Content-Based | — | 0.094 | 0.015 |
| Collaborative Filtering | 3.057 | 0.480 | 0.116 |
| Matrix Factorization (SVD) | **2.014** | **0.664** | **0.163** |

###  Insights

- **SVD performed best overall**, achieving:
  - Lowest RMSE
  - Highest Precision & Recall

- **Collaborative Filtering**:
  - Strong recommendation quality
  - Less accurate rating prediction

- **Content-Based**:
  - Lower performance
  - But useful for **cold-start scenarios**

---

## Note: Why Content-Based Was Deployed

Although SVD and CF performed better:

- They require **user history / ratings**
- Not suitable for **new users (cold start problem)**

 Therefore, the **content-based model was deployed** since it works without prior user data.

---

## 🖥️ Deployment

The application is deployed using **Streamlit Cloud**.

### Features:
-  Fuzzy search for movie names
-  Real-time recommendations
-  Interactive UI
-  Pre-trained model (`model.pkl`) for fast inference

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- RapidFuzz

---

## Project Structure

```
movie-recommender/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
│
|── Datasets/
│ └── movies.csv
  └── ratings.csv
  └── tags.csv
|
├── notebook/
│ └── ComparativeMovieRecommenderStudy.ipynb 
│
├── ComparativeMovieRecommenderStudy.ipynb - Colab.pdf
```

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/AnonymousPtr/MovieRecommender
cd movie-recommender

pip install -r requirements.txt

streamlit run app.py
```
## Future Improvements

- Hybrid recommendation system  
- Add movie posters (TMDB API)  
- Personalized user profiles  
- Faster similarity search (ANN methods)  

