# Enter your name:sagar
# Enter the product name:Toy1
# Write your feedback here and help us to improve the service:
# Awesome product
# Thank you for your valuable feedback on the product.
def feedback():
    customer_name = input("Enter your name: ")
    product_name = input("Enter the product name: ")
    feedback = input("Write your feedback here and help us to improve the service:\n")

    file_name = f"{product_name}.txt"

    with open(file_name,'a') as file:
        file.write(f"Customer name:{customer_name}\n")
        file.write(f"feedback: {feedback}\n")
        file.write("-" * 40 + "\n")

    print("Thank you for your valuable feedback on the product.")

feedback()








