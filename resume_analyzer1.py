import streamlit as st

import PyPDF2

from langchain_ollama import OllamaLLM

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")

st.title("📄 Resume Analyzer")

st.write("Upload your resume and get AI generated insights")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

# Basic styling - just a few essential elements

st.markdown("""

<style>

.main {

padding: 2rem;

}

.stButton>button {

width: 100%;

}

</style>

""", unsafe_allow_html=True)

if uploaded_resume:

    st.write("Resume successfully uploaded")

    # Read the resume & extract text for analysis

    pdf_reader = PyPDF2.PdfReader(uploaded_resume)

    resume_text = " ".join(page.extract_text() for page in pdf_reader.pages)

    st.text_area("Resume Text Preview", resume_text, height=300)

   

    llm = OllamaLLM(model="mistral", temperature=0.2, timeout=60)

    if st.button("Analyze resume"):

        with st.spinner("Analyzing..."):

            response = llm.invoke("Analyze this resume and extract key skills, experience, and suitability for the role of Software Engineer." + resume_text)

            st.write("Analysis result: ")

            st.write(response)