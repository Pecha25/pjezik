import lexing
import re

RESERVED = 'RESERVED'
BROJ = 'BROJ'
IME = 'IME'
OPERATOR = 'OPERATOR'
ISPIS = 'ISPIS'
DODELA = 'DODELA'
KRAJ = 'KRAJ'


token_exprs = [
    (r'[\n\t]+',                None),  #Praznine
    (r'(\/\/.*\/\/)',           None),  #Komentar
    (r'\=',                     DODELA),
    (r'\+',                     OPERATOR),
    (r'-',                      OPERATOR),
    (r'\*',                     OPERATOR),
    (r'/',                      OPERATOR),
    (r'stampaj',                ISPIS),
    (r';',                      KRAJ),
    (r'[0-9]+',                 BROJ),
    (r'[A-Za-z][A-Za-z0-9_]*',  IME),
]

def tech_lex(characters):
    return lexing.lex(characters, token_exprs)