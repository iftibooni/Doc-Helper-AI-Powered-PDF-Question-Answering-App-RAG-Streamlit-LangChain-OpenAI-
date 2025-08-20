# 📄 Doc Helper

**Doc Helper** is an AI-powered Streamlit application for interactive question answering on PDF documents.  
It uses Retrieval-Augmented Generation (RAG) with LangChain and OpenAI to let you upload a PDF, ask questions, and get accurate answers based on your document’s content.

---

## Features

- **PDF Upload:** Easily upload any PDF document.
- **Automatic Processing:** Document is chunked and embedded for semantic search.
- **Semantic Search:** Retrieves the most relevant content for your query.
- **AI-Powered Answers:** Uses OpenAI’s GPT model to answer questions from your document.
- **Modern UI:** Clean, responsive interface built with Streamlit.

---

## How It Works

1. **Upload a PDF:** Drag and drop your PDF file.
2. **Processing:** The app splits and embeds the document using LangChain and OpenAI.
3. **Ask Questions:** Type your question in the input box.
4. **Get Answers:** The app retrieves relevant chunks and generates an answer using GPT.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/doc-helper.git
   cd doc-helper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key:**
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Run the app:**
   ```bash
   streamlit run Code.py
   ```

---

## Usage

- Upload a PDF document.
- Ask any question about its content.
- Get instant, context-aware answers.

---

## Technologies Used

- [Streamlit](https://streamlit.io/)
- [LangChain](https://langchain.com/)
- [OpenAI GPT](https://platform.openai.com/)
- [FAISS](https://github.com/facebookresearch/faiss)

---

## Example

![Doc Helper Screenshot](screenshot.png)

---

## License

MIT License

---

## Acknowledgements

- Inspired by modern RAG architectures and open-source AI tools.
