from app import app, db, User

def check_users():
    with app.app_context():
        users = User.query.all()
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Password: {user.password}")

if __name__ == "__main__":
    check_users()

