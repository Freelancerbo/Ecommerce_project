# Product Class
class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} (Quantity: {self.quantity})"


# Cart Class
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product, quantity):
        if product.quantity >= quantity:
            self.cart_items.append({"product": product, "quantity": quantity})
            product.update_quantity(product.quantity - quantity)
            print(f"Added {quantity} of {product.name} to your cart.")
        else:
            print(f"Sorry, only {product.quantity} of {product.name} is available.")

    def total_price(self):
        total = 0
        for item in self.cart_items:
            total += item["product"].price * item["quantity"]
        return total

    def show_cart(self):
        print("\nYour Cart:")
        for item in self.cart_items:
            print(f"{item['product'].name} - ${item['product'].price} x {item['quantity']}")
        print(f"Total Price: ${self.total_price()}")


# Main Program
def show_products(products):
    print("\nAvailable Products:")
    for product in products:
        print(f"{product.id}. {product.name} - ${product.price} (Stock: {product.quantity})")


def main():
    # Creating some products
    product1 = Product(1, "Laptop", 1000, 10)
    product2 = Product(2, "Smartphone", 500, 20)
    product3 = Product(3, "Headphones", 100, 50)

    products = [product1, product2, product3]

    cart = Cart()

    while True:
        show_products(products)
        print("\nChoose a product to add to cart (enter product ID) or type 'exit' to quit.")

        user_input = input("Enter product ID: ")

        if user_input.lower() == 'exit':
            break

        try:
            product_id = int(user_input)
            quantity = int(input("Enter quantity: "))

            # Find the selected product by ID
            selected_product = next((p for p in products if p.id == product_id), None)

            if selected_product:
                cart.add_product(selected_product, quantity)
            else:
                print("Invalid product ID.")

        except ValueError:
            print("Invalid input, please enter valid numbers.")

        cart.show_cart()
        print("\n" + "-" * 30)

    print("Thank you for shopping!")


if __name__ == "__main__":
    main()
