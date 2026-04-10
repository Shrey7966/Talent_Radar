from app.resume_parser import extract_resume_text

text = extract_resume_text("/Users/shreyasg/Documents/SEMESTER-2-SPRING-2026/COURSES/MIS_6V99_DATABASE/6V99_Project/data/Shreyasg_SoftwareEngineer_Internship.pdf")
print(text[:500])