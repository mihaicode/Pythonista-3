# The following pseudo code describes how a bookstore computes the price of an order from the total price and the number of books that were ordered (PFE Business P2.32).

#1. Read the total book price and the number of books
price_per_book = int(input("Book Price:"))
number_of_books = int(input("Number of books:"))
total_book_price = price_per_book*number_of_books

#2. Compute the tax (7.5 per cent of the total book price), that is,

#tax = total book price * (7.5/100)
TAX_RATE = 7.5/100
order_tax = TAX_RATE*total_book_price

#3. Compute the shipping charge ($2 per book), that is,
# shipping charge = number of books * 2.00
SHIPPING_CHARGE_PER_BOOK = 2
total_shippping_cost = SHIPPING_CHARGE_PER_BOOK*number_of_books

#4. The price of the order is the sum of the total book price, the tax and the shipping charge, that is,

#order price = total book price + tax + shipping charge

order_price = total_book_price +  order_tax + total_shippping_cost
#5. Print the price of the order.

print("Tax:", order_tax)
print("Shipping:", total_shippping_cost)
print("Order total: ", order_price)
