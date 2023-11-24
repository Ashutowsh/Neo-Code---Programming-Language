class Info:
  def __init__(self):
    self.var_list = {}

  def get_value(self, key1):
    return f"[{key1.value} : {self.read(key1.value)}]"

  def read(self, key):
    return self.var_list[key]

  def read_all_variables(self):
    return self.var_list

  def write(self, var_name, exp):
    var_value = var_name.value
    self.var_list[var_value] = exp