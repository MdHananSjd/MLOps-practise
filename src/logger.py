#to log any errors or important information that may be useful for debugging or monitoring the application.
import logging
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"