from random import choice as random_choice
from enum import Enum

class Name: 
    
    class Format(Enum):
        UPPER = "upper"
        LOWER = "lower"
        CAPITALIZED = "capitalized" 

    male_names = ["João", "Pedro", "Lucas", "Gabriel", "Mateus", "Enzo", "Rafael", "Felipe", "Daniel", "André", "Carlos", "Eduardo", "Thiago", 
                "Marcelo", "Vinícius", "Leonardo", "Rodrigo", "Bruno", "Gustavo", "Arthur", "Davi", "Samuel", "Caio", "Diego", "Renato", "Igor", 
                "Roberto", "Ricardo", "Murilo", "Otávio", "Guilherme", "Henrique", "Luiz", "Cauã", "Nathan"]

    female_names = ["Ana", "Maria", "Laura", "Sofia", "Isabella", "Manuela", "Alice", "Clara", "Beatriz", "Mariana", "Gabriela", "Rafaela", 
                    "Carolina", "Larissa", "Camila", "Julia", "Valentina", "Amanda", "Letícia", "Vitória", "Eduarda", "Helena", "Luiza", 
                    "Isadora", "Sophia", "Lívia", "Yasmin", "Bianca", "Fernanda", "Natália", "Rebeca", "Raquel", "Patrícia", "Aline", "Cecília"]

    surnames = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", 
                "Martins", "Carvalho", "Araújo", "Melo", "Barbosa", "Monteiro", "Teixeira", "Nascimento", "Fernandes", "Mendes", "Dias", 
                "Cunha", "Rocha", "Moreira", "Cardoso", "Neves", "Machado", "Cavalcanti", "Freitas", "Correia", "Reis", "Guimarães", "Vieira"]

    def __init__(self, format:Format = Format.CAPITALIZED):
        self.name = self.generate_random_name(format)


    def generate_random_name(self, format:Format):
        genre = random_choice((self.male_names, self.female_names))
        
        match format:
            case format.CAPITALIZED:
                return random_choice(genre).capitalize() + " " + random_choice(genre).capitalize() + " " + random_choice(self.surnames).capitalize()
            
            case format.UPPER:
                return random_choice(genre).upper() + " " + random_choice(genre).upper() + " " + random_choice(self.surnames).upper()
            
            case format.LOWER:
                return random_choice(genre).lower() + " " + random_choice(genre).lower() + " " + random_choice(self.surnames).lower()
            
            
    def __str__(self):
        return f"{self.name}"