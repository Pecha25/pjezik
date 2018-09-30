import lexing
import re

RESERVED = 'RESERVED'
INT = 'INT'
ID = 'ID'
OPERATOR = 'OPERATOR'
PRINT = 'PRINT'
EQUALS = 'EQUALS'
END = 'END'


token_exprs = [
    (r'[\n\t]+',                None),  #Nova linija / Tab
    (r'[^\n]*',                 None),  #Komentar
    (r'\=',                     EQUALS),
    (r'\+',                     OPERATOR),
    (r'-',                      OPERATOR),
    (r'\*',                     OPERATOR),
    (r'/',                      OPERATOR),
    (r'print',                  PRINT),
    (r';',                      END),
    (r'[0-9]+',                 INT),
    (r'[A-Za-z][A-Za-z0-9_]*',  ID),
]

def tech_lex(characters):
    return lexer.lex(characters, token_exprs)