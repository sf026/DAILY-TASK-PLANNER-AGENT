## **Daily Task Planner Agent**
### Project Overview

The Daily Task Planner Agent is an AI-powered web application that helps users organize their daily goals into a clear, realistic, and time-based plan.
It uses a task-specific AI agent built with CrewAI and is deployed through a Flask web interface for easy interaction.

This project demonstrates how agent-based AI systems can be integrated into real-world applications to improve productivity.

### Problem Statement
Many people struggle to:
* Organize multiple daily tasks
* Allocate time effectively
* Maintain a balanced daily schedule
* Manual planning is often inefficient and inconsistent.

### Solution
This project provides:
* An AI Productivity Planner Agent
* A simple web UI to input daily tasks
* An automatically generated daily schedule with logical ordering and time slots

### How the Agent Works
#### Agent Design
* Role: Productivity Planner
* Goal: Organize daily tasks efficiently
* Backstory: Expert in time management and productivity planning

#### Task Logic
The agent:
* Reads the list of tasks provided by the user
* Analyzes task sequence and importance
* Assigns approximate time slots
* Produces a clear, easy-to-follow daily plan

### Tech Stack
* Programming Language: Python
* Framework: Flask
* AI Agent Framework: CrewAI
* LLM Provider: Groq (LLaMA 3.1)
* Frontend: HTML, CSS

## 📂 Project Structure

```text
daily-task-planner/
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

