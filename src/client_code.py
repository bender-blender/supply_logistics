from components import (
    Box,
    Container
)


def client_code_box(box: Box):
    """Кнопка для отправки коробки

    Args:
        box (Box): _description_
    """
    print(f"Коробка {box.name}: ", *box.func())


client_code_box(Box("Почта", ["Посылка 1", "Посылка 2", "Посылка 3"]))


def client_code_container(container: Container, *args: Box):
    for box in args:
        container.add(box)
    print(container.func())


client_code_container(Container(), Box(
    "Почта", ["Посылка 1", "Посылка 2", "Посылка 3"]),
    Box("Детали",["Болты","Шурупы","Гвозди"]))
