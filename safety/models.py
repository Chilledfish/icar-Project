import csv

makes = [["Aiways"], ["Alfa-Romeo"], ["Audi"], ["BMW", "Mini"], ["Chevrolet"], ["Citroen", "Citroën"], ["Dacia"], ["DS"], ["Fiat"],
         ["Ford"], ["Honda"], ["Hyundai", "Genesis"], ["Isuzu"], ["Jaguar"], ["Jeep"], ["Kia"], ["Lancia"], ["Land-Rover"],
         ["Lexus"], ["Lynk & Co"], ["Maserati"], ["Mazda"], ["Mercedes", "Mercedes-Benz"], ["MG"], ["Mitsubishi"],
         ["Nissan", "Infiniti"], ["Opel", "Opel/Vauxhall"], ["Peugeot"], ["Porsche"], ["Renault"], ["Seat", "Cupra"],
         ["Skoda", "Škoda"], ["Smart"], ["Ssangyong"], ["Subaru"], ["Suzuki"], ["Tesla"], ["Toyota"], ["Volkswagen", "VW"],
         ["Volvo"]]
yazranim = ["איווייס", "אלפא רומיאו", "אאודי", "ב מ וו", "שברולט", "סיטרואן", "דאציה", "די אס", "פיאט", "פורד", "הונדה", "יונדאי",
		    "איסוזו", "יגואר", "ג'יפ", "קיה", "לנצ'יה", "לנדרובר", "לקסוס", "לינק אנד קו", "מזארטי", "מזדה", "מרצדס", "מג",
            "מיצובישי", "ניסאן", "אופל", "פיג'ו", "פורשה", "רנו", "סיאט", "סקודה", "סמארט", "סאנגיונג", "סובארו",
            "סוזוקי", "טסלה", "טויוטה", "פולקסווגן", "וולוו"]


dic = {}
for i in range(len(makes)):
    for j in range(len(makes[i])):
        dic[makes[i][j]] = yazranim[i]

keys = [i for i in dic]



with open('makes.csv', 'w', encoding='utf-8') as csvwriter:
    writer = csv.DictWriter(csvwriter, fieldnames=keys)
    writer.writeheader()
    writer.writerow(dic)





print(makes)

