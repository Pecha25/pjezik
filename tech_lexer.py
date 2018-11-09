import tech_lexing
import re

RESERVED = 'RESERVED'
BROJ = 'BROJ'
IME = 'IME'


token_exprs = [
    (r'[\n\t ]+',               None),  #Praznine
    (r'(\/\/.*\/\/)',           None),  #Komentar
    (r'\(',                    RESERVED),
    (r'\)',                    RESERVED),
    (r';',                     RESERVED),
    (r'\+',                    RESERVED),
    (r'-',                     RESERVED),
    (r'\*',                    RESERVED),
    (r'/',                     RESERVED),
    (r'<=',                    RESERVED),
    (r'<',                     RESERVED),
    (r'>=',                    RESERVED),
    (r'>',                     RESERVED),
    (r'!=',                    RESERVED),
    (r'=',                     RESERVED),
    (r'and',                   RESERVED),
    (r'or',                    RESERVED),
    (r'not',                   RESERVED),
    (r'if',                    RESERVED),
    (r'then',                  RESERVED),
    (r'else',                  RESERVED),
    (r'while',                 RESERVED),
    (r'do',                    RESERVED),
    (r'[0-9]+',                 BROJ),
    (r'[A-Za-z][A-Za-z0-9_]*',  IME),
]

def tech_lex(characters):
    return tech_lexing.lex(characters, token_exprs)