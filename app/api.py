from fastapi import FastAPI, UploadFile, File
import shutil

from app.data_loader import load_data
from app.matcher import JobMatcher
from app.resume_parser import extract_resume_text
from app.skills import extract_skills   # ✅ ADD THIS

app = FastAPI()

# Load data
df = load_data()
matcher = JobMatcher(df)


@app.get("/")   # ✅ ADD THIS (optional but useful)
def home():
    return {"message": "TalentRadar API running 🚀"}


@app.post("/match")
async def match_resume(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"

    # Save file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract resume text
    resume_text = extract_resume_text(file_location)

    # 🔥 DEBUG (VERY IMPORTANT)
    print("\n===== RESUME TEXT =====\n")
    print(resume_text[:500])

    # 🔥 Extract resume skills separately
    resume_skills = extract_skills(resume_text)
    print("\n===== RESUME SKILLS =====\n", resume_skills)

    # Match jobs
    results = matcher.match(resume_text)

    # 🔥 Add resume skills in response
    return {
        "resume_skills": resume_skills,
        "matches": results.to_dict(orient="records")
    }