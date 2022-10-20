import os

MAX_HOURS = int(os.getenv("MAX_FORECAST_HOURS", 192))
SHAPE_HOURS = int(max_hours / 3 + 1)
