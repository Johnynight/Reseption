from docxtpl import DocxTemplate
from django.http import HttpResponse


def create_new_book(number, name_si, osnovaie, extr_osnovanie, name_osn, car, name_driver, where, extra_where, why,
                    extra_car, extra_name_driver, today, time, gos_number,exstra_why):
    doc = DocxTemplate('templates/templates.docx')
    context = {'number': number,
               'name_si': name_si,
               'osnovaie': osnovaie,
               'extr_osnovanie': extr_osnovanie,
               'name_osn': name_osn,
               'extra_car': extra_car,
               'extra_name_driver': extra_name_driver,
               'car': car,
               'gos_number':gos_number ,
               "name_driver": name_driver,
               'where': where,
               'extra_where': extra_where,
               'why': why,
               'exstra_why' : exstra_why,
               "today": today,
               'time': time
               }
    doc.render(context)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=mydocument.docx'
    doc.save(response)
    return response





if __name__ == '__main__':
    create_new_book()
