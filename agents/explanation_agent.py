from openai import OpenAI

client = OpenAI()

def explain_results(aoi, trend):
    prompt = f"""
    Summarize the NDVI trend analysis for {aoi}.
    Trend slope: {trend['slope']:.4f}
    Correlation: {trend['r']:.3f}
    p-value: {trend['p']:.3f}
    """

    resp = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return resp.choices[0].message["content"]