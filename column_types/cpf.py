from random import randint

class CPF:
    
    def __init__(self):
        self.cpf = self.generate_cpf()


    def calculate_verifier_digit(self, cpf_numbers, weight):
        sum = 0
        for i, digit in enumerate(cpf_numbers):
            sum += int(digit) * (weight - i)
            
        remainder = sum % 11
        if remainder < 2:
            return 0
        else:
            return 11 - remainder


    def generate_cpf(self):
        cpf_numbers = [randint(0, 9) for _ in range(9)]
        
        cpf_numbers.append(self.calculate_verifier_digit(cpf_numbers, 10))
        cpf_numbers.append(self.calculate_verifier_digit(cpf_numbers, 11))
        
        return ''.join(map(str, cpf_numbers))
        
        
    def __str__(self):
        return f"{self.cpf}"
    
if __name__ == "__main__":
    print(CPF())