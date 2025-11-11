# 🎬 Movie Recommender System

A **content-based movie recommendation system** built using **Machine Learning** and **Streamlit**.  
It recommends movies similar to the one you select — based on features like genres, keywords, and descriptions.

![App Screenshot](./image.png)

---

## 🚀 Features
- 🔍 Search and select any movie from the dropdown list  
- 🎥 Get top 5 similar movie recommendations instantly  
- 🧠 Powered by **content-based filtering** using cosine similarity  
- 💻 Interactive and modern web interface built with **Streamlit**  
- ✨ Dark-themed UI with clean movie card layout  

---

## 🧩 Tech Stack
- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
- **Pickle**

---

## ⚙️ How It Works
1. The dataset contains movie metadata (title, overview, genres, keywords, etc.).
2. Text data is converted into numerical vectors using **CountVectorizer**.
3. The **cosine similarity** metric measures how close movies are to each other.
4. Based on your selected movie, the top similar movies are recommended.

---

## 💡 Potential Uses
- 🎬 **Personalized Movie Recommendations** — Suggests movies similar in theme or content.  
- 🧠 **Content Similarity Insights** — Finds relationships between movies using text-based similarity.  
- 🗂️ **Scalable Recommendation System** — Can be extended for hybrid or collaborative filtering.  
- 🚀 **Practical Use Case** — Suitable for OTT platforms or movie suggestion apps.

---

## 🖥️ Run Locally
Clone the project and install dependencies.

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
streamlit run app.py
