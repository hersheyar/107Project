name = "Andrew"
age = 27
height = "6ft"
weight = 230


def create_dictionary():
    personal_info = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight
    }
    return personal_info



dictionary = create_dictionary()
print(dictionary)