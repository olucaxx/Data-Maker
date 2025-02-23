import random

male_names = ["João", "Pedro", "Lucas", "Gabriel", "Mateus", "Enzo", "Rafael", "Felipe", "Daniel", "André", "Carlos", "Eduardo", "Thiago", 
            "Marcelo", "Vinícius", "Leonardo", "Rodrigo", "Bruno", "Gustavo", "Arthur", "Davi", "Samuel", "Caio", "Diego", "Renato", "Igor", 
            "Roberto", "Ricardo", "Murilo", "Otávio", "Guilherme", "Henrique", "Luiz", "Cauã", "Nathan"]

female_names = ["Ana", "Maria", "Laura", "Sofia", "Isabella", "Manuela", "Alice", "Clara", "Beatriz", "Mariana", "Gabriela", "Rafaela", 
                "Carolina", "Larissa", "Camila", "Julia", "Valentina", "Amanda", "Letícia", "Vitória", "Eduarda", "Helena", "Luiza", 
                "Isadora", "Sophia", "Lívia", "Yasmin", "Bianca", "Fernanda", "Natália", "Rebeca", "Raquel", "Patrícia", "Aline", "Cecília"]

surnames = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", 
            "Martins", "Carvalho", "Araújo", "Melo", "Barbosa", "Monteiro", "Teixeira", "Nascimento", "Fernandes", "Mendes", "Dias", 
            "Cunha", "Rocha", "Moreira", "Cardoso", "Neves", "Machado", "Cavalcanti", "Freitas", "Correia", "Reis", "Guimarães", "Vieira"]
    
genders = ["male", "female"]

format = ["upper", "lower", "capitalized"]    
    
def generate_random_name(gender = "male", compound = False, surname = True, format = "capitalized"):
    names = male_names if gender == "male" else female_names
    
    name = random.choice(names)
    
    if compound:
        name += " " + random.choice(names)
        
    if surname:
        name += " " + random.choice(surnames)
    
    match format:
        case "upper":
            return name.upper()
            
        case "lower":
            return name.lower()
        
        case "capitalized":
            return name
    