def check_user(username, password):
    # Usuarios de ejemplo. Puedes reemplazar por una base de datos real o autenticación externa.
    users = {
        "admin": "admin123",
        "usuario": "password"
    }
    return users.get(username) == password
