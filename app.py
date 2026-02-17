from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load trained matrix
with open("model.pkl", "rb") as f:
    company_skill_matrix = pickle.load(f)

companies = list(company_skill_matrix.index)
skills = list(company_skill_matrix.columns)


@app.route("/", methods=["GET", "POST"])
def home():
    results = None
    num_results = 5  # default value

    if request.method == "POST":

        user_input = request.form.get("skills")
        num_results = int(request.form.get("num_results", 5))

        if user_input:

            selected_skills = [
                skill.strip().lower()
                for skill in user_input.split(",")
                if skill.strip()
            ]

            # Create user skill vector
            user_vector = np.array([
                1 if skill in selected_skills else 0
                for skill in skills
            ])

            # Compute similarity
            similarity_scores = cosine_similarity(
                [user_vector],
                company_skill_matrix.values
            )[0]

            recommendations = []

            for i, score in enumerate(similarity_scores):
                recommendations.append({
                    "company": companies[i],
                    "score": score
                })

            # Sort by similarity
            recommendations = sorted(
                recommendations,
                key=lambda x: x["score"],
                reverse=True
            )

            results = recommendations[:num_results]

    return render_template(
        "index.html",
        results=results,
        skills=skills,
        num_results=num_results
    )


if __name__ == "__main__":
    app.run(debug=True)
