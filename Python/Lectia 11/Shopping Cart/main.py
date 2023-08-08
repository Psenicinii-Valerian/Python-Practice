class User:
    def __init__(self, username, email, password, balance):
        self.username = username
        self.email = email
        self.password = password
        self.balance = balance
        self.cart = []

    def login(self, email, password):
        if self.email == email and self.password == password:
            print(f"Logged in as {self.username}\n")
        else:
            # raise - cuvant-cheie ce ridica o eroare    in program
            raise SystemExit("Login Failed. Wrong Credentials")

    def logout(self):
        print(f"Logged out. Goodbye {self.username}")

    def deposit(self, money):
        self.balance += money

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product.name} has been added successfully to the cart\n")

    def remove_from_cart(self, product):
        if product in self.cart:
            # del self.cart[product]
            self.cart.remove(product)
            print(f"{product.name} has been successfully deleted from the cart\n")
        else:
            print(f"{product.name} not found in cart\n")

    def view_cart(self):
        if self.cart:
            print(f"Cart for {self.username}:")
            for product in self.cart:
                print(product)
        else:
            print("Cart is empty\n")

    def checkout(self):
        if self.cart:
            total_price = sum(product.price for product in self.cart)
            print(f"Checkout complete. Total price: {total_price}$\n")
            if self.balance >= total_price:
                self.balance -= total_price
                print("Items bought. Deleting all your cart products\n")
                self.cart = []
            else:
                print("Insuficient funds. Add more money to your balance or remove some products from cart!\n")
        else:
            print("Cart is empty. Nothing to checkout\n")

    def __str__(self):
        return f"Username: {self.username}\nEmail: {self.email}\nBalance: {self.balance}\n"


class Product:
    next_product_id = 1

    def __init__(self, name, price, seller):
        self.product_id = Product.next_product_id
        Product.next_product_id += 1
        self.name = name
        self.price = price
        self.seller = seller

    def __str__(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nPrice: {self.price}\nSeller: {self.seller}\n"

user = User("kimateru", "maximka@mail.org", "PsheniciniVarelian228", 13)
user.login("maximka@mail.org", "PsheniciniVarelian228")

product1 = Product("Iphone 17 Pluton Raketa", 10, "Tim Cook V2.0 AI")
product2 = Product("JBL Minus Urechi Toxic Edition", 4, "Ionut 999")

user.add_to_cart(product1)
user.add_to_cart(product2)

user.view_cart()

user.checkout()

user.remove_from_cart(product1)

user.checkout()

print(user)

user.logout()