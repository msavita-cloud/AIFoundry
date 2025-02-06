# This code demonstrates the implementation of a multimodal AI model using OpenAI's API through the Azure Foundry service. 
# The model processes both textual and visual inputs, making it multimodal. 
# Specifically, it encodes an image using Base64 and feeds it along with textual instructions into the OpenAI model for a chat completion task. 
# The model is set up with a GPT-4 instance, where it takes a sequence of prompts (e.g., generating an image of a futuristic cityscape) as user input, 
# allowing it to interpret both text-based interactions and image-based content

import openai
import base64
from openai import AzureOpenAI  

# Open AI endpoint and key from Azure foundry Project endpoints section
client = AzureOpenAI(  
    azure_endpoint="https://agent-ai-servicesisz5.openai.azure.com/",  /
    api_key="xxxxxxx",  
    api_version="2024-05-01-preview",
)

# Image and Text Input (Multimodal)
image_url = "printed_text.jpg"
IMAGE_PATH = "https://nutritionstripped.com/wp-content/uploads/2016/03/nutritionlabelmainimage-1.jpg"
encoded_image = base64.b64encode(open(image_url, 'rb').read()).decode('ascii')
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Please generate an image of a futuristic cityscape"
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Please generate an image of a futuristic cityscape"
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Please generate an image of a futuristic cityscape"
            }
        ]
    }
] 
    
# Include speech result if speech is enabled  
messages = chat_prompt 

completion = client.chat.completions.create(  
    model="gpt-4o-mini",  
    messages=messages,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False  
)  
  
print(completion.to_json())  
