import db1


def generate_id1():
    list_ids = list(db1.DB.keys())

    if len(list_ids) == 0:
        return 1
    else:
        return list_ids[-1] + 1