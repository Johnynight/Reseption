import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)
from docxtpl import DocxTemplate

def create_new_book(output_path, number, name_si, osnovaie, extr_osnovanie, name_osn, car, name_driver, where, extra_where, why,
                    extra_car, extra_name_driver, today, time, gos_number, exstra_why):
    doc = DocxTemplate('templates/templates.docx')
    context = {
        'number': number,
        'name_si': name_si,
        'osnovaie': osnovaie,
        'extr_osnovanie': extr_osnovanie,
        'name_osn': name_osn,
        'extra_car': extra_car,
        'extra_name_driver': extra_name_driver,
        'car': car,
        'gos_number': gos_number,
        'name_driver': name_driver,
        'where': where,
        'extra_where': extra_where,
        'why': why,
        'exstra_why': exstra_why,
        'today': today,
        'time': time
    }
    doc.render(context)
    doc.save(output_path)

def main(page: Page):

    # Save file dialog
    def save_file_result(e: FilePickerResultEvent):
        if e.path:
            save_file_path.value = e.path
            save_file_path.update()
            create_new_book(
                output_path=e.path,
                number='12345',
                name_si='John Smith',
                osnovaie='Some reason',
                extr_osnovanie='Extra reason',
                name_osn='Supervisor Name',
                car='Toyota Camry',
                name_driver='Jane Doe',
                where='City Center',
                extra_where='Suburb',
                why='Business meeting',
                extra_car='Nissan Altima',
                extra_name_driver='Alex Johnson',
                today='2023-08-18',
                time='15:00',
                gos_number='AB123CD',
                exstra_why='Client visit'
            )
        else:
            save_file_path.value = "Cancelled!"
            save_file_path.update()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    page.overlay.extend([save_file_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Save file",
                    icon=icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web,
                ),
                save_file_path,
            ]
        ),
    )

flet.app(target=main)
