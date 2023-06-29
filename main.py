import flet as ft
from docxtpl import DocxTemplate
import datetime


def create_new_book(number1, name_si, car, name_driver):
    # number_pr = number2.get()
    doc = DocxTemplate('templates/Шаблон_материального_пропуска.docx')
    context = {'number': (number1),
               'name_si': (name_si),
               'car': (car),
               "name_driver": (name_driver),
               "today": (datetime.date.today())}
    doc.render(context)

    return doc.save(
         ".docx")


def main(page):
    def btn_click(e):
        if not number_mp.value and total.value and number_machine.value and driver.value:
            number_mp.error_text = "Please enter your name"
            page.update()
        else:
            name = number_mp.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

            create_new_book(
                number1=number_mp,
                name_si=total,
                car=number_machine,
                name_driver=driver
            )

    number_mp = ft.TextField(label="Номер материального пропуска")
    total = ft.TextField(label="Кол_во СИ")
    number_machine = ft.TextField(label="Номер машины")
    driver = ft.TextField(label="Имя водителя")

    page.add(number_mp,
             total,
             number_machine,
             driver,
             ft.ElevatedButton("Создать материальный пропуск", on_click=btn_click))


ft.app(target=main)
