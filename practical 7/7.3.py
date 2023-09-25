def calculate_discounted_price(original_price, discount_percentage):
    
    assert 0 <= discount_percentage <= 100, "Discount percentage must be between 0 and 100 inclusive"
    
   
    discount_amount = (discount_percentage / 100) * original_price
    
   
    assert discount_amount >= 0, "Discount amount cannot be less than zero"
    
   
    discounted_price = original_price - discount_amount
    
    return discounted_price

try:
    original_price = float(input("Enter the original price of the product: $"))
    discount_percentage = float(input("Enter the percentage discount: "))
    
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    
    print(f"The discounted price is: ${discounted_price:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numeric values for the original price and discount percentage.")
except AssertionError as e:
    print(f"Assertion Error: {e}")