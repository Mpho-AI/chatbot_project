from django.http import JsonResponse
from transformers import RagModel, RagTokenizer, AutoModelForSequenceClassification, AutoTokenizer
import requests

# Load data sources
try:
    poverty_data = requests.get('https://data.worldbank.org/indicator/SI.POV.DDAY?locations=1W-BR').json()
    internet_data = requests.get('https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W-BR').json()
    unemployment_data = requests.get('https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?locations=1W-BR').json()
except requests.exceptions.RequestException as e:
    print(f'Error fetching data: {e}')
    poverty_data = None
    internet_data = None
    unemployment_data = None

# Define the RAG model and tokenizer
rag_model = RagModel.from_pretrained('facebook/rag-base')
rag_tokenizer = RagTokenizer.from_pretrained('facebook/rag-base')

# Load language model
language_model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased')
language_tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def chatbot_response(request):
    try:
        user_input = request.GET.get('input')
        response = generate_response(user_input)
        return JsonResponse({'response': response})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def generate_response(user_input):
    try:
        # Preprocess user input
        input_text = preprocess_input(user_input)

        # Generate response using RAG model
        response = generate_response_rag(input_text)

        # Postprocess response
        response = postprocess_response(response)

        return response
    except Exception as e:
        return str(e)

def preprocess_input(user_input):
    # Tokenize user input
    input_tokens = rag_tokenizer.encode(user_input, return_tensors='pt')

    # Convert tokens to input IDs
    input_ids = input_tokens['input_ids'].flatten()

    return input_ids

def generate_response_rag(input_ids):
    try:
        # Generate response using RAG model
        output = rag_model.generate(input_ids, max_length=50)

        # Convert output to text
        response = rag_tokenizer.decode(output[0], skip_special_tokens=True)

        # Use language model to refine response
        response = refine_response(response, language_model, language_tokenizer)

        return response
    except Exception as e:
        return str(e)

def refine_response(response, language_model, language_tokenizer):
    try:
        # Tokenize response
        response_tokens = language_tokenizer.encode(response, return_tensors='pt')

        # Classify response using language model
        output = language_model(response_tokens)

        # Get the most likely response
        response = language_tokenizer.decode(output[0], skip_special_tokens=True)

        return response
    except Exception as e:
        return str(e)

def postprocess_response(response):
    # Check if response is related to Brazil
    if 'Brazil' in response:
        # Retrieve relevant data from data sources
        data = retrieve_data(response)

        # Incorporate data into response
        response = incorporate_data(response, data)

    return response

def retrieve_data(response):
    # Retrieve relevant data from data sources
    if 'poverty' in response:
        data = poverty_data['value']
    elif 'internet' in response:
        data = internet_data['value']
    elif 'unemployment' in response:
        data = unemployment_data['value']
    else:
        data = None

    return data

def incorporate_data(response, data):
    # Incorporate data into response
    if data is not None:
        response += f' According to the World Bank, {data}% of the population is affected.'

    return response