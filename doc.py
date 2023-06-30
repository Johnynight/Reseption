from docxtpl import DocxTemplate
import datetime

date = datetime.datetime.today()
today = date.strftime("%d.%m.%y")
def create_new_book(number, name_si, car, name_driver):
    doc = DocxTemplate('templates/Шаблон_материального_пропуска.docx')
    context = {'number': (number),
               'name_si': (name_si),
               'car': (car),
               "name_driver": (name_driver),
               "today": (today)}
    doc.render(context)

    return doc.save(f"{number}.docx")
