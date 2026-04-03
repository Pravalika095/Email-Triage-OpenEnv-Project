# Email Triage OpenEnv Environment

## Overview
This project implements a real-world RL environment for email triage. The agent must classify emails, assign priorities, and route them to appropriate departments.

## Features
- Real-world email simulation
- 3 tasks (easy, medium, hard)
- Deterministic grading (0.0–1.0)
- Step-based reward system
- Reproducible inference

## Action Space
- classify (spam, work, important)
- set_priority (low, medium, high)
- route (engineering, support, etc.)

## Observation Space
- email_id
- subject
- body
- sender

## Tasks
- Easy: spam classification
- Medium: classification + priority
- Hard: full triage

## Setup
```bash
pip install -r requirements.txt
python inference.py