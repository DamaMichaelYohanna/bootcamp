def arithmetic_arranger(equations, flag):
    """this takes list of arithmetic problem and rearrange them"""
    if len(equations) > 5:
        return "To many Problems"
    a = ''
    b = ''
    _ = ''
    answer = ''
    for equation in equations:
        first_n, operator, second_n = equation.split(' ')
        a += first_n.rjust(5).ljust(13)
##        print(a)
        b += operator.ljust(3)
        b += second_n.ljust(10)
        _ += '-------'.rjust(3).ljust(13)
        if flag:
            answer += str(eval(equation)).rjust(5).ljust(13)
##        print(b)

    print(a)
    print(b)
    print(_)
    print(answer)



arithmetic_arranger(['30 + 5', '30 + 5', '30 + 5', '30 + 5', '30 + 5'],True)

