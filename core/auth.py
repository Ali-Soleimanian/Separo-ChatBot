from core.database import setup_db, User

session = setup_db()

def register(username, password):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        return False
    else:
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        return True
