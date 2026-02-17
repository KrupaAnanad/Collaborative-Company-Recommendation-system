# 🚀 Smart Collaborative Company Recommender

A Flask-based web application that recommends companies using **Item-Based Collaborative Filtering**.  
The system builds a Company–Skill interaction matrix and applies **Cosine Similarity** to rank companies based on user-selected skills.

---

## 📌 Project Overview

This project implements a machine learning–driven recommendation engine that suggests companies based on skill similarity patterns.

Instead of simple keyword matching, it uses:

> **Item-Based Collaborative Filtering with Cosine Similarity**

Companies are ranked and categorized into qualitative recommendation tiers such as:

- 🔥 Best Match  
- ⭐ Strong Match  
- ✔ Suitable  
- ❌ Less Relevant  

The system provides dynamic ranking without displaying raw similarity percentages for better interpretability.

---

## 🧠 Recommendation Approach

1. Construct a **Company–Skill Interaction Matrix**
2. Convert user-selected skills into a binary skill vector
3. Compute similarity using **Cosine Similarity**
4. Rank companies based on similarity strength
5. Display ranked recommendations with qualitative labels

This ensures scalable and ML-driven recommendation logic.

---

## ⚙️ Technologies Used

- Python  
- Flask  
- Pandas  
- NumPy  
- Scikit-learn  
- HTML5  
- CSS3  

---

## 🏗️ Project Structure

```
flask-project/
│
├── train_model.py
├── app.py
├── model.pkl
├── company_skill_mixed_realistic_dataset.csv
│
└── templates/
    └── index.html
```

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

### 2️⃣ Train the Model

```bash
python train_model.py
```

### 3️⃣ Run the Application

```bash
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000
```

---

## 🎯 Key Features

✔ Collaborative Filtering (ML-based)  
✔ Cosine Similarity Ranking  
✔ Dynamic Skill Selection  
✔ Adjustable Number of Recommendations  
✔ Rank-Based Recommendation Categories  
✔ Modern Interactive UI  
✔ Clean & Modular Code  

---

## 📚 Academic Relevance

This project demonstrates:

- Collaborative Filtering Concepts  
- Cosine Similarity Implementation  
- Interaction Matrix Construction  
- ML Model Integration with Flask  
- End-to-End Web Deployment  

It can be extended into a hybrid recommender or matrix factorization model.

---

## 🔮 Future Enhancements

- Hybrid Recommendation System (Collaborative + Content-Based)  
- Matrix Factorization (SVD)  
- Precision@K and Recall@K Evaluation  
- User Login & Personalization  
- Cloud Deployment (Render / AWS / Docker)  

---

## 👨‍💻 Author

**K Anand**  
Machine Learning & Data Science Enthusiast  
