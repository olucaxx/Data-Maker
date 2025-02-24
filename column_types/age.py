from random import randint

class Age:
    
    def __init__(self, min:int = 18, max:int = 60):
        self.age = self.generate_random_age(min, max)
        
        
    def generate_random_age(self, min:int, max:int) -> int:
        return randint(min, max)
    
    
    def __str__(self):
        return f"{self.age}"
    
    
if __name__ == "__main__":
    print(Age())