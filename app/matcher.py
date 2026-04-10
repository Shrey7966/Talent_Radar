import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.embedding import get_embeddings
from app.skills import extract_skills


class JobMatcher:
    def __init__(self, df):
        self.df = df
        self.embeddings = get_embeddings(df["description"].tolist())

    def skill_gap(self, resume_text, job_skills):
        resume_skills = extract_skills(resume_text)
        return list(set(job_skills) - set(resume_skills))

    def match(self, resume_text, top_k=5):
        resume_emb = get_embeddings([resume_text])

        sims = cosine_similarity(resume_emb, self.embeddings)[0]
        top_indices = np.argsort(sims)[::-1][:top_k]

        results = self.df.iloc[top_indices].copy()
        results["match_score"] = [round(float(sims[i]), 2) for i in top_indices]

        results["missing_skills"] = results["skills"].apply(
            lambda x: self.skill_gap(resume_text, x)
        )

        return results