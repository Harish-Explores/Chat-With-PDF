import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

if __name__ == '__main__':
    st.set_page_config(page_title="Chat With PDF", layout="wide")
    st.title("Let's Chat With Your PDF")
    
    uploaded_file = st.file_uploader("Choose a PDF", type='pdf')
    
    if uploaded_file is not None:
        # Open the PDF file
        pdf_file = PdfReader(uploaded_file)
        
        # Extract the content
        pdf_text = ''
        for i, page in enumerate(pdf_file.pages):
            print(page.extract_text())
            page_content = page.extract_text()
            if page_content:
                pdf_text += page_content
        
        # split the text into chunks
        text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap=200, separator='\n', strip_whitespace=False)
        text_chunks = text_splitter.create_documents([pdf_text])
        
        st.write(text_chunks)
