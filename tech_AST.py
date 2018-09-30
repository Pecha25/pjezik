from podudaranje import *

#--------------------------------------------------------------------------#
class Aexp(Podudaranje):                    #ARITMETIČKI IZRAZI
    pass

class IntAexp(Aexp):                            
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return 'IntAexp(%d)' % self.i

class VarAexp(Aexp):
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return 'VarAexp(%s)' % self.name

class BinopAexp(Aexp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return 'BinopAexp(%s, %s, %s)' % (self.op, self.left, self.right)
#--------------------------------------------------------------------------#
class Bexp(Podudaranje):                    #LOGIČKI IZRAZI
    pass

class RelopBexp(Bexp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
    
    def __repr__(self):
        return 'RelopBexp(%s, %s, %s)' % (self.op, self.left, self.right)

class AndBexp(Bexp):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __repr__(self):
        return 'AndBexp(%s, %s)' % (self.left, self.right)

class OrBexp(Bexp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return 'OrBexp(%s, %s)' % (self.left, self.right)

class NotBexp(Bexp):
    def __init__(self, exp):
        self.exp = exp
    
    def __repr__(self):
        return 'NotBexp(%s)' % (self.exp)

#--------------------------------------------------------------------------#
class Statement(Podudaranje):               #KOMBINACIJA LOGIČKIH I ARITMETIČKIH ISKAZA POPUT DODELE, OBRAZCA, IF i WHILE-a
    pass

class AssignStatement(Statement):
    def __init__(self, name, aexp):
        self.name = name
        self.aexp = aexp

    def __repr__(self):
        return 'AssignStatement(%s, %s)' % (self.name, self.aexp)

class CompoundStatement(Statement):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return 'CompoundStatement(%s, %s)' % (self.first, self.second)

class IfStatement(Statement):
    def __init__(self, condition, true_stmt, false_stmt):
        self.condition = condition
        self.true_stmt = true_stmt
        self.false_stmt = false_stmt
    def __repr__(self):
        return 'IfStatement(%s, %s, %s)' % (self.condition, self.true_stmt, self.false_stmt)

class WhileStatement(Statement):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __repr__(self):
        return 'WhileStatement(%s, %s)' % (self.condition, self.body)