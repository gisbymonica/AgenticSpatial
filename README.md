# 🛰️ Agentic GeoAI RAG System
### Retrieval‑Augmented Generation + Autonomous GeoAgents + Sentinel‑2 Spatio‑Temporal Analytics

This repository implements a **production‑grade Agentic GeoAI system** capable of:

- Natural language → structured geospatial task planning  
- Retrieval‑Augmented Generation (RAG) using ChromaDB  
- Autonomous agents coordinating spatio‑temporal analysis  
- Real Sentinel‑2 L2A ingestion through STAC  
- Cloud‑masking + mosaicking + NDVI computation  
- Trend analysis (Mann‑Kendall, Theil‑Sen, linear regression)  
- AI‑generated narrative interpretations  
- Multipage Streamlit UI for demonstration  

The system combines **LLMs + Agents + GeoAI + Earth Observation + RAG**, suitable for research, internal demos, and conference presentations.

---
# 🧱 Architecture Overview

## High‑Level System Architecture

```
              User Query (NLQ)
                      ↓
        ┌───────────────────────────┐
        │ LLM Orchestrator Agent    │
        └─────────────┬─────────────┘
                      ↓
   ┌──────────────────────────────────────────────┐
   │             Agentic GeoAI Subsystems        │
   │                                              │
   │ RAG Agent → Dataset Agent → Processing Agent │
   │       → Analysis Agent → Explanation Agent   │
   └──────────────────────────────────────────────┘
                      ↓
            Streamlit Frontend UI
```

---
# 🗂 Project Structure

```
geoai-agentic-rag/
│
├── app.py
├── config.py
├── agents/
├── core/
├── models/
├── data/
├── requirements.txt
└── Dockerfile
```

---
# 🛰 Sentinel‑2 Workflow

1. STAC search for Sentinel‑2 L2A tiles  
2. Download NIR, RED, SCL bands  
3. Clip to AOI  
4. Cloud masking using SCL codes  
5. NDVI generation  
6. Temporal statistics

---
# 🚀 Deployment

## Local
```
pip install -r requirements.txt
streamlit run app.py
```

## Docker
```
docker build -t geoai-rag .
docker run -p 8501:8501 geoai-rag
```

## Streamlit Cloud
1. Push to GitHub
2. Deploy via share.streamlit.io

---
# 🎥 Demo Workflow

1. Enter query  
2. LLM parses task  
3. RAG retrieves metadata  
4. Sentinel‑2 pipeline executes  
5. Trend analysis  
6. AI summary generated

---
# 📧 Contact
monica.mohan@capgemini.com
