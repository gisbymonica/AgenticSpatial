from openai import OpenAI

client = OpenAI()

def route_query(user_query: str):
    """
    LLM interprets natural language and produces:
    - AOI
    - date range
    - analysis type
    - required datasets
    """
    system_prompt = """
    You are a GeoAI Orchestrator Agent.
    Convert user geospatial questions into a structured JSON plan.
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )

    return response.choices[0].message["content"]
``