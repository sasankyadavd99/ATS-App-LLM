_import_('pysqlite3')
import sys
sys.modules['sqlite3']=sys.modules.pop('pysqlite3')

from dotenv import load_dotenv # type: ignore
load_dotenv()
import streamlit as st # type: ignore
import os
import io
import base64
from PIL import Image # type: ignore
import pdf2image # type: ignore
import google.generativeai as genai # type: ignore
HF_TOKEN =st.secrets['HUGGINGFACE_ACCESS_TOKEN']
os.environ['HUGGINGFACE_API_TOKEN']=HF_TOKEN

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text
    #if hasattr(response, 'parts'):
     #   texts = []
      #  for part in response.parts:
       #     if hasattr(part, 'text'):
       #         texts.append(part.text)
        #return ' '.join(texts)
        # If response contains parts and each part contains text
    #else:
     

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        #convert the pdf to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        #convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts=[
            {
                "mime_type": "image/jpeg",
                "data":base64.b64encode(img_byte_arr).decode()  #encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    
##streamlit app
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload Your Resume(PDF)",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1=st.button("Tell me About the Resume")

#submit2=st.button("How Can I Improve my Skills")

submit3=st.button("Percentage Match")

input_prompt1 = """
You are an experienced HR professional specializing in the tech industry in the field of Data Science, Machine learning engineer, Project Manager, Scrum engineer, ETL Developer,
Full Stack Web Development, Database Developer, Cloud Engineer, Data engineer, Data Analyst, your task is to review the provided resume against the job description for those profiles.
Please share your professional evaluation on whether the Candidate's profile aligns with the job description.
Highlight the strengths and weaknesses of the applicant in relation to the specified job description or role. Dont prompt candidate resume again and again just follow prompts given.
"""


##input_prompt2="""
#You are a career coach with a focus on professional development in the technology sector. Analyze the resume to identify gaps in skills and experience compared to industry standards for roles like 
#Frontend Developer, Database Developer, Data Engineer, and other tech positions. Offer actionable advice on additional certifications, courses, or projects 
#that the applicant could pursue to enhance their career trajectory and increase their marketability
#"""

input_prompt3= """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack Web Development,
Data Science Analyst, SQL Developer, Big Data Engineer, System Administrator, Database Developer, Cloud Engineer, Machine learning engineer, Project Manager, Scrum engineer, ETL Developer. 
Your task is to evaluate the resume against the provided job description. You should give me the resume percentage match based on key criteria in job descriptions 
such as required skills, requirements, prefered qualifications,and suggest areas of improvement to increase the match percentage. Dont prompt candidate resume again and again just follow prompts given.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
elif submit3:
     if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
     else:
        st.write("Please upload the resume")

