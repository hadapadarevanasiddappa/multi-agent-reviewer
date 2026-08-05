# 🤖 Virtual Engineering Team (Multi-Agent CI/CD Pipeline)

> An automated, multi-agent AI pipeline integrated directly into GitHub Actions that performs autonomous code review, QA testing, and algorithmic optimization on every push.

## 🚀 Overview
Most CI/CD pipelines just run static linters. This project deploys a **Swarm of AI Agents** using CrewAI and Groq's ultra-fast Llama-3.3 70B model to dynamically act as a Virtual Engineering Team.

Whenever code is pushed to this repository, three distinct AI personas boot up, read the codebase, collaborate, and generate a final engineering report.

## 🧠 The Agent Ecosystem
1. **The Code Reviewer (Senior Staff Engineer):** Scans for security vulnerabilities, edge cases, and anti-patterns.
2. **The QA Engineer:** Takes the reviewer's feedback and automatically writes extreme-edge-case `pytest` functions.
3. **The Systems Architect:** Analyzes time/space complexity (Big O) and suggests structural algorithm optimizations.

## ⚙️ Tech Stack
* **Orchestration Framework:** CrewAI
* **LLM Engine:** ChatGroq (Llama-3.3-70b-versatile) for sub-second inference
* **CI/CD Infrastructure:** GitHub Actions (Ubuntu Runners)
* **Language:** Python 3.11

## 🔄 Pipeline Architecture
1. **Trigger:** Developer pushes Python code to the `main` branch.
2. **Environment Setup:** GitHub Actions provisions an Ubuntu runner, installs dependencies, and securely injects API keys.
3. **Orchestration:** The Python engine initializes the LLM and assigns dynamic tasks based on the newly pushed code.
4. **Execution:** Agents communicate in real-time, passing context to one another to analyze the codebase.
5. **Output:** A comprehensive Markdown report containing bugs found, generated unit tests, and optimization strategies is logged in the console.

## 📝 Copyright & License
© 2026 H.RevanaSiddappa. All Rights Reserved.
This code is proprietary and serves as a portfolio demonstration. It may not be copied, distributed, or modified without express written permission.