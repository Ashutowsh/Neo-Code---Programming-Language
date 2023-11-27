class Token:
  def __init__(self, type, value):
    self.type = type
    self.value = value

  def __repr__(self):
    return str(self.value)

class Integer(Token):
  def __init__(self, value):
    super().__init__("INT", value)

class Float(Token):
  def __init__(self, value):
    super().__init__("FLT", value)

class Operator(Token):
  def __init__(self, value):
    super().__init__("OPERATOR", value)

class Variable(Token):
  def __init__(self, value):
    super().__init__("VAR(?)", value)

class Declaration(Token):
  def __init__(self, value):
    super().__init__("DECL", value)

class Method(Token):
  def __init__(self, value):
    super().__init__("METH", value)

class Boolean(Token):
  def __init__(self, value):
    super().__init__("BOOL", value)
class Comparator(Token):
  def __init__(self, value):
    super().__init__("COMPARATOR", value)
class Reserved(Token):
  def __init__(self, value):
    super().__init__("RESERVED", value)