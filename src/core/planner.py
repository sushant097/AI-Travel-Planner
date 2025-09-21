from langchain_core.messages import AIMessage, HumanMessage
from src.chains.itinerary_chain import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)


class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itineary = ""

        logger.info("Initializing TravelPlanner")

    def set_city(self, city: str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info(f"City set to: {city} successfully")
        except Exception as e:
            logger.error(f"Error setting city: {e}")
            raise CustomException(f"Failed to set city: {e}")
        
    def set_interests(self, interests_str: str):
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info(f"Interests set successfully")
        except Exception as e:
            logger.error(f"Error setting interests: {e}")
            raise CustomException(f"Failed to set interests: {e}")

    def create_itinerary(self) -> str:
        try:
            logger.info(f"Generating itinerary for {self.city} with interests: {self.interests}")
            print(f"Generating itinerary for {self.city} with interests: {self.interests}")
            self.itineary = generate_itineary(self.city, self.interests)
            self.messages.append(AIMessage(content=self.itineary))
            logger.info("Itinerary generated successfully")
            return self.itineary
        except Exception as e:
            logger.error(f"Error generating itinerary: {e}")
            raise CustomException(f"Failed to generate itinerary: {e}")