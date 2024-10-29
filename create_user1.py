from datetime import datetime
from generate_id1 import generate_id1
from db1 import DB 


today = datetime.today()


def create_user1(*, name: str=None, surname: str=None, credet_at: str=None) -> dict:
    if credet_at == '':
        credet_at = today
    else:
        flag = True
        while True:
            try:
                if flag:
                    credet_at = datetime.strptime(credet_at, '%d-%m-%Y')
                    if credet_at > today:
                        print("Gelecek vaxt verile bilmez.")
                    else:
                        break
            except ValueError:
                print("Daxil etdiyiniz format düzgün deyil.")
    
    id = generate_id1()
    data = {'name': name, 'surname': surname, 'credet_at': credet_at}

    DB[id] = data