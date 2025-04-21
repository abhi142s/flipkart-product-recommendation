# Flipkart Product Recommendation Chatbot

This is a lightweight, AI-powered chatbot designed to help users ask product-related questions, specifically around **earphones and audio products**, based on Flipkart-style product data and reviews.

It leverages:
- Natural Language Processing for user queries
- Vector similarity search with AstraDB
- A custom conversational RAG (retrieval-augmented generation) pipeline using LangChain
- A modern, Bootstrap-styled web interface built in Flask

---

## 🔧 Features
- 💬 Ask product comparison and feature questions like "Which Bluetooth earbuds are waterproof?"
- 🧠 Personalized chat memory with session tracking
- 🧾 Markdown/HTML response formatting support for clean bot answers
- 🎨 Beautiful, mobile-responsive chatbot UI
- 📁 Vector database with semantic search over product reviews

---

## 📁 Project Structure

```
flipkar-product-recommendation/
├── app.py                    # Flask app runner
├── template.py              # Auto-creates project files/folders
├── setup.py                 # Package config
├── requirements.txt         # Python dependencies
├── flipkart/                # Core Python package
│   ├── __init__.py
│   ├── data_converter.py    # Converts CSV reviews to documents
│   ├── data_ingestion.py    # Embeds and stores data in AstraDB
│   ├── retrieval_generation.py # Builds the conversational chain
├── static/                  # Static assets
│   └── style.css            # Custom chatbot styling
├── templates/
│   └── index.html           # Frontend chatbot interface
├── Data/                    # Your raw product review files
│   └── flipkart_product_review.csv
```

---

## 🚀 How to Run Locally

### 1. 🧪 Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 2. 📦 Install Requirements
```bash
pip install -r requirements.txt
```

### 3. 🔑 Set Environment Variables
Create a `.env` file with:
```
ASTRA_DB_API_ENDPOINT=...
ASTRA_DB_APPLICATION_TOKEN=...
ASTRA_DB_KEYSPACE=...
GROQ_API=...
```

### 4. 📥 Load Data
Run:
```bash
python flipkart/data_ingestion.py
```
You’ll see something like:
```
Inserted 1 documents.
```

### 5. 🖥️ Start the Chatbot
```bash
python app.py
```
Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Technologies Used
- **LangChain** (retriever chains, prompt templates)
- **AstraDB** + **Cassandra Vector Store** for embedding search
- **Groq LLaMA-3 API** for conversational generation
- **Flask** for backend
- **Bootstrap** + **jQuery** for frontend UI

---

## 🪄 Example Questions
- "What's the best Bluetooth earphone under ₹2000?"
- "Is the Realme Buds 2 waterproof?"
- "Compare Realme Buds 2 and Boat Airdopes."

---

## 📌 Notes
- The chatbot supports **HTML-formatted responses** (including bold, lists, and line breaks).
- You can customize the starting message and embed images/backgrounds in the `style.css`.

---

## 📃 License
MIT License

---

## 👤 Author
**Abhisrinivasan**
