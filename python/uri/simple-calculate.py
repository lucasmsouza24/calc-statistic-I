def input_samples():
    string_input = input()
    string_input_array = string_input.split(' ')
    code_product = int(string_input_array[0])
    units_of_product = int(string_input_array[1])
    price = float(string_input_array[2])
    return [code_product, units_of_product, price]

def total_prod(prod):
    return prod[1] * prod[2]

prod1 = input_samples()
prod2 = input_samples() 

total = total_prod(prod1) + total_prod(prod2)

print(f'VALOR A PAGAR: R$ {total:.2f}')
