import turtle


# 8
def get_8_param():
    return {"axiom": ' F - F - F - F ',
            "chr_1": 'F',
            "rule_1": 'F + F - F - F F F + F + F - F',
            "start_angle": 0,
            "angle": 90,
            "gens": 2, }


# 9
def get_9_param():
    return {"axiom": '[ F ] + [ F ] + [ F ] + [ F ] + [ F ] + [ F ]',
            "chr_1": 'F',
            "rule_1": 'F [ + + F] [ - F F ] F F [ + F ] [ - F ] F F',
            "start_angle": 0,
            "angle": 60,
            "gens": 3}


# 10
def get_10_param():
    return {"axiom": 'F + + F + + F',
            "chr_1": 'F',
            "rule_1": 'F - F + + F - F',
            "start_angle": 0,
            "angle": 60,
            "gens": 2}


# 11
def get_11_param():
    return {"axiom": ' F ',
            "chr_1": 'F',
            "rule_1": 'F - F + F + F + F - F - F - F + F ',
            "start_angle": 0,
            "angle": 60,
            "gens": 2}


# 12
def get_12_param():
    return {"axiom": 'F',
            "chr_1": 'F',
            "rule_1": 'F [ + F ] F [ - F ] F',
            "start_angle": 90,
            "angle": 25.7,
            "gens": 3}


def apply_rules(param):
    return ''.join([param["rule_1"] if chr == param["chr_1"] else chr for chr in param["axiom"]])


def get_result(param):
    for gen in range(param["gens"]):
        param["axiom"] = apply_rules(param)
        # print(f"Str: {param['axiom']}")
    return param


def get_fractal(param):
    """функция отрисовки фрактала"""
    # screen settings
    WIDTH, HEIGHT = 1920, 1080
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.screensize(30*WIDTH, 30*HEIGHT)
    screen.delay(0)

    # turtle settings
    turt = turtle.Turtle()
    turt.pensize(1)
    turt.speed(0)
    turt.penup()
    turt.setpos(0, 0)
    turt.pendown()

    step = 20
    stack = []
    color = [0, 0, 0]
    thickness = 5

    param = get_result(param)
    turt.pensize(thickness)

    turt.left(param["start_angle"])
    for chr in param["axiom"]:
        turt.color(color)
        if chr == 'F':
            turt.forward(step)
        elif chr == '+':
            turt.right(param["angle"])
        elif chr == '-':
            turt.left(param["angle"])
        elif chr == '[':
            angle_, pos_ = turt.heading(), turt.pos()
            stack.append((angle_, pos_, thickness, step, color[1]))
        elif chr == ']':
            angle_, pos_, thickness, step, color[1] = stack.pop()
            turt.pensize(thickness)
            turt.setheading(angle_)
            turt.penup()
            turt.goto(pos_)
            turt.pendown()
    screen.exitonclick()


def context_menu():
    match input("Выберите фигуру для постройки [8-12]:"):
        case "8":
            get_fractal(get_8_param())
        case "9":
            get_fractal(get_9_param())
        case "10":
            get_fractal(get_10_param())
        case "11":
            get_fractal(get_11_param())
        case "12":
            get_fractal(get_12_param())
        case "0":
            print("Exit")
            return False
        case _:
            print("Error Value")
            return True


if __name__ == '__main__':
    """main function"""
    work = context_menu()
