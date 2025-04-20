import pandas as pd
from langchain_core import Document

def dataconverter():
    product_data = pd.read_csv("Data/flipkart_product_review.csv")

    data = product_data[["product_title","review"]]

    product_list = []

    #Iterate over the dataframe

    for index,row in data.iterrows():
        object = {
        "product_name" : row["product_title"],
        "review" : row["review"]
    }

    #   Apend the object to product list
    product_list.append(object)
    docs = []
    for entry in product_list:
        metadata = {"product_name":entry["product_name"]}
        doc = Document(page_content = entry['review'],metadata = metadata)
        docs.append(doc)
    return docs