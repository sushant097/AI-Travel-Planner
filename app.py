import streamlit as st
from src.core.planner import TravelPlanner
from src.utils.logger import get_logger
from dotenv import load_dotenv

logger = get_logger(__name__)

st.set_page_config(page_title="AI Travel Itinerary Planner", page_icon="✈️")
st.title("✈️ Travel Itinerary Planner")
st.markdown("Plan your perfect day trip with AI-powered itinerary suggestions!")


load_dotenv() # Load environment variables from .env file

with st.form("travel_form"):
    city = st.text_input("Enter the city you want to visit:", placeholder="e.g., Paris, New York")
    interests = st.text_input("Enter your interests (comma-separated):", placeholder="e.g., art, history, food")
    submitted = st.form_submit_button("Generate Itinerary")

if submitted:
    if not city or not interests:
        st.error("Please provide both city and interests to generate an itinerary.")
    else:
        try:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itinerary = planner.create_itinerary()

            st.subheader("📄 Your AI-Generated Itinerary:")
            st.markdown(itinerary)
            logger.info("Itinerary displayed successfully")
        except Exception as e:
            st.error(f"An error occurred while generating the itinerary: {e}")
            logger.error(f"Error in itinerary generation: {e}")