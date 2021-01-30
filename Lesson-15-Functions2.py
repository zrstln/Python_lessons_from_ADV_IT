def create_record(name, telefone, address):
    """Create record"""
    record = {
        'name': name,
        'phone': telefone,
        'address': address
    }
    return record


user1 = create_record("Vasya", "+7161651656515616", "Stavvvrooooppppoool")
user2 = create_record("Petya", "+71561641564645641", "kwebfwerfvhweb")
print(user1)
print(user2)

def give_award(medal, *persons):
    """Give medal to persons"""
    for person in persons:
        print("Товарищ " + person.title() + " награждается медалью " + medal)


give_award("За Берлин", "иванов", "петров")
give_award("За Вену", "Сидоров", "Нестеров", "Пряников")
