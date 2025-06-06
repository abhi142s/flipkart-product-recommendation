from flask import Flask, render_template, request
from flipkart.retrieval_generation import generation
from flipkart.data_ingestion import data_ingestion
from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

from flipkart.retrieval_generation import get_session_history


from dotenv import load_dotenv
import os
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model = "llama-3.3-70b-versatile", temperature=0)

chat_history = []
store = {}

vstore, random = data_ingestion("done")

chain = generation(vstore)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get",methods = ["POST","GET"])
def chat():
    if request.method == "POST":
        msg = request.form["msg"]
        input = msg
        result = chain.invoke(
        {"input": input},
        config = {
            "configurable" : {"session_id" : "abhi142s"}
        },
        )["answer"]
        return str(result)
    
if __name__ == '__main__':
    app.run(host = "0.0.0.0",port=5000,debug=True)


    
