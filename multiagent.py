# This code demonstrates how to use multiple agents to process data,
#  generate reports, and send emails using Azure AI services.
# Explanation of the Code
# Configuration:
# Sets up the Azure AI client using a connection string and credentials.
# Initializes the Bing connection (if needed).

# EmailSender Class:
# Defines a class to handle sending emails using Gmail's SMTP server.

# Creating Agents:
# Creates three agents: one for data processing, one for report generation, and one for sending emails.

# Processing Data:
# Creates a thread and message for the data processing agent to process the provided data.
# Runs the agent and retrieves the processed data.

# Generating Report:
# Creates a thread and message for the report generation agent to generate a report based on the processed data.
# Runs the agent and retrieves the generated report.

# Sending Email:
# Uses the EmailSender class to send the generated report via email.

# Cleanup:
# Deletes the agents once their tasks are completed.

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import BingGroundingTool
from azure.ai.projects.models import MessageTextContent
project_connection_string="eastus.api.azureml.ms;fxxx1d2-9b1c-49d5-xxxx-xxxx;savyaiagent;ai-basic-project-isxxz5"
# Create an Azure AI Client from a connection string, copied from your Azure AI Foundry project.
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(), conn_str=project_connection_string
)
bing_connection = project_client.connections.get(
    connection_name="bin"
)
class EmailSender:
    def send_email(self, subject, body, to_email):
        from_email = "smxxxx@xxxx.com"
        password = "xxx xxx xxx xxxx"  # Use the App Password generated from your Google account

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
            server.starttls()
            server.login(from_email, password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

with project_client:
    # Create Agent 1 for data processing
    agent1 = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="data-processor",
        instructions="You are an agent that processes data.",
    )
    print(f"Created agent1, agent ID: {agent1.id}")

    # Create Agent 2 for report generation
    agent2 = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="report-generator",
        instructions="You are an agent that generates reports based on processed data.",
    )
    print(f"Created agent2, agent ID: {agent2.id}")

    # Create Agent 3 for sending email
    email_sender = EmailSender()

    # Create a thread for Agent 1
    thread1 = project_client.agents.create_thread()
    print(f"Created thread1, thread ID: {thread1.id}")

    # Create a message for Agent 1 to process data
    message1 = project_client.agents.create_message(
        thread_id=thread1.id,
        role="user",
        content="Process the following data: Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    print(f"Created message1, message ID: {message1.id}")

    # Run Agent 1
    run1 = project_client.agents.create_and_process_run(thread_id=thread1.id, assistant_id=agent1.id)
    print(f"Run1 finished with status: {run1.status}")

    if run1.status == "failed":
        print(f"Run1 failed: {run1.last_error}")

    # Get processed data from Agent 1
    messages1 = project_client.agents.list_messages(thread_id=thread1.id)
    processed_data = messages1.get_last_text_message_by_sender("assistant").text.value
    print(f"Processed Data: {processed_data}")

    # Create a thread for Agent 2
    thread2 = project_client.agents.create_thread()
    print(f"Created thread2, thread ID: {thread2.id}")

    # Create a message for Agent 2 to generate a report
    message2 = project_client.agents.create_message(
        thread_id=thread2.id,
        role="user",
        content=f"Generate a report based on the following processed data: {processed_data}",
    )
    print(f"Created message2, message ID: {message2.id}")

    # Run Agent 2
    run2 = project_client.agents.create_and_process_run(thread_id=thread2.id, assistant_id=agent2.id)
    print(f"Run2 finished with status: {run2.status}")

    if run2.status == "failed":
        print(f"Run2 failed: {run2.last_error}")

    # Get the report from Agent 2
    messages2 = project_client.agents.list_messages(thread_id=thread2.id)
    report = messages2.get_last_text_message_by_sender("assistant").text.value
    print(f"Generated Report: {report}")

    # Send the report via email using Agent 3
    email_subject = "Generated Report"
    email_body = f"Here is the generated report:\n\n{report}\n\nContinuous monitoring of revenue trends is advised for making informed decisions and adjusting business strategies accordingly.\n\nFor any further analysis or additional metrics, please feel free to reach out."
    recipient_email = "xxx@microsoft.com"
    email_sender.send_email(email_subject, email_body, recipient_email)

    # Delete the agents once done
    project_client.agents.delete_agent(agent1.id)
    project_client.agents.delete_agent(agent2.id)
    print("Deleted agents")
