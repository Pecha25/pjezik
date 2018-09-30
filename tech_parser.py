from tech_lexer import *
from kombinatori_parser import *
from tech_AST import *

def keyword(kw):
    return Reserved(kw, RESERVED)