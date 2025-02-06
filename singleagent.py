import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import MessageTextContent

# Configuration
project_connection_string = "eastus.api.azureml.ms;xxx-9b1c-x-83e4-x;xxxagent;ai-basic-project-ixxz5"

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
