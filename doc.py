from docxtpl import DocxTemplate


def create_new_book(number, name_si, osnovaie, extr_osnovanie, name_osn, car, name_driver, where, extra_where, why,
                    extra_car, extra_name_driver, today, time):
    doc = DocxTemplate('templates/Шаблон_материального_пропуска.docx')
    context = {'number': number,
               'name_si': name_si,
               'osnovaie': osnovaie,
               'extr_osnovanie': extr_osnovanie,
               'name_osn': name_osn,
               'extra_car': extra_car,
               'extra_name_driver': extra_name_driver,
               'car': car,
               "name_driver": name_driver,
               'where': where,
               'extra_where': extra_where,
               'why': why,
               "today": today,
               'time': time
               }
    doc.render(context)

    return doc.save(f"Материальный пропуск №{number}.docx")


if __name__ == '__main__':
    create_new_book()
