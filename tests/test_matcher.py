from app.data_loader import load_data
from app.matcher import JobMatcher
from app.resume_parser import extract_resume_text

# 1. Load dataset
print("Loading data...")
df = load_data()
print("Data loaded:", df.shape)

# 2. Initialize matcher
print("Building matcher...")
matcher = JobMatcher(df)

# 3. Load resume
resume_path = "/Users/shreyasg/Documents/SEMESTER-2-SPRING-2026/COURSES/MIS_6V99_DATABASE/6V99_Project/data/Shreyasg_SoftwareEngineer_Internship.pdf"
resume_text = extract_resume_text(resume_path)

# 4. Run matching
print("Matching jobs...")
results = matcher.match(resume_text)

# 5. Print results
print("\nTop Matches:\n")
for i, row in results.iterrows():
    print("Job Title:", row['job_title'])
    print("Match Score:", row['match_score'])
    print("Skills:", row['skills'])
    print("Missing Skills:", row['missing_skills'])
    print("-" * 50)