import pickle

NCAP_makes = ["AIWAYS", "ALFA-ROMEO", "AUDI", "BMW", "CHEVROLET", "CITROEN", "DACIA", "DS", "FIAT", "FORD", "HONDA",
              "HYUNDAI", "ISUZU", "JAGUAR", "JEEP", "KIA", "LANCIA", "LAND-ROVER", "LEXUS", "LYNK & CO", "MASERATI",
              "MAZDA", "MERCEDES", "MG", "MINI", "MITSUBISHI", "NISSAN", "OPEL", "PEUGEOT", "PORSCHE", "RENAULT",
              "SEAT", "SKODA", "SMART", "SSANGYONG", "SUBARU", "SUZUKI", "TESLA", "TOYOTA", "VOLKSWAGEN", "VOLVO"]

first_word_makes = ["Aiways", "Alfa", "Audi", "BMW", "Mini", "Chevrolet", "Citroen", "Citroën", "Dacia", "DS", "Fiat",
                    "Ford", "Honda", "Hyundai", "Genesis", "Isuzu", "Jaguar", "Jeep", "Kia", "Lancia", "Land",
                    "Lexus", "Lynk", "Maserati", "Mazda", "Mercedes", "Mercedes", "MG", "Mitsubishi",
                    "Nissan", "Infiniti", "Opel", "Opel/Vauxhall", "Peugeot", "Porsche", "Renault", "Seat", "Cupra",
                    "Skoda", "Škoda", "Smart", "Ssangyong", "Subaru", "Suzuki", "Tesla", "Toyota", "Volkswagen", "VW",
                    "Volvo"]

two_word_makes = {"Alfa": 1,
                  "Land": 20,
                  "Mercedes": 25,
                  "Lynk": 22
                  }

yazranim = ["איווייס", "אלפא רומיאו", "אאודי", "ב מ וו", "שברולט", "סיטרואן", "דאציה", "די אס", "פיאט", "פורד", "הונדה",
            "יונדאי",
            "איסוזו", "יגואר", "ג'יפ", "קיה", "לנצ'יה", "לנדרובר", "לקסוס", "לינק אנד קו", "מזארטי", "מזדה", "מרצדס",
            "מג",
            "מיצובישי", "ניסאן", "אופל", "פיג'ו", "פורשה", "רנו", "סיאט", "סקודה", "סמארט", "סאנגיונג", "סובארו",
            "סוזוקי", "טסלה", "טויוטה", "פולקסווגן", "וולוו"]

base_url = "https://www.euroncap.com/en/"

makes = ["Alfa-Romeo", "Audi", "BMW", "Chevrolet", "Citroen", "Dacia", "DS", "Fiat",
         "Ford", "Honda", "Hyundai", "Isuzu", "Jaguar", "Jeep", "Kia", "Lancia", "Land-Rover",
         "Lexus", "Lynk & Co", "Maserati", "Mazda", "Mercedes", "MG", "Mitsubishi",
         "Nissan", "Opel", "Peugeot", "Porsche", "Renault", "Saab", "Seat",
         "Skoda", "Smart", "Ssangyong", "Subaru", "Suzuki", "Tesla", "Toyota", "Volkswagen",
         "Volvo"]

data_makes = ["אלפא רומיאו", "אאודי", "ב מ וו", "שברולט", "סיטרואן", "דאצ'יה", "די.אס", "פיאט", "פורד",
              "הונדה", "יונדאי", "איסוזו", "יגואר", "ג'יפ", "קיה", "לנצ'יה", "לנדרובר", "לקסוס", "לינק אנד קו",
              "מזראטי", "מזדה", "מרצדס", "מ.ג", "מיצובישי", "ניסאן", "אופל", "פיג'ו", "פורשה", "רנו", "סיאט",
              "סקודה", "סמארט", "סאנגיונג", "סובראו", "סוזוקי", "טסלה", "טויוטה", "פולקסווגן", "וולוו"]

ncap_data_dict = dict(zip(makes, data_makes))

small_makes = [make.lower() for make in makes]

make_exceptions = {"opel/Vauxhall": "Opel",
                   "lynk-&amp;-co": "Lynk & Co",
                   "mini": "BMW",
                   "genesis": "Hyundai",
                   "cupra": "Seat",
                   "škoda": "Skoda",
                   "citroën": "Citroen",
                   "vw": "Volkswagen",
                   "mercedes-benz": "Mercedes",
                   "range-rover": "Land-Rover",
                   "infiniti": "Nissan",
                   "geely-emgrand": "Geely"
                   }

makes_dict = dict(zip(small_makes, makes))

makes_dict.update(make_exceptions)