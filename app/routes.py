from flask import Blueprint, jsonify, request

from app import db
from .exceptions import EvaluationError, RequiredParameterError
from .models import Polynomial
from .utils import eval_poly

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/poly', methods=['POST'])
def add_polynomial():
    expression = request.json.get('expression')
    if not expression:
        return {'error': 'Parameter `expression` is required.'}

    polynomial = Polynomial(
        expression=expression,
    )
    db.session.add(polynomial)
    db.session.commit()
    return jsonify(polynomial_id=polynomial.id)


@api_blueprint.route('/poly/eval', methods=['GET'])
def evaluate_polynomial():
    polynomial_id = request.args.get('polynomial_id')
    if not polynomial_id:
        raise RequiredParameterError('Parameter `polynomial_id` is required.')
    x = request.args.get('x')
    if not x:
        raise RequiredParameterError('Parameter `x` is required.')
    y = request.args.get('y')
    if not y:
        raise RequiredParameterError('Parameter `y` is required.')

    polynomial = Polynomial.query.get(polynomial_id)

    try:
        result = eval_poly(polynomial.expression, x, y)
    except SyntaxError:
        raise EvaluationError('Expression cannot be evaluated. Only x and y variables are allowed.')
    return jsonify(expression=polynomial.expression, value=result)
