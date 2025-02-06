# This code demonstrates a unimodal approach to sentiment analysis using Azure's Cognitive Services.
# It is considered unimodal because it processes only one type of input, which in this case is textual data. 
# The code focuses solely on analyzing the sentiment of text-based inputs, without integrating any additional modes such as images, audio, or video.

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Set your Azure credentials
endpoint = "https://agent-ai-servicesisz5.cognitiveservices.azure.com//"
api_key = "1KgkFVogcQ5MSlTsxyajFx77iUBvDI7nICse0ZhnhuGE8CISCMqfJQQJ99BAACYeBjFXJ3w3AAAAACOGg8ZR"

# Authenticate to the service
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

# Example text for sentiment analysis
documents = [
    "I love using Azure for building AI models!",
    "The product was good, but the support could be improved.",
    "I'm disappointed with the recent update."
]

# Perform sentiment analysis
response = client.analyze_sentiment(documents)

# Display the results
for idx, doc in enumerate(response):
    print(f"Document {idx}: Sentiment - {doc.sentiment}")
