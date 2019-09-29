from django.core.exceptions import ValidationError
import re
from datetime import date, datetime

email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
#letras = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
letras_regex=r"(^[a-zA-Z]+$)"
phone_regex= r"(^[0-9]+[0-9]+[0-9]+[0-9]+-[0-9]+[0-9]+[0-9]+[0-9]+$)"
dui_regex=r"(^[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+-+[0-9]$)"
nit_regex= r"(^[0-9]+[0-9]+[0-9]+[0-9]+-[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+-[0-9]+[0-9]+[0-9]+-[0-9]$)"
nrc_regex=r"(^[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+-[0-9]$)"

def validate_nombre(value):
      if value and not re.match(letras_regex,value):
            raise ValidationError("El nombre debe contener solo letras")
            return value
      if not len (value)>3:
            raise ValidationError("El nombre debe de tener mínimo 3 letras") 
            
def validate_apellido(value):
      if value and not re.match(letras_regex,value):
            raise ValidationError("El apellido debe contener solo letras")
            return value
      if not len (value)>3:
            raise ValidationError("El apellido debe de tener mínimo 3 letras") 

def validate_texto(value):
      if value and not re.match(letras_regex,value):
            raise ValidationError("Escriba una especialidad válida")
            return value
      if not len(value)>3:
            raise ValidationError("La especialidad debe tener mínimo 3 letras")     

def validate_telefono(value):
      if value and not re.match(phone_regex,value):
            raise ValidationError("Ingrese un número valido con el siguiente formato: 9999-9999")
            return value 

def validate_email(value):
      if value and not re.match(email_regex, value):
            raise ValidationError("Introduzca una dirección de correo electrónico válida")
            return value

def validate_dui(value):
      if value and not re.match(dui_regex,value):
             raise ValidationError("Ingrese un número de DUI válido")
             return value
def validate_nit(value):
      if value and not re.match(nit_regex,value):
            raise ValidationError("Ingrese un número de NIT válido")
            return value
def validate_nrc(value):
      if value and not re.match(nrc_regex,value):
            raise ValidationError("Ingrese un número de registro de contribuyente válido")
            return value
#PACIENTE
         
