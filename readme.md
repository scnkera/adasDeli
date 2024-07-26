Ada's Delicious Deli

Ada’s Delicious Deli is a popular spot known for its warm atmosphere and yummy customizable sandwiches. The café offers a variety of bread types, fillings, and optional extras. The goal is to create an efficient order cost calculator for Ada’s Delicious Deli sandwich orders.

An order has one and only one bread type. The options are white, wheat, rye, and sourdough. Their respective prices are listed below.
An order can have between none and multiple fillings. The options are ham, turkey, chicken, tofu, and cheese. Their respective prices are listed below.
An order can include any number of extras. The options are lettuce, tomato, avocado, and bacon. Their respective prices are listed below.
If a customer provides the coupon code “ADARULEZ”, subtract $1.50 from the order total.

The function called sandwich_order_calculator accepts four parameters:
bread_type, a string representing the type of bread for the sandwich
fillings, a list of strings where each string represents the optional fillings in the sandwich
extras, a list of strings where each string represents the optional fillings in the sandwich
promo_code, a string representing the discount code

The function must return a message describing the price of the order in dollars (i.e., with two decimal places). Refer to the example output for the specific formatting.

Bread Prices
Name	Price ($)
white	1.77
wheat	2.18
rye	2.50
sourdough	2.99

Filling Prices
Name	Price ($)
ham	3.15
turkey	3.55
chicken	4.75
tofu	2.75
cheese	0.55

Extra Prices
Name	Price ($)
lettuce	0.65
tomato	0.88
avocado	2.22
bacon	3.15

Unit Tests
The specific challenges your code is required to accommodate are written as unit tests that can be run from the Unit Tests panel at the left (the icon looks like a check mark). Clicking the Run tests button will run the Challenge inputs against your code, displaying either a success message, or a message about what was expected and what was observed.

Examples
These examples are also provided as a set of tests that can be run from the Unit Tests panel at the left (the icon appears under Tools, and looks like a check mark). Clicking the Run tests button will run the Challenge inputs against your code, displaying either a success message, or a message about what was expected and what was observed. You may need to open an additional Console view, and rerun the tests, in order to see the test result messages.