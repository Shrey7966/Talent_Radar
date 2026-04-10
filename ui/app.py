import streamlit as st
import requests

st.set_page_config(page_title="TalentRadar", layout="centered")

st.title("🚀 TalentRadar")
st.subheader("AI Resume → Job Matching System")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):
        with st.spinner("Processing..."):

            files = {
                "file": ("resume.pdf", uploaded_file.getvalue(), "application/pdf")
            }

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/match",
                    files=files,
                    timeout=30
                )

                if response.status_code == 200:
                    data = response.json()

                    st.subheader("🧠 Resume Skills")
                    st.write(", ".join(data["resume_skills"]))

                    st.subheader("🎯 Top Job Matches")

                    for job in data["matches"]:
                        st.markdown("---")
                        st.markdown(f"### {job['job_title']}")
                        st.write("Match Score:", round(job["match_score"], 2))
                        st.progress(min(int(job["match_score"] * 100), 100))
                        st.write("Skills Required:", ", ".join(job["skills"]))
                        st.write(
                            "Missing Skills:",
                            ", ".join(job["missing_skills"]) if job["missing_skills"] else "None"
                        )

                else:
                    st.error("API returned an error.")

            except Exception as e:
                st.error(f"❌ Backend error: {e}")