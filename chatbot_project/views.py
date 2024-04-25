#chatbot_project/views.py
import logging
from django.http import JsonResponse, HttpResponse
import requests
from transformers import AutoModelForSequenceClassification, AutoTokenizer, RagTokenForGeneration
from my_chatbot_app.chatbot_logic import generate_response

# Configure logging
logger = logging.getLogger(__name__)

def fetch_data_from_api(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        if 'application/json' in response.headers.get('Content-Type', ''):
            return response.json()
        else:
            logger.error(f'Invalid Content-Type for URL {url}: {response.headers.get("Content-Type")}')
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f'Failed to fetch data from {url}: {str(e)}')
        return None

def get_poverty_data():
    api_url = "http://api.worldbank.org/v2/country/BR/indicator/SI.POV.DDAY?format=json"
    return fetch_data_from_api(api_url)

def chatbot_response(request):
    user_input = request.GET.get('input', '')
    try:
        response = generate_response(user_input)
        return JsonResponse({'response': response})
    except Exception as e:
        logger.error(f"Failed to generate response: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

# Load RAG model and tokenizer
rag_model = AutoTokenizer.from_pretrained("facebook/rag-token-nq")
rag_tokenizer = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")

# Load language model
language_model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased')
language_tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def generate_response_rag(user_input):
    try:
        input_tokens = rag_tokenizer.encode(user_input, return_tensors='pt')
        output_ids = rag_model.generate(input_tokens['input_ids'], attention_mask=input_tokens['attention_mask'], max_length=50)
        response = rag_tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return response
    except Exception as e:
        logger.error(f"Error in RAG response generation: {str(e)}")
        return str(e)

def refine_response(response):
    try:
        response_tokens = language_tokenizer.encode(response, return_tensors='pt')
        output = language_model(response_tokens)
        refined_response = language_tokenizer.decode(output[0], skip_special_tokens=True)
        return refined_response
    except Exception as e:
        logger.error(f"Error refining response: {str(e)}")
        return str(e)

def chat(request):
    user_input = request.GET.get('question', '')
    try:
        response = generate_response(user_input)
        return JsonResponse({'response': response})
    except Exception as e:
        logger.error(f"Failed to generate response: {str(e)}")
        return JsonResponse({'error': 'Failed to process the request'}, status=500)

