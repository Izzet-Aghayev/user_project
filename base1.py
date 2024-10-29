import login1
from create_user1 import create_user1
from detail_user1 import detail_user1


while True:
    email = input("Emaili yaz: ")           # a
    pswd = input("Sifreni yaz: ")           # a

    checked = login1.login1(email=email, pswd=pswd)
    if checked:
        print("daxil oldu.")
        break
    print("Sifre ve ya email sefdi.")


while True:
    print('''
        1 -> Create User
        2 -> Detail User
        3 -> Exit
        '''
    )
    operation = input('Emeliyyati daxil edin: ')

    if operation == '1':
        name = input("Adı daxil edin: ")
        surname = input("Soyadı daxil edin: ")
        creted_at = input('Ise daxil oldugu tarix [GG-AA-IIII] (Bos kecile biler): ')

        create_user1(name=name, surname=surname, credet_at=creted_at)
        print("Isci daxil edildi. ")
    elif operation == '2':
        id = int(input('ID-ni daxil et: '))

        print(detail_user1(id=id))
    elif operation == '3':
        break
    else:
        print('Bele emeliyyat yoxdu.')