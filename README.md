# mendibeltz-maintenance

AI agent for wind turbine maintenance at **Mendibeltz Wind Farm** (fictional), built with **Microsoft Foundry** as the Challenge Day 4 project of the Cloud Computing course (MADI, Tecnun – University of Navarra).

The agent answers maintenance questions using technical documentation (PDFs) and manages maintenance tickets as GitHub issues in this repository.

## Features
- **Foundry agent** with custom instructions for wind turbine maintenance.
- **Code Interpreter** for data analysis and calculations.
- **Knowledge base**: technical PDFs stored in Azure Blob Storage and indexed for retrieval.
- **GitHub MCP**: the agent reads and creates maintenance tickets as issues in this repo.
- **Terminal client** in Python that connects to the agent through the Foundry SDK.

## Architecture
User (terminal) → Python client (Foundry SDK) → Foundry Agent → [Code Interpreter | PDFs in Storage | GitHub MCP → Issues]

## Repository structure
- `agent.py`: [terminal client that connects to the agent]
- `docs/`: [maintenance PDFs used as knowledge base]
- `requirements.txt`: [Python dependencies]
- `.env.example`: [required environment variables, no secrets]

## Setup
1. Clone the repo and create a virtual environment.
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in your Foundry project endpoint and agent name.
4. Sign in to Azure (`az login`) and run `python agent.py`.

## Example usage
> "What is the maintenance procedure for a gearbox oil temperature alarm?"
> "Open a ticket for turbine WT-03 with abnormal vibration."

## Maintenance tickets
Tickets live in the [Issues](../../issues) tab (labels: [severity / turbine]).

## Tech stack
Microsoft Foundry · Azure AI Agent Service · Azure Blob Storage · Python · Model Context Protocol (GitHub MCP)

## Author
Alexander Delgado Sarriegui, MADI – Cloud Computing, 2026.
