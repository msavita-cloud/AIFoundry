AI Workshop
# Azure AI Foundry

Azure AI Foundry is a comprehensive platform provided by Microsoft Azure for building, deploying, and managing AI-driven applications. It combines various AI tools and services, enabling seamless integration and project management.

## How Azure AI Foundry is Useful for AI Projects and how to get started with foundry project
### Azure AI Project SDK and Azure Identity

### azure-ai-projects

**Description**: This package provides the Azure AI Project SDK, which is a comprehensive toolchain designed to simplify the development of AI applications on Azure. It enables developers to access various AI models and services through a single interface.

**Functionality**: Allows you to create, manage, and deploy AI projects using Azure AI Foundry. It provides programmatic access to Azure AI capabilities, making it easier to integrate different AI services into your applications.

### azure-identity

**Description**: This package provides Azure Active Directory (Azure AD) token authentication support across the Azure SDK. It includes various credential classes for authenticating with Azure services.

**Functionality**: Enables secure authentication to Azure services using Azure AD credentials. It supports different authentication methods, such as managed identities, environment variables, and interactive browser authentication.

### Streamlined Development
- Simplifies the development process by providing a robust toolkit for seamless integration of Azure AI services.
- Ensures that developers can focus on building and fine-tuning their models without worrying about compatibility issues.
### Comprehensive AI Capabilities
- Offers a wide range of AI capabilities, including image analysis, speech-to-text, language understanding, and more.
- Allows developers to build versatile AI applications that can handle multiple tasks.
### Scalability and Flexibility
- Designed to be scalable, allowing organizations to start small and expand their AI capabilities as needed.
- Ensures that AI projects can grow and adapt to changing business requirements.
## Example Use Case

Imagine a company that wants to build an AI-driven customer support system. Using Azure AI Foundry, the company can:

1. **Develop Custom Models**: Build and train custom machine learning models to understand customer queries and provide accurate responses.
2. **Integrate OpenAI Models**: Use OpenAI models to generate natural language responses and enhance the conversational experience.
3. **Leverage Cognitive Services**: Utilize Azure Cognitive Services for speech-to-text conversion, language understanding, and sentiment analysis.
4. **Collaborate Across Teams**: Enable data scientists, engineers, and business professionals to collaborate on the project, ensuring that the AI system meets business goals.
5. **Deploy and Manage**: Deploy the AI system on Azure and manage it using the tools provided by Azure AI Foundry.
   
**Prerequisites**
**Azure Subscription with access to Azure AI Foundry.<br>
**Azure AI Foundry deployed and ready with a model..<br>
**Azure Identity Library and Azure AI Project SDK installed:.<br>
**In vs code: pip install azure-ai-projects azure-identity
## Difference Between Multimodal and Unimodal AI Models
| Feature        | Unimodal AI Models                                                                 | Multimodal AI Models                                                                |
|----------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| **Definition** | Designed to analyze and process a single type of data, such as text, images, or audio. | Combine multiple data sources and integrate them into a common system capable of handling text, images, video, and audio simultaneously. |
| **Example**    | A text analytics model that performs sentiment analysis on text data.             | A model that can understand and generate both text and images, such as GPT-4o, which integrates text and images in a single model. |
| **Use Case**   | Writing text, recognizing objects in photos, speech-to-text conversion.            | Enhancing accuracy and responsiveness in human-computer interactions, generating content that includes both text and images. |
| **Endpoints**   | Typically involve a single AI model endpoint that handles one type of data.        | May involve multiple AI model endpoints or a single endpoint that can handle multiple types of data. |




