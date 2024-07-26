import math

# declares the sandwich order dictionary and provides the associated order options
sandwich_order = {
    'bread_type': {
        'white': 1.77,
        'wheat': 2.18,
        'rye': 2.50,
        'sourdough': 2.99
    },
    'fillings': {
        'ham': 3.15,
        'turkey': 3.55,
        'chicken': 4.75,
        'tofu': 2.75,
        'cheese': 0.55  
    },
    'extras': {
        'lettuce': 0.65,
        'tomato': 0.88,
        'avocado': 2.22,
        'bacon': 3.15
    },
    'promo_code': {
        'ADARULEZ': -1.50
    }
}

# defines the sandwich order function that calculates the sandwhcih order total 
def sandwich_order_calculator(bread_type, fillings, extras, promo_code):
    # sums all of the sanwich component prices
    order_total = bread_type_calc(bread_type) + fillings_calc(fillings) + extras_calc(extras) + promo_code_calc(promo_code)
    output = f'The total price is ${order_total:.2f}'
    print(output)
    return output

# defines the bread type function that calculates the bread type total 
def bread_type_calc(bread_type):
    bread_type_dic = sandwich_order['bread_type']
    bread_type_keys = bread_type_dic.keys()
    bread_type_total = 0

    if isinstance(bread_type, str): # checks if the bread type is a string
        if bread_type in bread_type_keys: # checks if the bread type is a legitmate option
            bread_type_total = bread_type_dic[bread_type]
        else:
            print("You entered an invalid bread type. Please, try again.")
    else: 
        print("Please select only one bread type.")
    
    return bread_type_total

# defines the fillings function that calculates the fillings total 
def fillings_calc(fillings):
    fillings_dic = sandwich_order['fillings']
    fillings_keys = fillings_dic.keys()
    fillings_total = 0
    
    for fillings_item in fillings:
        if fillings_item in fillings_keys: # checks if the filling is a legitmate option
            filling_price = fillings_dic[fillings_item]
            fillings_total += filling_price
        elif fillings_item == '': # sets filling price to 0 if there is an empty string
            filling_price = 0
            fillings_total += filling_price
        else:
            print("You entered an invalid filling. Please, try again.")
    
    return fillings_total


# defines the extras function that calculates the extras total 
def extras_calc(extras):
    extras_dic = sandwich_order['extras']
    extras_keys = extras_dic.keys()
    extras_total = 0
    
    for extras_item in extras:
        if extras_item in extras_keys: # checks if the extra is a legitmate option
            extras_price = extras_dic[extras_item]
            extras_total += extras_price
        elif extras_item == '': # sets extra price to 0 if there is an empty string
            extras_price = 0
            extras_total += extras_price
        else:
            print("You entered an invalid extra . Please, try again.")
    
    return extras_total

# defines the promo code function that adds that registers a discounted price
def promo_code_calc(promo_code):
    promo_code_total = 0

    if isinstance(promo_code, str): # checks if the promo code is a string
        if promo_code == 'ADARULEZ': # checks if the promo code entered is correct
            promo_code_total = sandwich_order['promo_code'][promo_code]
        else:
            promo_code_total = 0
            # print("You entered an invalid promo code. No discount available.")

        return promo_code_total
    else: 
        print("Please, insert only one promo code.")

# Unit tests
input_one = sandwich_order_calculator('wheat', ['ham', 'cheese'], ['lettuce', 'bacon'], 'ADARULEZ')
output_one = 'The total price is $8.18'

input_two = sandwich_order_calculator('wheat', ['ham', 'cheese'], ['lettuce', 'bacon'], 'ADARULEZZZ')
output_two = 'The total price is $9.68'

input_three = sandwich_order_calculator('rye', ['turkey', 'cheese'], ['avocado', 'tomato'], '')
output_three = 'The total price is $9.70'

input_four = sandwich_order_calculator('sourdough', ['chicken'], ['lettuce', 'bacon'], 'ADARULEZ')
output_four = 'The total price is $10.04'

input_five = sandwich_order_calculator('rye', [''], ['avocado', 'tomato', 'bacon', 'lettuce'], '')
output_five = 'The total price is $9.40'

input_six = sandwich_order_calculator('rye', ['chicken', 'ham', 'tofu', 'turkey'], ['tomato', 'lettuce'], 'ADARULEZ')
output_six = 'The total price is $16.73'

# assertions used to confirm that challenges 1-6 generate the correct outputs
assert input_one == output_one, f"Expected Price: {output_one}, but got: {input_one}"
assert input_two == output_two, f"Expected Price: {output_two}, but got: {input_two}"
assert input_three == output_three, f"Expected Price: {output_three}, but got: {input_three}"
assert input_four == output_four, f"Expected Price: {output_four}, but got: {input_four}"
assert input_five == output_five, f"Expected Price: {output_five}, but got: {input_five}"
assert input_six == output_six, f"Expected Price: {output_six}, but got: {input_six}"