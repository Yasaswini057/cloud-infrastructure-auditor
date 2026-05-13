import logging
import os

# Create logs directory if not exists
os.makedirs("output/logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="output/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create logger object
logger = logging.getLogger(__name__)