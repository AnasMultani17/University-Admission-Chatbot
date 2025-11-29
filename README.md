# 🎓 University Admission Chatbot

## 🧠 Overview
The **University Admission Chatbot** is an intelligent conversational assistant designed to automate and simplify access to university-related information. Using advanced **Natural Language Processing (NLP)** and **Retrieval-Augmented Generation (RAG)** techniques, the chatbot provides instant, accurate, and human-like responses to student queries about **admissions, fees, scholarships, and courses**.

---
[![Live Demo](https://img.shields.io/badge/Demo-Live-brightgreen?style=for-the-badge)](https://university-admission-chatbot-fronte.vercel.app/)


## 👥 Team Members
| Name | Student ID |
|------|-------------|
| Jenil Soni | 23BCE119 |
| Rishi Kukadiya | 23BCE156 |
| Karmit Langhnoda | 23BCE157 |
| Mahin Mehta | 23BCE161 |
| Anas Multani | 23BCE188 |

---

## 🚀 Key Features
- **Natural Language Understanding:** Interprets user queries and intent using advanced NLP models.  
- **Slot Extraction:** Extracts key details (e.g., course name, location, or fee type) from user input.  
- **Intent Classification:** Determines the user’s purpose (e.g., *admission process*, *fee details*, *scholarships*).  
- **Document Retrieval (RAG):** Searches relevant university PDFs or scanned documents using TF-IDF and cosine similarity.  
- **Context-Aware Conversations:** Maintains user context and conversation flow using **MongoDB**.  
- **Human-like Responses:** Generates answers via **Google Gemini 2.5 Flash**, ensuring factual and conversational accuracy.  
- **Scalable Design:** Modular architecture for easy integration with other university services.  
- **Multilingual Support:** Easily extendable to handle queries in multiple languages.

---

## ⚙️ System Architecture

### 🔹 Step-by-Step Workflow
1. **User Input** — The student types a question into the chat interface (React frontend).  
2. **Backend Processing** — Backend creates/updates user session and forwards query to AI agent.  
3. **Intent & Slot Extraction**  
   - **Intent Classifier:** A HuggingFace-based Transformer model identifies user intent.  
   - **Slot Extractor:** Uses **Google Gemini 2.5 Flash (via LangChain)** to parse structured data (JSON format).  
4. **Retrieval-Augmented Generation (RAG):**  
   - Retrieves top relevant document chunks via **TF-IDF + cosine similarity**.  
   - Combines retrieved content with user context to craft a factual LLM prompt.  
5. **Response Generation:** Gemini 2.5 Flash produces a domain-specific, human-like response.  
6. **Database Logging:** Session data and extracted slots are stored in **MongoDB**.  
7. **Final Output:** The chatbot delivers a precise and contextual response to the user.

---

## 🧩 AI Components

| Component | Model / Framework | Function |
|------------|------------------|-----------|
| **Slot Extraction** | Google Gemini 2.5 Flash (via LangChain) | Converts natural text into structured JSON data. |
| **Intent Classification** | HuggingFace Transformers | Classifies user intent (e.g., *fees_info*, *admission_process*). |
| **Document Retrieval** | TF-IDF + Cosine Similarity | Finds the most relevant university documents. |
| **OCR Processing** | PyPDF2 + Tesseract OCR | Extracts text from scanned or image-based PDFs. |
| **Database** | MongoDB | Stores session context and slot data persistently. |
| **Frontend** | React.js | Provides an interactive chat interface. |
| **Backend** | Python (Flask / FastAPI) | Handles NLP processing and API integration. |

---

## 🧾 Tech Stack

| Layer | Technologies |
|--------|---------------|
| **Frontend** | React.js, HTML, CSS |
| **Backend** | Python, Flask / FastAPI |
| **NLP / AI** | LangChain, HuggingFace Transformers, Gemini 2.5 Flash |
| **Retrieval** | TF-IDF, Cosine Similarity |
| **OCR & Data** | PyPDF2, Tesseract OCR |
| **Database** | MongoDB |
| **Version Control** | Git & GitHub |

---

## 🔍 Insights
- **High Accuracy:** RAG ensures the chatbot delivers factual, document-grounded answers.  
- **Persistent Context:** MongoDB enables continuous conversation flow and session management.  
- **Scalable & Modular:** Components can be independently improved or replaced.  
- **Real-world Application:** Demonstrates the power of NLP and information retrieval for academic institutions.

---

## 🧭 Future Enhancements
- Voice-based query support (speech-to-text & text-to-speech integration)  
- Advanced multilingual support (regional languages)  
- Integration with student portals for personalized information  
- Enhanced analytics dashboard for administrators  

---

## 🏁 Conclusion
The **Gujarat University Admission Chatbot** showcases the fusion of NLP, document retrieval, and conversational memory to build intelligent, context-aware systems. It represents a major step toward **automating university information systems** and improving **student engagement** through natural, conversational interactions.

---

## 📬 Contact
For project inquiries or collaborations, contact the team via email or through the university’s innovation cell.

