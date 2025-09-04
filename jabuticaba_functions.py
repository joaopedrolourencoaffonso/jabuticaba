def abrirArquivoSimples():
    file = open("temp.txt","r").read();
    return file;

def send_openai_request(api_key, input_text, requests):
    url = "https://api.openai.com/v1/responses"
    
    # Set headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Define the payload
    data = {
        "model": "gpt-4",
        "input": input_text
    }
    
    # Send POST request
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Example usage:
#api_key = "your_openai_api_key"
#input_text = "Write a one-sentence bedtime story about a unicorn."
#result = send_openai_request(api_key, input_text)
