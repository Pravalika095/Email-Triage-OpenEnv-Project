---
title: Email Triage OpenEnv
emoji: 📧
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---

# 📧 Email Triage OpenEnv Environment

## 🚀 Overview
This project implements a real-world Reinforcement Learning (RL) environment for **email triage**.

An AI agent learns to:
- Classify emails
- Assign priority
- Route to correct department

Built using the **OpenEnv framework**.

---

## ✨ Features
- Real-world workflow simulation
- 3+ tasks (easy → medium → hard)
- Deterministic grading (0.0–1.0)
- Dense reward function
- Fully reproducible inference
- Docker + Hugging Face deployment

---

## ⚙️ Action Space
The agent outputs:

- `category` → spam, work, important  
- `priority` → low, medium, high  
- `department` → engineering, support  

---

## 📊 Observation Space

Each state includes:

- email_id  
- subject  
- body  
- sender  
- category (optional)  
- priority (optional)  
- department (optional)  

---

## 🧪 Tasks

### 🟢 Easy
- Detect spam email  

### 🟡 Medium
- Classify + assign priority  

### 🔴 Hard
- Full triage (classification + routing)  

---

## 🎯 Reward Design

- +0.4 → correct classification  
- +0.3 → correct priority  
- +0.3 → correct routing  
- Penalty for incorrect actions  

---

## 🔌 API Endpoints

- `GET /` → health check  
- `GET /reset` → reset environment  
- `POST /step` → perform action  
- `GET /state` → current state  

---

## 🛠 Setup

```bash
pip install -r requirements.txt
python inference.py
```

---

## 📈 Baseline Output

```
[START]
[STEP] ...
[END] success=true
```

---

## 🌐 Deployment

Deployed on Hugging Face Spaces using Docker.

---

## 👤 Author

Pravalika