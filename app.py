# app.py

import streamlit as st
from streamlit_option_menu import option_menu

from agents.llm_router import route_query
from agents.dataset_agent import fetch_sentinel_series
from agents.processing_agent import generate_ndvi_timeseries
from agents.analysis_agent import compute_trend
from agents.explanation_agent import explain_results
from agents.rag_agent import retrieve_relevant_metadata


st.set_page_config(page_title="Agentic RAG GeoAI", layout="wide")

# ---------------- Navigation ----------------
with st.sidebar:
    choice = option_menu(
        "GeoAI Agentic RAG System",
        ["Home", "RAG Explorer", "Sentinel‑2 NDVI", "Trend Analysis", "Interpretation"],
        icons=["house", "search", "camera", "bar-chart", "chat"],
        menu_icon="radar",
        default_index=0,
    )


# ---------------- Home Page ----------------
if choice == "Home":
    st.title("🛰 Agentic RAG‑Powered GeoAI")
    st.write("""
        This system integrates:
        - Retrieval-Augmented Generation (RAG)
        - Autonomous GeoAgents
        - STAC-based satellite retrieval
        - Spatial raster processing
        - LLM-driven interpretations
    """)


# ---------------- RAG Explorer ----------------
elif choice == "RAG Explorer":
    st.title("🔍 RAG Metadata Explorer")

    query = st.text_input("Enter search query:", "Sentinel NDVI Bengaluru Rural")

    if st.button("Search Metadata"):
        results = retrieve_relevant_metadata(query)
        st.json(results)


# ---------------- Sentinel NDVI Analysis ----------------
elif choice == "Sentinel‑2 NDVI":
    st.title("🌱 Sentinel‑2 NDVI Processing")

    user_query = st.text_input("Enter geospatial task:",
                               "Analyze NDVI for Bengaluru Rural from 2016 to 2024")

    if st.button("Run"):
        task = route_query(user_query)
        st.subheader("LLM Task Plan")
        st.json(task)

        st.subheader("Fetching Sentinel‑2 Scenes")
        items = fetch_sentinel_series(task)
        st.write(f"Found {len(items)} scenes.")


# ---------------- Trend Analysis ----------------
elif choice == "Trend Analysis":
    st.title("📊 NDVI Trend Analysis")

    st.warning("Run NDVI processing first in the previous tab.")

    # Data stored in session_state after NDVI computation
    if "times" in st.session_state and "ndvis" in st.session_state:
        time_list = st.session_state["times"]
        ndvi_series = st.session_state["ndvis"]

        st.line_chart({"NDVI": ndvi_series})

        trend = compute_trend(time_list, ndvi_series)
        st.subheader("Trend Results")
        st.json(trend)

    else:
        st.error("No NDVI data available.")


# ---------------- Interpretation ----------------
elif choice == "Interpretation":
    st.title("📝 AI‑Generated Interpretation")

    if "trend" not in st.session_state:
        st.error("Run Trend Analysis first.")
    else:
        aoi = st.session_state["task"]["aoi"]
        trend = st.session_state["trend"]
        summary = explain_results(aoi, trend)
        st.write(summary)
