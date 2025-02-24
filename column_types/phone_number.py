from enum import Enum
from random import choice as random_choice
from random import random as random_int

class PhoneNumber:
        
    br_area_codes = [
        11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 
        41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 
        69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 
        96, 97, 98, 99
    ]
    
    def __init__(self, area_code:bool = True):
        self.phone_number = self.generate_random_number(area_code)


    def generate_random_number(self, area_code: bool) -> str:
        phone_number = ""
        
        if area_code:
            phone_number += str(random_choice(self.br_area_codes))
            
        return phone_number + "9" + str(int(random_int() * 10 ** 8))
        

    def __str__(self):
        return f"{self.phone_number}"
    