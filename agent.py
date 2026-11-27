"""Terminal client for the Mendibeltz maintenance agent (Microsoft Foundry).

The agent itself (instructions, Code Interpreter, PDF knowledge base and GitHub MCP)
is created in the Foundry portal. This script only opens a chat with it from the terminal.
"""

import os  # reads environment variables

from azure.ai.projects import AIProjectClient  # client for the Foundry project
from azure.identity import DefaultAzureCredential  # uses your `az login` session
from dotenv import load_dotenv  # loads variables from the .env file

load_dotenv()  # reads .env so os.environ contains your endpoint and agent name

ENDPOINT = os.environ["FOUNDRY_PROJECT_ENDPOINT"]  # project endpoint, copied from the Foundry portal
AGENT_NAME = os.environ["FOUNDRY_AGENT_NAME"]  # name of the agent created in the portal

# Tells the Responses API which agent must answer (instead of a plain model)
AGENT_REF = {"agent_reference": {"name": AGENT_NAME, "type": "agent_reference"}}


def send(openai_client, conversation_id, payload):
    """Send one request to the agent inside the given conversation and return the response."""
    return openai_client.responses.create(  # calls the agent
        conversation=conversation_id,  # keeps the chat history on the server side
        input=payload,  # user text, or a list with approval decisions
        extra_body=AGENT_REF,  # routes the call to our agent
    )


def ask(openai_client, conversation_id, text):
    """Ask the agent a question, handling tool approvals (GitHub MCP), and return its answer."""
    response = send(openai_client, conversation_id, text)  # first call with the user's question

    while True:  # the agent may need several approvals before answering
        requests = [item for item in response.output if item.type == "mcp_approval_request"]  # pending tool calls
        if not requests:  # nothing to approve, the answer is ready
            break

        decisions = []  # approvals/rejections that we will send back
        for req in requests:
            print(f"\n[tool request] {req.server_label}.{req.name}({req.arguments})")  # shows what the agent wants to do
            ok = input("Approve this call? [y/N]: ").strip().lower() == "y"  # asks the user for permission
            decisions.append(
                {
                    "type": "mcp_approval_response",  # message type expected by the API
                    "approval_request_id": req.id,  # which request we are answering
                    "approve": ok,  # True to allow, False to reject
                }
            )
        response = send(openai_client, conversation_id, decisions)  # agent continues after our decision

    return response.output_text  # final text answer from the agent


def main():
    """Open a chat loop in the terminal."""
    credential = DefaultAzureCredential()  # authenticates with your Azure login
    with AIProjectClient(endpoint=ENDPOINT, credential=credential) as project:  # connects to the project
        openai_client = project.get_openai_client()  # OpenAI-compatible client bound to the project
        conversation = openai_client.conversations.create()  # new conversation (memory of this chat)

        print(f"Connected to agent '{AGENT_NAME}'. Type 'exit' to quit.\n")  # expected output: connection message
        while True:
            question = input("You: ").strip()  # reads the user's question
            if question.lower() in {"exit", "quit"}:  # exit condition
                break
            if not question:  # ignore empty lines
                continue
            print(f"\nAgent: {ask(openai_client, conversation.id, question)}\n")  # prints the agent's answer


if __name__ == "__main__":  # runs main() only when executed as a script
    main()
