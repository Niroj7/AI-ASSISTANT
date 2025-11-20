# 🤖 **AI Chat Assistant**

A smart, fast, and interactive **LLM-powered assistant** with file reading, CSV analysis, and conversation memory — built using **Streamlit + Groq API**.

---

## 🔗 **Live Demo**
👉 https://ai-assistant-mheejbemf6k6ydedq3aql7.streamlit.app/

---

## 🚀 **Overview**

The **AI Chat Assistant** is a modern Streamlit application that enables users to:

- 💬 **Chat with an AI assistant** powered by Groq’s ultra-fast **Llama 3.1 model**
- 📂 **Upload files** (CSV, TXT, PDF) for intelligent summaries
- 📊 **Analyze CSV data** with automated statistics, missing value detection & column insights
- 🧠 Maintain **conversation memory** for improved context
- 🎨 Enjoy a **clean, simple, and modern UI**

Perfect for **recruiters, students, developers, and data enthusiasts** exploring real-world LLM apps.

---

## 🖼️ **Screenshots**

### 🧠 Chat Interface  
A clean, modern interface for AI conversations.  
![Chat Screenshot](screenshots/chat.png)

### 📊 CSV Analyzer  
Upload CSV files and get instant insights.  
![CSV Screenshot](screenshots/csv.png)

### 📂 File Reader  
Analyze TXT & PDF files with automatic summarization.  
![File Reader Screenshot](screenshots/filereader.png)

> ℹ️ *Replace the image paths above with your actual GitHub image URLs after uploading them.*

---

## ✨ **Features**

### 💬 **AI Chat Interface**
- Powered by **Groq Llama 3.1**
- Fast responses with memory support

### 📂 **File Reader Module**
- Supports TXT & PDF  
- Extracts and summarizes text automatically

### 📊 **CSV Analyzer**
- Dataset preview  
- Missing value detection  
- Column-level insights  
- Automated summary & interpretation  

### 🎨 **Modern UI/UX**
- Styled chat bubbles  
- Sidebar shortcuts  
- Clean layout and responsive design  

---

## 🧱 **Tech Stack**

| Tool | Purpose |
|------|---------|
| **Python** | Core backend logic |
| **Streamlit** | UI & Web application |
| **Groq API (Llama 3.1)** | LLM engine |
| **Pandas** | CSV processing |
| **PyPDF2** | PDF extraction |
| **dotenv** | Environment variable handling |

---

## 📁 **Project Structure**



## 📁 **Project Structure**
```
AI-ASSISTANT/
│── app.py
│── file_reader.py
│── csv_analyzer.py
│── ui_style.py
│── requirements.txt
│── .gitignore
```

---

## 🛠️ **Running Locally**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Niroj7/AI-ASSISTANT.git
cd AI-ASSISTANT
```
<b>2️⃣ Install Dependencies</b>
```
pip install -r requirements.txt
```
<b>3️⃣ Add Your Groq API Key</b>

<i>Create a .env file:</i>
```
GROQ_API_KEY=your_api_key_here
```
<b>4️⃣ Run the App</b>
```
streamlit run app.py
```




