
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#Inspect DataFrame
print(visits.head(),
      cart.head(),
      checkout.head(),
      purchase.head())

# combining Visits and cart using left merge
visits_cart_left = pd.merge(visits, cart, how='left')
#[2052 rows x 3 columns]
print(visits_cart_left)
# lenght of merged dataFrame = 2052
visits_cart_left_rows = len(visits_cart_left)

# number of null values cart_time
null_values_cart = len(visits_cart_left[visits_cart_left.cart_time.isnull()])
# number of null values = 1652
print(null_values_cart)

# Percentage of people who visited cool T-shirt 
# but did not place a t-shirt in their
# cart = 0.805068226121
print(float(null_values_cart) / visits_cart_left_rows)

#combining cart and checkout using left merge
cart_checkout = pd.merge(cart,checkout, how = 'left')
#[602 rows x 3 columns]
print(cart_checkout)

cart_checkout_rows = len(cart_checkout)
# length of merged dataFrame = 602
print(cart_checkout_rows)

# number of null values from cart_checkout
null_cart_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
# number of null values = 126
print(null_cart_checkout)

# percentage of people
# who put item in their cart 
# but did not proceed to checkout = 0.209302325581
print(float(null_cart_checkout) / cart_checkout_rows)

# combining purchase and checkout using left merge
checkout_purchase = pd.merge(checkout, purchase, how = 'left')
print(checkout_purchase)

checkout_purchase_rows = len(checkout_purchase)
# length of merged dataFrame = 598
print(checkout_purchase_rows)

# number of null values from checkout_purchase
null_checkout_purchase = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
# number of null values = 101
print(null_checkout_purchase)

# percentage of people who proceeded to 
# checkout but did not 
# purchase a t-shirt = 0.16889632107
print(float(null_checkout_purchase) / checkout_purchase_rows)


# merging all four steps of the funnel, in order
all_data = visits\
           .merge(cart, how = 'left')\
           .merge(checkout, how = 'left')\
           .merge(purchase, how = 'left')
# calculating average time from 
# initial visit to final purchase
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)

#average time to purchase = 0 days 00:44:02.672413
print(all_data.time_to_purchase.mean())

   









































