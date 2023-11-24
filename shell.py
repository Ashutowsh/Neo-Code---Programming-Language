from lexer import Lexer
from parser_1 import Parser
from interpreter import Interpreter
from info import Info
info = Info()
while True :
  inpText = input("Enter text : ")
  lexer = Lexer(inpText)
  arr = lexer.tokenization()
  # print(arr)
  parser = Parser(arr)
  tree = parser.parse()
  # print(tree)
  interpreter = Interpreter(tree, info)
  output = interpreter.interpret()
  print(output)