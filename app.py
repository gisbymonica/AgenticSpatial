import streamlit as st
import json
from agents.llm_router import route_query
from agents.rag_agent import retrieve_relevant_docs
from agents.dataset_agent import fetch_sentinel_series
from agents.processing_agent import generate_ndvi_timeseries
from agents.analysis_agent import compute_trend
from agents.explanation_agent import explain_results

st.set_page_config(page_title="Agentic RAG GeoAI", layout="wide")

st.title("🛰 Agentic RAG GeoAI – Spatio-Temporal Variability Analyzer")

query = st.text_input("Ask a geospatial question:", 
                      "Analyze NDVI trend for Bengaluru Rural from 2016 to 2024")

if st.button("Run Analysis"):
    st.header("1. LLM Interpretation")
    task = json.loads(route_query(query))
    st.json(task)

    st.header("2. RAG Metadata Retrieval")
    rag_docs = retrieve_relevant_docs(query)
    st.json(rag_docs)

    st.header("3. Fetching Sentinel‑2 imagery")
    items = fetch_sentinel_series(task)
    st.write(f"Fetched {len(items)} scenes.")

    st.header("4. Computing NDVI Time Series")
    time_list, ndvi_series = generate_ndvi_timeseries(items, task)
    st.line_chart({"NDVI": ndvi_series})

    st.header("5. Trend Analysis")
    trend = compute_trend(time_list, ndvi_series)
    st.json(trend)

    st.header("6. AI‑Generated Scientific Explanation")
    summary = explain_results(task["aoi"], trend)
    st.write(summary)