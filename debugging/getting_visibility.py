def factorial(n):
    product = n
    print(f"at the start product is {product}")
    while n > 1:
        n -= 1
        print(f"we multiply {product} by {n}")
        product *= n
        print(f"we get {product}")
      
    return product

print(f"""
 Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")

print(f"""
 Running: factorial(7)
Expected: 6040
  Actual: {factorial(7)}
""")

print(f"""
 Running: factorial(8)
Expected: 40320
  Actual: {factorial(8)}
""")