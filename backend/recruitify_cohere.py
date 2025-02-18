from dotenv import load_dotenv
import pdfplumber
import os
from langchain_cohere.chat_models import ChatCohere
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
cohere_api_key = os.getenv("COHERE_API")

def pdf_to_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def generate_script():
    resume = pdf_to_text("./uploads/resume.pdf")
    
    job_description_file = open("./uploads/job_description.txt", "r")
    job_description = job_description_file.read()

    writing_sample_file = open("./uploads/writing_sample.txt", "r")
    writing_sample = writing_sample_file.read()

    prompt = ChatPromptTemplate.from_template("""
    Based on the following resume and job description and writing_sample, create a compelling 2-paragraph pitch from the resume owner's point of view in the style and tone similar to the writing sample. Only return the pitch:
        
        WRITING SAMPLE:
        {writing_sample}

        RESUME:
        {resume}
        
        JOB DESCRIPTION:
        {job_description}
        
        Create a personalized pitch that:
        1. Shows enthusiasm for the company and role in the first paragraph
        2. Highlights relevant achievements and potential contributions in the second paragraph
        3. Ends with a polite request for an interview or coffee chat
        4. Maintains a professional yet engaging tone
        5. Is specific to the role and company
        """)

    llm = ChatCohere(
        model="command-r-plus", 
        temperature=0.5, 
        api_key=cohere_api_key)

    chain = prompt | llm

    response = chain.invoke({
        "writing_sample" : writing_sample,
        "resume": resume,
        "job_description": job_description
    })

    return response.content

def main():
    print(generate_script())


if __name__ == '__main__':
    main()