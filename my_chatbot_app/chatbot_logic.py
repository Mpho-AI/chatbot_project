# my_chatbot_app/chatbot_logic.py
#from transformers import RagTokenizer, RagTokenForGeneration, #RagRetriever
# Load model directly
from transformers import AutoTokenizer, RagTokenForGeneration

tokenizer = AutoTokenizer.from_pretrained("facebook/rag-token-nq")
model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")


def setup_rag_model():
    # tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    # retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", indexed_dataset=None)  # Configure as per your dataset
    # model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)
    tokenizer = AutoTokenizer.from_pretrained("facebook/rag-token-nq")
    model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")
    return tokenizer, model

def generate_response(question):
    tokenizer, model = setup_rag_model()
    inputs = tokenizer(question, return_tensors="pt")
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

