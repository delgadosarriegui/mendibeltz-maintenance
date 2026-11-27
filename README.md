# mendibeltz-maintenance

![Tickets](https://img.shields.io/badge/maintenance-tickets-orange) ![Agent](https://img.shields.io/badge/agent-WindCare-0078D4) ![Status](https://img.shields.io/badge/status-academic%20project-lightgrey)

Maintenance tickets of the fictional **Mendibeltz Wind Farm** (Haizea Renewables, 4 EKW-3.2 turbines, WTG-01 to WTG-04), managed as **GitHub Issues**.

> **This repository is one half of the project.**
> `mendibeltz-maintenance` (this repo) is the wind farm: every incident and work order is an [Issue](../../issues).
> [`windcare-agent`](https://github.com/delgadosarriegui/windcare-agent) is the AI agent (Microsoft Foundry) that reads these tickets, diagnoses them and writes its recommendation back as a comment.

Built for the MADI Cloud Computing Challenge (Day 4).

## How the two repositories work together

```text
Technician ──► opens an Issue ──► mendibeltz-maintenance
                                         │  GitHub MCP
                                         ▼
                                  WindCare agent (windcare-agent)
                                   · company documents (manual, alarms, safety, spare parts)
                                   · SCADA data analysis
                                         │
                                         ▼
                      Comment with diagnosis, action, spare parts and safety precautions
```

1. A technician or the control room opens an issue using the [maintenance report template](.github/ISSUE_TEMPLATE/maintenance_ticket.md).
2. The WindCare agent reads the open issues through the GitHub MCP server.
3. It checks the company documents and the SCADA data, and comments with a diagnosis.
4. When asked, it creates new issues as work orders. It never closes an issue unless explicitly asked.

## Tickets

Issues are labelled by turbine (`WTG-01` to `WTG-04`) and by type (for example `work order`).

| Ticket | Turbine | Situation | Agent outcome |
|---|---|---|---|
| [#1](../../issues/1) | WTG-03 | Metallic noise from the gearbox, alarms E-101 and E-110 | Urgent: high-speed shaft bearing wear, plan endoscopy and oil sampling, spare part GB-HSB-22 |
| [#2](../../issues/2) | WTG-02 | Production lower than neighbour turbines | Investigation leading to a pitch calibration work order |
| [#3](../../issues/3) | WTG-04 | Generator temperature warning E-201 | Open |
| [#4](../../issues/4) | WTG-01 | Request to climb the tower with 16 m/s forecast | Refused: the limit is 15 m/s (HR-HSE-003) |
| [#5](../../issues/5) | WTG-02 | Work order: verify pitch calibration of blade B | Work order created with safety precautions |

## Report an incident

1. Go to **Issues → New issue** and choose **Maintenance report**.
2. Fill in who reports it, the date, the turbine and a description with alarm codes and SCADA values.
3. Add a question for the agent, for example: "Is any action required?"

## Related repository

- [`windcare-agent`](https://github.com/delgadosarriegui/windcare-agent): agent definition, terminal and web chat, setup and architecture.

## Author

**Alexander Delgado Sarriegui**, Double MSc in Industrial Engineering and Artificial Intelligence, Universidad de Navarra. Cloud Computing, 2026.
