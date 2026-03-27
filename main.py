import os
import asyncio
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from emergentintegrations import EmergentLLM

load_dotenv()
app = FastAPI()

# Initialize the AI Client [cite: 8, 76]
ai_client = EmergentLLM(api_key=os.getenv("EMERGENT_LLM_KEY"))

class AnalysisRequest(BaseModel):
    event: str
    sector: str

def get_live_usd_inr():
    try:
        res = requests.get("https://api.frankfurter.app/latest?from=USD&to=INR")
        return res.json()['rates']['INR']
    except:
        return 83.50 # Fallback [cite: 39]

@app.post("/api/analyze")
async def analyze_impact(data: AnalysisRequest):
    current_rate = get_live_usd_inr()
    
    # Task 1: Business-specific Impact Analysis [cite: 42]
    business_prompt = (
        f"Analyze the {data.event} for an Indian {data.sector} business. "
        "Provide: 5 Risk Factors, Headwinds, Opportunities, 3 Actions, and a Resilience Score (X/10). "
        "Use 'Composed Business Analyst' tone with measured, hedged language[cite: 45, 46]."
    )

    # Task 2: Broad Industry Map [cite: 43]
    industry_prompt = (
        "Map the impact of this event across these 10 sectors: IT, Pharma, Auto, Agri, Energy, "
        "Fintech, Logistics, Textiles, Retail, Chemicals. "
        "For each, provide: Status (RISK/OPP/NEU) and Intensity (1-10)[cite: 35]."
    )

    # Execute calls in parallel for speed [cite: 41, 72]
    business_analysis, industry_map = await asyncio.gather(
        ai_client.generate_async(model="claude-haiku-4.5", prompt=business_prompt),
        ai_client.generate_async(model="claude-haiku-4.5", prompt=industry_prompt)
    )

    return {
        "summary": {"event": data.event, "sector": data.sector, "rate": current_rate},
        "business_data": business_analysis,
        "industry_data": industry_map
    }
