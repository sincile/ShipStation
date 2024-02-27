from dotenv import load_dotenv
from os import getenv
import sys

sys.path.append("../ship_station/")
from ship_station import ShipStation


load_dotenv()

ss_api_key = getenv("SHIPSTATION_API_KEY", "")
ss_api_secret = getenv("SHIPSTATION_API_SECRET", "")
handler = ShipStation(ss_api_key, ss_api_secret)
