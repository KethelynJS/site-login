from app import app, db, User

def create_user(username, password):
    with app.app_context():
        if User.query.filter_by(username=username).first():
            print(f"Usuário {username} já existe!")
            return
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        print(f"Usuário {username} criado com sucesso!")

if __name__ == "__main__":
    username = "admin4"  # Nome de usuário desejado
    password = "admin4"  # Senha desejada
    
    create_user(username, password)
