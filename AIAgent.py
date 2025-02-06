"""
DESCRIPTION:
    This sample demonstrates how to use basic agent operations from
    the Azure Agents service using a synchronous client.

USAGE:
     Before running the sample:
     pip install azure-ai-projects azure-identity

    Set these  variables with your own values:
    1) PROJECT_CONNECTION_STRING - The project connection string, as found in the overview page of your
       Azure AI Foundry project.
    2) MODEL_DEPLOYMENT_NAME - The deployment name of the AI model, as found under the "Name" column in 
       the "Models + endpoints" tab in your Azure AI Foundry project.

       # Explanation of the Code
# Configuration:
# Sets up the Azure AI client using a connection string and credentials.

# Creating an Agent:
# Creates an agent named "my-assistant" with instructions to be a helpful assistant.

# Creating a Thread:
# Creates a thread for the agent to handle the conversation.

# Creating a Message:
# Creates a message for the agent with the content "What are the benefits of using Azure AI services?"

# Running the Agent:
# Runs the agent to process the message and perform its task.
# Polls the run status until it is completed.

# Deleting the Agent:
# Deletes the agent once its task is completed.

# Listing and Displaying Messages:
# Lists and displays the messages from the agent, showing the conversation.
"""

import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import MessageTextContent

# Configuration
project_connection_string = "eastus.api.azureml.ms;XXX-9b1c-xxx-83e4-xxx;savxxaiagent;ai-basic-project-ixx"

# Create an Azure AI Client from a connection string, copied from your Azure AI Foundry project.
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=project_connection_string,
)

with project_client:

    # Create an agent
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-assistant",
        instructions="You are a helpful assistant",
    )
    print(f"Created agent, agent ID: {agent.id}")

    # Create a thread for the agent
    thread = project_client.agents.create_thread()
    print(f"Created thread, thread ID: {thread.id}")

    # Create a message for the agent
    message = project_client.agents.create_message(thread_id=thread.id, role="user", content="What are the benefits of using Azure AI services?")
    print(f"Created message, message ID: {message.id}")

    # Create and run the agent
    run = project_client.agents.create_run(thread_id=thread.id, assistant_id=agent.id)

    # Poll the run as long as run status is queued or in progress
    while run.status in ["queued", "in_progress", "requires_action"]:
        # Wait for a second
        time.sleep(1)
        run = project_client.agents.get_run(thread_id=thread.id, run_id=run.id)
        print(f"Run status: {run.status}")

    # Delete the agent once done
    project_client.agents.delete_agent(agent.id)
    print("Deleted agent")

    # List and display messages
    messages = project_client.agents.list_messages(thread_id=thread.id)

    # The messages are following in the reverse order,
    # we will iterate them and output only text contents.
    for data_point in reversed(messages.data):
        last_message_content = data_point.content[-1]
        if isinstance(last_message_content, MessageTextContent):
            print(f"{data_point.role}: {last_message_content.text.value}")

    print(f"Messages: {messages}")
