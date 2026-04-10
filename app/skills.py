skills_list = [
    "python", "java", "c++", "javascript",
    "machine learning", "data science",
    "aws", "azure", "gcp", "cloud",
    "docker", "kubernetes",
    "sql", "mysql", "mongodb",
    "devops", "linux", "git",
    "react", "node", "api",
    "tensorflow", "pytorch",
    "excel", "power bi", "tableau"
]

def extract_skills(text):
    if not isinstance(text, str):
        return []

    text = text.lower()

    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return list(set(found))