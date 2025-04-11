class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email
        self.orders = []

    def register(self):
        return f"User {self.name} registered."

    def login(self):
        return f"User {self.name} logged in."

    def view_orders(self):
        return self.orders