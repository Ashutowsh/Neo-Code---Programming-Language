class Parser:
  def __init__(self, token_arr):
    self.token_arr = token_arr
    self.index = 0
    self.token = self.token_arr[self.index]

  def parse(self):
    if self.token.type=="INT" or self.token.type=="FLT" or self.token.type=="OPERATOR" or self.token.value=="not":
      return self.booleanExpression()
    elif self.token.type=="DECL":
      return self.assignVariable()
    elif self.token.type=="METH" :
      return self.handleMethod()

  def factor(self):
    if self.token.type == "INT" or self.token.type == "FLT":
      return self.token
    elif self.token.type.startswith("VAR"):
       return self.token
    elif self.token.value == "(":
      self.move()
      return self.booleanExpression()
    elif self.token.value == "not":
      operator = self.token
      self.move()
      output = [operator, self.booleanExpression()]
      return output
    elif self.token.value == "+" or self.token.value == "-":
      operator = self.token
      self.move()
      operand = self.boolean_expression()
      return [operator, operand]

  def term(self):
    t = self.factor()
    self.move()
    while self.token.value == "*" or self.token.value == "/":
      op = self.token
      self.move()
      right = self.factor()
      self.move()
      t = [t, op, right]
    return t

  def expression(self):
    exp = self.term()
    while self.token.value == "+" or self.token.value == "-":
      op = self.token
      self.move()
      right = self.term()
      exp = [exp, op, right]
    return exp

  def getVariable(self):
    if self.token.type.startswith("VAR"):
      return self.token

  def assignVariable(self):
    self.move()
    var_name = self.getVariable()
    self.move()
    if self.token.value=="=":
      operation = self.token
      self.move()
      var_value = self.booleanExpression()
      return [var_name, operation, var_value]

  def handleMethod(self):
    if self.token.value == "show":
      output = [self.token]
      self.move()
      if self.token.type.startswith("VAR"):
        output.append(self.token)
      return output

  def booleanExpression(self):
    exp = self.comparisonExpression()
    while self.token.type=="BOOL":
      op = self.token
      self.move()
      right = self.comparisonExpression()
      exp = [exp, op, right]
    return exp

  def comparisonExpression(self):
    exp = self.expression()
    while self.token.type=="COMPARATOR":
      op = self.token
      self.move()
      right = self.expression()
      exp = [exp, op, right]
    return exp

  def move(self):
    self.index+=1
    if self.index<len(self.token_arr):
      self.token = self.token_arr[self.index]