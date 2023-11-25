from tokens import Integer, Float
class Interpreter:
  def __init__(self, tree, var_data):
    self.tree = tree
    self.var_data = var_data

  def interpret(self, tree = None):
    if tree == None:
      tree = self.tree

    if tree[0].type == "METH":
      if len(tree) == 1 :
        return self.processMethod()
      else :
        return self.var_data.get_value(tree[1])

    if not isinstance(tree, list):
      return tree

    if isinstance(tree, list) and len(tree)==2 :
      exp = tree[1]
      if isinstance(exp, list):
        exp = self.interpret(exp)
      return self.unary_operation(tree[0], exp)

    operator = tree[1]
    left_node = tree[0]
    if isinstance(left_node, list):
      left_node = self.interpret(left_node)
    right_node = tree[2]
    if isinstance(right_node, list):
      right_node = self.interpret(right_node)

    return self.solve(left_node, operator, right_node)

  def processMethod(self):
    if self.tree[0].value == "show":
      return self.var_data.read_all_variables()

  def read_INT(self, value):
    return int(value)

  def read_FLT(self, value):
    return float(value)

  def read_VAR(self, id):
    variable = self.var_data.read(id)
    variable_type = variable.type

    return getattr(self, f"read_{variable_type}")(variable.value)

  def solve(self, left, operator, right):
    output = 0
    left_type = "VAR" if str(left.type).startswith("VAR") else str(left.type)
    right_type = "VAR" if str(right.type).startswith("VAR") else str(right.type)

    if operator.value == "=":
      left.type = f"VAR{right_type}"
      self.var_data.write(left, right)
      return self.var_data.get_value(left)

    left_value = getattr(self, f"read_{left_type}")(left.value)
    right_value = getattr(self, f"read_{right_type}")(right.value)

    if operator.value == "+" :
      output = left_value + right_value
    elif operator.value == "-":
      output = left_value - right_value
    elif operator.value == "*":
      output = left_value * right_value
    elif operator.value == "/":
      output = left_value / right_value
    elif operator.value == ">":
      output = 1 if left_value > right_value else 0
    elif operator.value == ">=":
      output = 1 if left_value >= right_value else 0
    elif operator.value == "<":
      output = 1 if left_value < right_value else 0
    elif operator.value == "<=":
      output = 1 if left_value <= right_value else 0
    elif operator.value == "?=":
      output = 1 if left_value == right_value else 0
    elif operator.value == "and":
      output = 1 if left_value and right_value else 0
    elif operator.value == "or":
      output = 1 if left_value or right_value else 0
    return Integer(output) if (left_type=="INT" and right_type=="INT") else Float(output)

  def unary_operation(self, operator, operand):
    operand_type = "VAR" if str(operand.type).startswith("VAR") else str(operand.type)
    operand = getattr(self, f"read_{operand_type}")(operand.value)

    if operator.value == "+":
      return +operand
    elif operator.value == "-":
      return -operand
    elif operator.value=="not":
      return 1 if not operand else 0