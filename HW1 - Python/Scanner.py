#Austin Keelin - ajk0033
#Assignment 1

#Class Scanner - Reads a TINY program and emits tokens
from Token import Token 

class Scanner:    

   # Constructor - Is passed a file to scan and outputs a token 
   # each time nextToken() is invoked. Fails gracefully if file does
   # not exist   
   def __init__(self, fileName):
      try:            
         self.position = 0            
         self.fileName = fileName           
         self.nextChar() 
      except IOError:
         print("The file does not exist")    
      
   # Function nextChar() returns the next character in the file            
   def nextChar(self):                
      self.f = open(self.fileName)            
      self.f.seek(self.position)                
      self.c = self.f.read(1)            
         
      if not self.c:                   
         self.c = 'eof'                 
      else:                       
         self.position = self.f.tell()                 
      self.f.close()     
         
   # Function nextToken() reads characters in the file and returns  
   # the next token 
   def nextToken(self):
      #eof
      if self.c == 'eof':
         token = Token(Token.EOF, 'eof')
         return token
         sys.exit(1)
      #LPAREN                  
      elif self.c == '(':
         token = Token(Token.LPAREN, '(')
         self.nextChar()
         return token
      #RPAREN   
      elif self.c == ')':
         token = Token(Token.RPAREN, ')')
         self.nextChar()
         return token
      #ADDOP   
      elif self.c == '+':
         token = Token(Token.ADDOP, '+')
         self.nextChar()
         return token
      #SUBOP   
      elif self.c == '-':
         token = Token(Token.SUBOP, '-')
         self.nextChar()
         return token
      #MULOP   
      elif self.c == '*':
         token = Token(Token.MULOP, '*')
         self.nextChar()
         return token
      #DIVOP   
      elif self.c == '/':
         token = Token(Token.DIVOP, '/')
         self.nextChar()
         return token 
      #EQUAL     
      elif self.c == '=':
         token = Token(Token.EQUAL, '=')
         self.nextChar()
         return token 
      #whitespace   
      elif self.c.isspace():                       
         str = ''                        
         while self.c.isspace():
            if(self.c == " "):
               self.c = ''
            elif(self.c == "\n"):
               self.c = ''                             
            str += self.c                              
            self.nextChar()                       
         token = Token(Token.WS, str)
         return token
      #ID & print   
      elif self.c.isalpha():
         str = ''
         while self.c.isalpha():
            str += self.c
            self.nextChar()
         if str == 'print':
            token = Token(Token.PRINT, str)
            return token
         else:
            token = Token(Token.ID, str)   
            return token
      #INT      
      elif self.c.isdigit():
         int = ''
         while self.c.isdigit():
            int += self.c
            self.nextChar()
         token = Token(Token.INT, int)
         return token
      #Unknown             
      else:                                             
         token = Token('unknown', 'unknown') 
         self.nextChar()
         return token