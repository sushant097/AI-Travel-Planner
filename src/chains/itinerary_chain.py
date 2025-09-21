from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY


llm = ChatGroq(
    groq_api_key = GROQ_API_KEY,
    model_name = "llama-3.3-70b-versatile",
    temperature=0.3,
)

itinerary_prompt = ChatPromptTemplate([
    ("system", 
     "You are a professional travel agent. Your task is to design a detailed, engaging, "
     "and practical one-day itinerary tailored to the user’s preferences. "
     "Make sure to include local highlights, food stops, cultural experiences, "
     "and relaxing breaks. The plan should be realistic and time-bound."),
    ("human", 
     "Plan a day trip itinerary for {city}. The user is interested in: {interests}. "
     "Provide the plan as a concise, bulleted list with time slots if possible.")
])

def generate_itineary(city:str, interests:list[str]) -> str:
    """Generate a travel itinerary based on the city and user interests."""
    interests_str = ", ".join(interests)
    messages = itinerary_prompt.format_messages(city=city, interests=interests_str)
    resp = llm.invoke(messages)
    return resp.content
