#Austin Keelin - ajk0033
#Assignment 1

#  Class Token - Encapsulates the tokens in TINY 
#
#   type = the type of token 
#   text = the text of the token
class Token:      
   # Token Class Variables      
   EOF = "eof"     
   LPAREN = "("     
   RPAREN = ")"     
   ADDOP = "+"  
   SUBOP = "-"  
   MULOP = "*"
   DIVOP = "/"
   EQUAL = "="
   WS = "whitespace"
   ID = "ID"
   INT = "INT"
   PRINT = "print"     
   
   # Constructor        
   def __init__(self, type, text):            
      self.type = type 
      self.text = text      
   
   # String representation of an instance of Token      
   def toString(self):            
      return '[Type:{}, Text:{}]'.format(self.type, self.text)
   
   # Returns the text of a token   
   def getText(self):
      return self.text
   
   # Returns the type of a token   
   def getType(self):
      return self.type