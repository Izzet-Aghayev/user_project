from datetime import datetime
from db1 import DB

today = datetime.today()

def detail_user1(*, id: int=0) -> dict:
    if id in DB.keys():
        data = DB[id]
        data['days'] = (today - data['credet_at']).days
        return data
    else:
        print("Id tapilmadi.")
        return {}
        