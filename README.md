# 🚀 TalentRadar – AI Resume to Job Matching System

TalentRadar is an AI-powered application that matches a candidate’s resume with relevant job postings using semantic similarity and skill-based analysis. The system processes a resume PDF, extracts meaningful information such as skills, and compares it against a dataset of job postings to recommend the most relevant opportunities along with match scores and missing skill insights.

The goal of this project is to demonstrate how modern techniques like embeddings and similarity search can be used to build intelligent job recommendation systems. It provides a working prototype that integrates backend APIs, machine learning models, and a user-friendly interface.

---

## 📌 Features

- Upload resume in PDF format
- Automatic extraction of text from resume
- Skill identification using keyword matching
- Semantic matching between resume and job descriptions
- Ranking of top matching jobs
- Match score visualization
- Identification of missing skills
- Interactive UI built using Streamlit

---

## 🏗️ Project Structure

TalentRadar/
│  
├── app/                 → Backend logic (API, matcher, embeddings, parsing)  
├── data/                → Dataset and sample resumes  
├── tests/               → Testing scripts  
├── ui/                  → Streamlit frontend  
├── notebooks/           → Data exploration (EDA)  
│  
├── requirements.txt  
├── README.md  
└── .gitignore  

---

## ⚙️ Tech Stack

This project is built using:

- Python  
- FastAPI (for backend API)  
- Streamlit (for frontend UI)  
- Sentence Transformers (for generating embeddings)  
- Scikit-learn (for cosine similarity)  
- Pandas and NumPy (for data processing)  
- PyPDF (for resume parsing)  
- NetworkX (for future skill graph integration)  

---

## 🚀 How to Run the Project

Follow these steps to run the project locally:

1. Clone the repository  
   git clone <your-repo-link>  
   cd TalentRadar  

2. Create a virtual environment  
   python3 -m venv venv  
   source venv/bin/activate  

3. Install dependencies  
   pip install -r requirements.txt  

4. Run the backend server  
   uvicorn app.api:app --reload  

5. Run the frontend application (in a new terminal)  
   streamlit run ui/app.py  

6. Open the browser and go to  
   http://localhost:8501  

Upload your resume and click “Analyze Resume” to see results.

---

## 📊 How the System Works

The system follows a simple but effective pipeline:

1. A resume is uploaded in PDF format  
2. The text is extracted using a PDF parser  
3. Skills are identified from the extracted text  
4. Job postings are preprocessed and converted into text descriptions  
5. Both resume and job descriptions are converted into embeddings  
6. Cosine similarity is used to find the closest matching jobs  
7. Top matching jobs are returned along with match scores  
8. Missing skills are identified by comparing resume skills with job requirements  

---

## ⚠️ Notes

- The dataset is sampled (5000 records) for faster performance during development  
- FAISS was initially considered for vector search but replaced with cosine similarity due to local environment compatibility issues  
- The system is designed as a prototype and can be scaled for production use  

---

## 🔮 Future Improvements

- Integrate FAISS or vector databases like Pinecone or Weaviate  
- Improve skill extraction using NLP techniques (NER models)  
- Build a skill recommendation engine using graph databases (Neo4j)  
- Add real-time job data from APIs (LinkedIn, Indeed, etc.)  
- Enhance ranking with hybrid scoring (skills + semantic + graph-based)  

---

## 👨‍💻 Author

Shreyas Gangadhar  
MS in Information Technology & Management  
The University of Texas at Dallas  