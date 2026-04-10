import pandas as pd
from app.skills import extract_skills

def load_data():
    # ✅ Load dataset from correct path
    df = pd.read_csv("data/linkedin_job_postings.csv")

    # ✅ LIMIT DATA (VERY IMPORTANT)
    df = df.sample(5000, random_state=42)   # use 5k rows (good balance)

    # ✅ Handle missing values safely
    df['job_title'] = df['job_title'].fillna('')
    df['company'] = df['company'].fillna('')
    df['job_location'] = df['job_location'].fillna('')
    df['job_level'] = df['job_level'].fillna('')
    df['job_type'] = df['job_type'].fillna('')
    df['search_position'] = df['search_position'].fillna('')

    # ✅ Create rich description (THIS IS CORE FOR MATCHING)
    df['description'] = (
        df['job_title'] + " " +
        df['company'] + " " +
        df['job_location'] + " " +
        df['job_level'] + " " +
        df['job_type'] + " " +
        df['search_position']
    )

    df['description'] = df['description'].astype(str).str.lower()

    # ✅ Extract skills
    df['skills'] = df['description'].apply(extract_skills)

    # ✅ Keep only useful columns
    df = df[['job_title', 'company', 'job_location', 'skills', 'description']]

    return df