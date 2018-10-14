from tech_lexer import *
from kombinatori_parser import *
from tech_AST import *
import functools 

#OSNOVNI PARSERI
def keyword(kw):
    return Reserved(kw, RESERVED)

id = Tag(IME)

num = Tag(BROJ) ^ (lambda i: int(i))

#ARITMETIČKE OPERACIJE I IZRAZI
def aexp():
    return precedence(aexp_term(), aexp_precedence_levels, process_binop)

def aexp_value():
    return (num^ (lambda i: IntAexp(i))) | (id ^ (lambda v: VarAexp(v)))

def aexp_group():
    return keyword('(') + Lazy(aexp) + keyword(')') ^ process_group

def aexp_term():
    return aexp_group() | aexp_value()

#BINARNE OPERACIJE I IZRAZI
def bexp_relop():
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return aexp() + any_operator_in_list(relops) + aexp() ^ process_relop


#POMOĆNE FUNKCIJE
def process_group(parsed):
    ((_, p), _) = parsed
    return p

def process_binop(op):
    return lambda l, r: BinopAexp(op, l, r)

def any_operator_in_list(ops):
    op_parsers = [keyword(op) for op in ops]
    parser = functools.reduce(lambda l, r: l | r, op_parsers)
    return parser

def process_relop(parsed):
    ((left, op), right) = parsed
    return RelopBexp(op, left, right)

def process_logic(op):
    if op == 'and':
        return lambda l, r: AndBexp(l, r)
    elif op == 'or':
        return lambda l, r: OrBexp(l, r)
    else:
        raise RuntimeError('Nepoznati logički operator: ' + op)

def precedence(value_parser, precedence_levels, combine):
    def op_parser(precedence_level):
        return any_operator_in_list(precedence_level) ^ combine
    parser = value_parser * op_parser(precedence_levels[0])
    for precedence_level in precedence_levels[1:]:
        parser = parser * op_parser(precedence_level)
    return parser

aexp_precedence_levels = [
    ['*', '/'],
    ['+', '-'],
]