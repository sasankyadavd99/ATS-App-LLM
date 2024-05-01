# ATS-App-LLM

Overview
The ATS Scanner LLM Model is a Streamlit-based application designed to assess resumes against specific job descriptions using cutting-edge language model APIs. This project leverages Python and various libraries to convert resumes in PDF format to images, extract text using OCR, and apply machine learning models to evaluate and match resumes to job descriptions.

Features
PDF Upload: Users can upload their resumes in PDF format.
Resume Analysis: The application utilizes machine learning models to extract and analyze the content of the resume.
Job Description Matching: Compares the extracted resume data against entered job descriptions to assess fit.
Percentage Match: Provides a quantitative measure of how well the resume matches the job description.

Tech Stack
Python: Primary programming language.
Streamlit: For creating the web application.
Pillow: For image processing tasks.
pdf2image: Converts PDF documents into images.
Google's generativeai: For accessing advanced ML model APIs.
Dotenv: For loading environment variables.

Usage
Start by cloning the repository and navigate to the project directory.
Install dependencies using pip install -r requirements.txt.
Run the Streamlit application using streamlit run app.py.

Application Screenshots
<img width="1512" alt="Screenshot 2024-04-30 at 11 47 58 PM" src="https://github.com/sasankyadavd99/ATS-App-LLM/assets/160814035/382a99a6-06ae-456b-a19a-2964deab3227">

