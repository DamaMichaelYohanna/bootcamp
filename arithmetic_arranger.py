def arithmetic_arranger(equations):
    """this takes list of arithmetic problem and rearrange them"""
    if len(equations) > 5:
        return "To many Problems"

    for equation in equations:
        first_n, operator, second_n = equation.split(' ')
        print(first_n.ljust(10), end='')
        print(operator.ljust(2), end='')
##        print(first_n, operator, second_n)



arithmetic_arranger(['30 + 5', '30 + 5', '30 + 5', '30 + 5', '30 + 5'])

