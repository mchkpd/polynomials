import re


def eval_poly(expression: str, x: float, y: float):
    # Initial cleanup: remove spaces and make variables lowercase.
    prepared_expression = expression.replace(' ', '').lower()
    # Add coefficient "1" when not specified explicitly at the beginning of the expression.
    prepared_expression = re.sub('^(x|y)', r'1\1', prepared_expression)
    # Add coefficient "1" when not specified explicitly in the middle of the expression.
    prepared_expression = re.sub('(\\+(x|y))', r'+1\2', prepared_expression)
    prepared_expression = re.sub('(-(x|y))', r'-1\2', prepared_expression)
    # Add proper mathematical operations (ASCII codes: 94 => ^, 120 => x, 121 => y).
    prepared_expression = prepared_expression.translate({94: '**', 120: '*x', 121: '*y'})
    # Interpolate values.
    prepared_expression = prepared_expression.translate({120: str(x), 121: str(y)})
    return eval(prepared_expression)
