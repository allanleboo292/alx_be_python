from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")  # Output: The sum is: 15

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")  # Output: The product is: 50

if __name__ == "__main__":
    main()
