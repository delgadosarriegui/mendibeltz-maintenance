# mendibeltz-maintenance

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Microsoft Foundry](https://img.shields.io/badge/Microsoft-Foundry-0078D4) ![MCP](https://img.shields.io/badge/GitHub-MCP-black) ![Status](https://img.shields.io/badge/status-academic%20project-lightgrey)

AI maintenance assistant for **Mendibeltz Wind Farm** (fictional), built with **Microsoft Foundry** as the Challenge Day 4 project of the Cloud Computing course (MADI, Universidad de Navarra).

The agent answers maintenance questions from technical documentation, runs calculations, and manages maintenance tickets as GitHub issues in this very repository.

## Table of contents

- [Features](#features)
- [How it works](#how-it-works)
- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
- [Example conversation](#example-conversation)
- [Maintenance tickets](#maintenance-tickets)
- [Troubleshooting](#troubleshooting)
- [Tech stack](#tech-stack)
- [Author](#author)

## Features

| Capability | What it does |
|---|---|
| **Custom instructions** | Maintenance-focused behavior with safety reminders and a fixed ticket format ([docs/agent_instructions.md](docs/agent_instructions.md)) |
| **Knowledge base** | Technical PDFs stored in the Storage account of the Foundry resource and indexed for retrieval ([manual](docs/mendibeltz_maintenance_manual.pdf)) |
| **Code Interpreter** | Calculations and data analysis, such as availability, downtime or trends |
| **GitHub MCP** | Lists, creates and comments on maintenance tickets, which are the [Issues](../../issues) of this repository |
| **Terminal client** | Python chat ([agent.py](agent.py)) that asks for confirmation before every tool call |

## How it works

```text
┌──────────────┐   Foundry SDK    ┌────────────────┐
│  Terminal    │ ───────────────► │  Foundry agent │
│  (agent.py)  │ ◄─────────────── │                │
└──────────────┘     answers      └───────┬────────┘
                                          │
              ┌───────────────────────────┼───────────────────────────┐
              ▼                           ▼                           ▼
     Knowledge base (PDFs)        Code Interpreter           GitHub MCP tool
     manuals, alarm codes         calculations, data         read / create issues
                                                                      │
                                                                      ▼
                                                           Maintenance tickets
```

1. The user asks a question in the terminal.
2. The agent decides whether it needs the documents, the Code Interpreter or the GitHub tool.
3. If it needs GitHub, the terminal shows the exact call and waits for the user to approve it (`y/N`).
4. The agent answers, citing the document it used.

## Repository structure

| Path | Description |
|---|---|
| `agent.py` | Terminal chat client for the agent |
| `requirements.txt` | Python dependencies |
| `.env.example` | Template for environment variables (copy to `.env`) |
| `docs/mendibeltz_maintenance_manual.pdf` | Maintenance manual used as knowledge base |
| `docs/agent_instructions.md` | System instructions of the agent |
| `.github/ISSUE_TEMPLATE/maintenance_ticket.md` | Template for maintenance tickets |

## Getting started

### Prerequisites

- Python 3.10 or newer
- An Azure subscription with a Microsoft Foundry project
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) installed

### 1. Create the agent in the Foundry portal

1. Paste the instructions from `docs/agent_instructions.md`.
2. Enable **Code Interpreter**.
3. Upload the PDFs from `docs/` as the knowledge base.
4. Add the **GitHub MCP** tool.

### 2. Install the client

```bash
git clone https://github.com/delgadosarriegui/mendibeltz-maintenance.git
cd mendibeltz-maintenance
python -m venv .venv
.venv\Scripts\activate          # Windows (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```

### 3. Configure

Copy `.env.example` to `.env` and fill in:

```env
FOUNDRY_PROJECT_ENDPOINT=https://<your-resource>.services.ai.azure.com/api/projects/<your-project>
FOUNDRY_AGENT_NAME=<your-agent-name>
```

### 4. Run

```bash
az login
python agent.py
```

## Example conversation

```text
You: What should I check if the gearbox oil temperature alarm appears?
Agent: Alarm A101 (oil temperature above 75 °C). Check the oil level and the filter,
       and inspect the cooling fan. Stop the turbine if it exceeds 85 °C.
       Source: Maintenance Manual, section 3. Remember to apply lock-out/tag-out.

You: Open a high-priority ticket for WT-03: abnormal vibration at the main bearing.

[tool request] github.create_issue({...})
Approve this call? [y/N]: y

Agent: Ticket created: "[WT-03] Abnormal vibration at main bearing" (priority High).
```

## Maintenance tickets

Tickets are GitHub issues that follow the template in `.github/ISSUE_TEMPLATE/`:

| Field | Values |
|---|---|
| Turbine | WT-XX |
| Priority | Critical, High, Medium, Low |
| Type | Corrective, Preventive, Inspection |
| Content | Symptom, suspected component, recommended action, status |

## Troubleshooting

| Problem | Fix |
|---|---|
| `KeyError: 'FOUNDRY_PROJECT_ENDPOINT'` | The `.env` file is missing or empty. Copy `.env.example` and fill it in. |
| Authentication error | Run `az login` again and check that your account has access to the Foundry project. |
| Agent not found | `FOUNDRY_AGENT_NAME` must match the agent name in the portal exactly. |
| Agent ignores the manual | Check in the portal that the PDFs are attached to the agent as knowledge. |

## Tech stack

Microsoft Foundry · Azure AI Projects SDK · Azure Storage · Model Context Protocol (GitHub MCP) · Python

## Author

**Alexander Delgado Sarriegui**, Double MSc in Industrial Engineering and Artificial Intelligence, Universidad de Navarra. Cloud Computing, 2026.
