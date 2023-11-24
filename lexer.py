from tokens import Integer, Float, Operator, Method, Declaration, Variable, Boolean, Comparator
class Lexer:
    digits = "0123456789"
    stopWords = " "
    operators = "+-/*()="
    specialCharacters = "<>?="
    letters = "abcdefghijklmnopqrstuvwxyz"
    declarations = ["create"]
    methods = ["show"]
    comparators = ["<", ">", "<=", ">=", "?="]
    boolean = ["and", "or", "not"]
    # reserved = ["if", "elif", "else", "do", "while"]

    def __init__(self, inpText):
        self.inpText = inpText
        self.index = 0
        self.currentChar = self.inpText[self.index]
        self.token_arr = []
        self.token = None

    def tokenization(self):
        while self.index < len(self.inpText):
          if self.currentChar in Lexer.digits:
            self.token = self.getNumber()
          elif self.currentChar in Lexer.operators:
            self.token = Operator(self.currentChar)
            self.move()
          elif self.currentChar in Lexer.letters:
            self.token = self.getWord()
          elif self.currentChar in Lexer.specialCharacters:
            self.token = self.getComparator()
          elif self.currentChar in Lexer.stopWords:
            self.move()
            continue
          self.token_arr.append(self.token)

        return self.token_arr

    def getNumber(self):
      isDecimalPresent = False
      ans = ""
      while self.index<len(self.inpText) and (self.currentChar in Lexer.digits or self.currentChar=='.'):
        if self.currentChar == '.':
          isDecimalPresent = True
        ans+=self.currentChar
        self.move()

      return Float(ans) if isDecimalPresent else Integer(ans)

    def getWord(self):
      word=""
      while self.index<len(self.inpText) and self.currentChar in Lexer.letters:
        word+=self.currentChar
        self.move()
      if word in Lexer.declarations :
        output = Declaration(word)
      elif word in Lexer.methods :
        output = Method(word)
      elif word in Lexer.boolean:
        output = Boolean(word)
      else :
        output = Variable(word)

      return output
    def getComparator(self):
      comparator = ""
      while self.index<len(self.inpText) and self.currentChar in Lexer.specialCharacters:
        comparator+=self.currentChar
        self.move()
      return Comparator(comparator)

    def move(self):
      self.index+=1
      if self.index < len(self.inpText):
        self.currentChar = self.inpText[self.index]