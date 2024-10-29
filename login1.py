EMAIL = 'a'
PSWd = 'a'

def login1(email: str=None, pswd: str=None) -> bool:
    if email == EMAIL and pswd == PSWd:
        return True
    return False