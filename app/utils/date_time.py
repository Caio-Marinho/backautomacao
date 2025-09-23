from datetime import datetime,time,date
from ..configuration.config import configuration as config
import pytz
FUSO_LOCAL = pytz.timezone(config.FUSO_LOCAL)
def dia_hora() -> datetime:
    return datetime.now(FUSO_LOCAL)

def hoje() -> date:
    return datetime.today().astimezone(FUSO_LOCAL)

def agora() -> time:
    return datetime.now(FUSO_LOCAL).time()
