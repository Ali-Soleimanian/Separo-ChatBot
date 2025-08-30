from core.database import setup_db, User

session = setup_db()

def register(username, password):
    register_existing_user = session.query(User).filter_by(username=username).first()
    if register_existing_user:
        return False
    else:
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        return True


def login(username, password):
    login_existing_user = session.query(User).filter_by(username=username, password=password).first()
    if login_existing_user:
        return True
    else:
        return False
