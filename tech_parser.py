from tech_lexer import *
from kombinatori_parser import *
from tech_AST import *
import functools 

#OSNOVNI PARSERI
def keyword(kw):
    return Reserved(kw, RESERVED)

id = Tag(IME)

num = Tag(BROJ) ^ (lambda i: int(i))

#GLAVNI PARSERI
def parser():
    return Phrase(stmt_list())

def tech_parse(tokens):
    ast = parser()(tokens, 0)
    return ast

#ARITMETIČKE OPERACIJE
def aexp():
    return precedence(aexp_term(), aexp_precedence_levels, process_binop)

def aexp_value():
    return (num^ (lambda i: IntAexp(i))) | (id ^ (lambda v: VarAexp(v)))

def aexp_group():
    return keyword('(') + Lazy(aexp) + keyword(')') ^ process_group

def aexp_term():
    return aexp_group() | aexp_value()

#BINARNE OPERACIJE
def bexp():
    return precedence(bexp_term(), bexp_precendence_levels, process_logic)

def bexp_relop():
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return aexp() + any_operator_in_list(relops) + aexp() ^ process_relop

def bexp_not():
    return keyword('not') + Lazy(bexp_term) ^ (lambda parsed: NotBexp(parsed[1]))

def bexp_group():
    return keyword('(') + Lazy(bexp) + keyword(')') ^ process_group

def bexp_term():
    return bexp_not() | bexp_relop | bexp_group()

#IZJAVE/IZRAZI
def stmt():
    return assign_stmt() | if_stmt() | while_stmt()

def assign_stmt():
    def process(parsed):
        ((name, _), exp) = parsed
        return AssignStatement(name, exp)
    return id + keyword('=') + aexp() ^ process

def stmt_list():
    separator = keyword(';') ^ (lambda x: lambda l, r:CompoundStatement(l, r))
    return Exp(stmt(), separator)

def if_stmt():
    def process(parsed):
        (((((_, condition), _), true_stmt), false_parsed), _) = parsed
        if false_parsed:
            (_, false_stmt) = false_parsed
        else:
            false_stmt = None
        return IfStatement(condition, true_stmt, false_stmt)
    return keyword('if') + bexp() + \
           keyword('then') + Lazy(stmt_list) + \
           Opt(keyword('else') + Lazy(stmt_list)) + \
           keyword('end') ^ process

def while_stmt():
    def process(parsed):
        ((((_, condition), _), body), _) = parsed
        return WhileStatement(condition, body)
    return keyword('while') + bexp() + keyword('do') + Lazy(stmt_list) + keyword('end') ^ process

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

bexp_precendence_levels = [
    ['and'],
    ['or'],
]