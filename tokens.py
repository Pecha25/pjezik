import lexer
import re

RESERVED = 'RESERVED'
INT = 'INT'
ID = 'ID'
OPERATOR = 'OPERATOR'
PRINT = 'PRINT'
EQUALS = 'EQUALS'

token_exprs = [
    (r'[\n\t]+',                None),
    (r'#[^\n]*',                None),
    (r'\=',                     EQUALS),
    (r'\+',                     OPERATOR),
    (r'-',                      OPERATOR),
    (r'\*',                     OPERATOR),
    (r'/',                      OPERATOR),
    (r'print',                  PRINT),
    (r'[0-9]+',                 INT),
    (r'[A-Za-z][A-Za-z0-9_]',   ID),
]