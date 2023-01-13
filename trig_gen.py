import math as m
import os

STYLESHEETS_FOLDER = "trig_stylesheets"

trig_functions = {
    'sin': m.sin,
    'cos': m.cos,
    'tan': m.tan
}

atrig_functions = {
    'asin': m.asin,
    'acos': m.acos,
    'atan': m.atan
}

CSS_TEMPLATE = """/* Trigonometry definitions for css */

:root {
%s
}
"""

EXAMPLE_TEMPLATE = """
/* Unit circle example animations */

"""

def get_trig_string(func_string, func, title):
    res = title
    for deg in range(0, 361):
        res += f"\t--{func_string}_deg_{deg}: {func(m.radians(deg)):.5f};\n"

    return res


def create_stylesheets():
    if not os.path.exists(STYLESHEETS_FOLDER):
        os.makedirs(STYLESHEETS_FOLDER)

    trig_full = ""
    for key in trig_functions:
        trig_string = get_trig_string(key, trig_functions[key], f"\t/* {key.title()} definitions in degrees */\n")
        trig_full += trig_string + "\n\n"

        with open(os.path.join(STYLESHEETS_FOLDER, f'{key}.css'), 'w') as file:
            file.write(CSS_TEMPLATE % trig_string)
    
    with open(os.path.join(STYLESHEETS_FOLDER, f'trig_full.css'), 'w') as file:
        file.write(CSS_TEMPLATE % trig_full)


def create_keyframes(name, top, left, sign):
    res = "@keyframes " + name + " {\n"
    for deg in range(0, 361):
        res += f"""\t{'{:.2f}'.format(deg / 3.6) + '%'} {'{'}
        top: calc(50% - var(--{top}_deg_{deg}) * 50%);
        left: calc(50% {sign} var(--{left}_deg_{deg}) * 50%)
    {'}'}
"""

    return res + '}\n\n'

def create_example():
    cos = create_keyframes('cosinus', 'cos', 'sin', '-')
    sin = create_keyframes('sinus', 'sin', 'cos', '+')
    with open("unit_circle.css", 'w') as file:
        file.write(EXAMPLE_TEMPLATE + cos + sin)

if __name__ == '__main__':
    create_stylesheets()
    create_example()