# mendibeltz-maintenance

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Microsoft Foundry](https://img.shields.io/badge/Microsoft-Foundry-0078D4) ![MCP](https://img.shields.io/badge/GitHub-MCP-black) ![Status](https://img.shields.io/badge/status-academic%20project-lightgrey)

AI maintenance assistant for **Mendibeltz Wind Farm** (fictional), built with **Microsoft Foundry** as the Challenge Day 4 project of the Cloud Computing course (MADI, Universidad de Navarra).

The agent answers maintenance and safety questions from company documentation, analyses turbine data, and manages maintenance tickets as GitHub issues in this very repository.

## Table of contents

- [Features](#features)
- [How it works](#how-it-works)
- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
- [Real examples](#real-examples)
- [Maintenance tickets](#maintenance-tickets)
- [Troubleshooting](#troubleshooting)
- [Tech stack](#tech-stack)
- [Author](#author)

## Features

| Capability | What it does |
|---|---|
| **Custom instructions** | Maintenance-focused behavior: safety first, grounded in the company documents, with recommended actions and spare parts |
| **Knowledge base** | Company documents (safety procedure, alarm and failure-mode references, maintenance manual, service bulletins, spare-parts stock) stored in the Storage account of the Foundry resource and indexed for retrieval |
| **Code Interpreter** | Analysis of turbine data, such as SCADA temperatures, vibration and alarm history |
| **GitHub MCP** | Reads, comments on and labels maintenance tickets, which are the [Issues](../../issues) of this repository |
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
     procedures, alarms,          SCADA data analysis        read / comment on issues
     bulletins, spare parts                                          │
                                                                      ▼
                                                           Maintenance tickets
```

1. A technician reports an incident as a GitHub issue, or asks a question in the terminal.
2. The agent decides whether it needs the documents, the Code Interpreter or the GitHub tool.
3. If it needs GitHub, the terminal shows the exact call and waits for approval (`y/N`).
4. The agent answers with a diagnosis or decision, the recommended action, the spare parts needed and the safety precautions.

## Repository structure

| Path | Description |
|---|---|
| `agent.py` | Terminal chat client for the agent |
| `requirements.txt` | Python dependencies |
| `.env.example` | Template for environment variables (copy to `.env`) |
| `.github/ISSUE_TEMPLATE/maintenance_ticket.md` | Template for maintenance reports |

The company documents used as knowledge base are fictional course material and are not included in this repository.

## Getting started

### Prerequisites

- Python 3.10 or newer
- An Azure subscription with a Microsoft Foundry project
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) installed

### 1. Create the agent in the Foundry portal

1. Write the agent instructions (role, safety rules, answer format).
2. Enable **Code Interpreter**.
3. Upload the maintenance documents to the Storage account and attach them as knowledge.
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

When the agent wants to use the GitHub tool, the terminal shows the call and asks `Approve this call? [y/N]`.

## Real examples

| Ticket | Situation | Agent outcome |
|---|---|---|
| [#4](../../issues/4) | WTG-01: request to climb the tower for a yaw inspection with 16 m/s forecast at hub height | Climb **not approved**: the safety procedure (HR-HSE-003) limits tower and nacelle work to 15 m/s. Postpone, use at least 2 qualified technicians, work permit and full LOTO |
| [#1](../../issues/1) | WTG-03: metallic noise from the gearbox, alarms E-101 and E-110, oil at 80 °C | Diagnosis consistent with high-speed shaft bearing wear. Urgent action plan, spare part GB-HSB-22 (lead time 6 weeks) and safety precautions |
| [#5](../../issues/5) | WTG-02: work order to verify pitch calibration of blade B | Work order with reason, urgency, safety precautions and a note on the documents still to consult before execution |

## Maintenance tickets

Tickets are GitHub issues, one per incident, labelled by turbine (WTG-01 to WTG-04) and type (for example `work order`). The template in `.github/ISSUE_TEMPLATE/` asks for the reporter, the date, the turbine and a description with alarms and SCADA values.

## Troubleshooting

| Problem | Fix |
|---|---|
| `KeyError: 'FOUNDRY_PROJECT_ENDPOINT'` | The `.env` file is missing or empty. Copy `.env.example` and fill it in. |
| Authentication error | Run `az login` again and check that your account has access to the Foundry project. |
| Agent not found | `FOUNDRY_AGENT_NAME` must match the agent name in the portal exactly. |
| Agent ignores the documents | Check in the portal that the PDFs are attached to the agent as knowledge. |

## Tech stack

Microsoft Foundry · Azure AI Projects SDK · Azure Storage · Model Context Protocol (GitHub MCP) · Python

## Author

**Alexander Delgado Sarriegui**, Double MSc in Industrial Engineering and Artificial Intelligence, Universidad de Navarra. Cloud Computing, 2026.
