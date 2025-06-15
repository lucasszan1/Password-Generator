import random
import string

class GeneratedPasword():

#Função que gera a senha.
    def generate(self, size = 12, use_symbols = True, use_numbers = True, use_upper = True, use_lowers = True):
        caracteres = ''

        if use_symbols:
            caracteres += string.punctuation
    
        if use_numbers: 
            caracteres += string.digits

        if use_upper:
            caracteres += string.ascii_uppercase

        if use_lowers:
            caracteres += string.ascii_lowercase

        if not caracteres:
            return None

        return ''.join(random.choice(caracteres) for _ in range(size))
   
  