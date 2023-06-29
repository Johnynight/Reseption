import flet as ft
import doc


def main(page):
    page.title = "Форма материального пропуска"

    def btn_click(e):
        if not number_mp.value and total.value and number_machine.value and driver.value:
            number_mp.error_text = "Please enter your value"
            page.update()
        else:
            name = number_mp.value
            # page.add(ft.Text(f"Hello, {name}!"))

            doc.create_new_book(
                number=number_mp.value,
                name_si=total.value,
                car=number_machine.value,
                name_driver=driver_dropdown.value
            )

    driver_dropdown = ft.Dropdown(
        width=200,
        label='Имя водителя',
        options=[
            ft.dropdown.Option('Алмаз'),
            ft.dropdown.Option('Нуржигит'),
            ft.dropdown.Option('Адиль'),
        ]
    )
    number_mp = ft.TextField(label="Номер материального пропуска")
    total = ft.TextField(label="Кол_во СИ")
    number_machine = ft.TextField(label="Номер машины")
    driver = ft.TextField(label=driver_dropdown.value)

    page.add(ft.Text("Материального пропуска", size=30, color="Yellow"),
             number_mp,
             total,
             number_machine,
             driver_dropdown,
             ft.ElevatedButton("Создать материальный пропуск", on_click=btn_click))


ft.app(target=main)
