def arithmetic_arranger(equations):
    """this takes list of arithmetic problem and rearrange them"""
    if len(equations) > 5:
        return "To many Problems"
    a = ''
    b = ''
    for equation in equations:
        first_n, operator, second_n = equation.split(' ')
        a += first_n.rjust(5)
##        print(a)
        b += operator.ljust(3)
        b += second_n.ljust(10)
##        print(b)

    print(a)
    print(b)



arithmetic_arranger(['30 + 5', '30 + 5', '30 + 5', '30 + 5', '30 + 5'])

