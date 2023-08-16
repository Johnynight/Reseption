import flet as ft
# import doc
import datetime
#import create_excel


def main(page: ft.Page):
    page.scroll = True
    page.title = "Форма материального пропуска"
    # img = ft.Image(
    #     width=200,
    #     height=75,
    #     src=f'/Users/slavachurikov/PycharmProjects/flet/borusan.png',
    #     fit=ft.ImageFit.CONTAIN,
    # )

    def btn_click(e):
        if not number_mp.value:
            number_mp.error_text = "Обязательно заполните поле"
            page.update()
        else:
            # doc.create_new_book(
            #     number=number_mp.value,
            #     name_si=total.value,
            #     osnovaie=osnovanie_dropdown.value,
            #     extr_osnovanie=extr_osnovanee.value,
            #     name_osn=name.value,
            #     car=number_machine_dropdown.value,
            #     gos_number=gos_number.value,
            #     extra_car=extra_car.value,
            #     name_driver=driver_dropdown.value,
            #     extra_name_driver=extra_driver.value,
            #     where=where_dropdown.value,
            #     extra_where=extra_where.value,
            #     why=names_nach.value,
            #     exstra_why=extra_names_nach.value,
            #     today=datetime.datetime.now().strftime("%d.%m%.%Y"),
            #     time=datetime.datetime.today().time().strftime("%H:%M")
            # )
            dlg = ft.AlertDialog(
                title=ft.Text(f"Материальный пропуск №{number_mp.value} создан!")
            )
            page.dialog = dlg
            dlg.open = True
            # try:
            #     create_excel.write_excel(
            #         number=number_mp.value,
            #         content=total.value,
            #         date=datetime.datetime.now().strftime("%d.%m%.%Y"),
            #         where=where_dropdown.value + extra_where.value,
            #         reason=osnovanie_dropdown.value + extr_osnovanee.value,
            #         owner=name.value
            #     )
            # except:
            #     dlg = ft.AlertDialog(
            #         title=ft.Text('Возникла ошибка при добавлении excel записи')
            #     )
            #     page.dialog = dlg
            #     dlg.open = True

            page.update()

    def refresh_values(e):
        # number_mp.value = create_excel.last_value() + 1
        total.value = ''
        osnovanie_dropdown.value = ''
        extr_osnovanee.value = ''
        name.value = ''
        number_machine_dropdown.value = ''
        extra_car.value = ''
        driver_dropdown.value = ''
        extra_driver.value = ''
        where_dropdown.value = ''
        extra_where.value = ''
        gos_number.value = ''
        extra_names_nach.value = ''
        extra_driver.visible = False
        driver_dropdown.visible = True
        number_machine_dropdown.visible = True
        extra_car.visible = False
        osnovanie_dropdown.visible = True
        extr_osnovanee.visible = False
        where_dropdown.visible = True
        extra_where.visible = False
        extra_names_nach.visible = False
        names_nach.visible = True
        page.update()

    def extr_driver(e):
        if driver_dropdown.value == ' ':
            extra_driver.visible = True
            extra_driver.autofocus = True
            driver_dropdown.visible = False
            page.update()
        else:
            return None

    def extr_car(e):
        if number_machine_dropdown.value == ' ':
            extra_car.visible = True
            extra_car.autofocus = True
            number_machine_dropdown.visible = False
            page.update()

    def extr_osn(e):
        if osnovanie_dropdown.value == ' ':
            extr_osnovanee.visible = True
            extr_osnovanee.autofocus = True
            osnovanie_dropdown.visible = False
            page.update()

    def extr_where_dropdown(e):
        if where_dropdown.value == ' ':
            extra_where.visible = True
            extra_where.autofocus = True
            where_dropdown.visible = False
            page.update()

    def extr_names_nach(e):
        if names_nach.value == ' ':
            extra_names_nach.visible = True
            extra_names_nach.autofocus = True
            names_nach.visible = False
            page.update()

    number_machine_dropdown = ft.Dropdown(
        width=300,
        label='Автомобиль',
        on_change=extr_car,
        options=[
            ft.dropdown.Option('Самовывоз'),
            ft.dropdown.Option('Avis'),
            ft.dropdown.Option('Toyota Hilux'),
            ft.dropdown.Option('Volkswagen'),
            ft.dropdown.Option('Renault Duster'),
            ft.dropdown.Option('Камаз'),
            ft.dropdown.Option('Газ'),
            ft.dropdown.Option(' ', text='Другое'),
        ]
    )

    driver_dropdown = ft.Dropdown(
        width=300,
        label='Имя водителя',
        on_change=extr_driver,
        visible=True,
        options=[
            ft.dropdown.Option('Алмаз'),
            ft.dropdown.Option('Жандос'),
            ft.dropdown.Option('Адиль'),
            ft.dropdown.Option('Avis'),
            ft.dropdown.Option(' ', text='Другое'),
        ])

    osnovanie_dropdown = ft.Dropdown(
        width=300,
        label='Основание',
        on_change=extr_osn,
        visible=True,
        options=[
            ft.dropdown.Option('ТОО КМФ Имсталькон'),
            ft.dropdown.Option('ТОО Ki-bay'),
            ft.dropdown.Option(' ', text='Другое'),
        ]
    )

    names_nach = ft.Dropdown(
        width=300,
        on_change=extr_names_nach,
        label='Подписать у:',
        options=[
            ft.dropdown.Option('Супервайзер админ. отдела: Беков А.Т.', text='Беков Ардак'),
            ft.dropdown.Option('Главный инженер: Кусаинов А.К.', text='Кусаинов Арман'),
            ft.dropdown.Option('Зам. дир. по производству: Канафин Е.Ж.', text='Канафин Еламан'),
            ft.dropdown.Option('Директор филиала: Нурахметов С.Ж.', text='Нурахметов Серик'),
            ft.dropdown.Option(' ', text='Другое'),
        ])

    where_dropdown = ft.Dropdown(
        width=300,
        label='Куда',
        on_change=extr_where_dropdown,
        options=[
            ft.dropdown.Option('г.Караганда'),
            ft.dropdown.Option('п.Бозшаколь'),
            ft.dropdown.Option('п.Шубарколь'),
            ft.dropdown.Option('г.Астана'),
            ft.dropdown.Option('г.Алматы'),
            ft.dropdown.Option(' ', text='Другое'),
        ]
    )

    number_mp = ft.TextField(label="Номер материального пропуска",)
    total = ft.TextField(label="Что вывозят")
    extr_osnovanee = ft.TextField(label="Основание", visible=False)
    name = ft.TextField(label="Имя и фамилия")
    extra_driver = ft.TextField(label='Введите имя водителя', visible=False)
    extra_car = ft.TextField(label='Введите номер машины', visible=False)
    extra_where = ft.TextField(label='Куда', visible=False)
    extra_names_nach = ft.TextField(label='Подписать У:', visible=False)
    gos_number = ft.TextField(label='Гос номер:', visible=True)

    page.add(
        ft.Column(
            controls=[
                # img,
                number_mp,
                total,
                osnovanie_dropdown, ft.Row(controls=[extr_osnovanee]),
                name,
                ft.Row(controls=[extra_car]),
                ft.Row(
                    controls=[
                        number_machine_dropdown, gos_number
                    ]
                ),
                driver_dropdown,
                ft.Row(controls=[extra_driver]),
                where_dropdown, extra_where,
                names_nach, ft.Row(controls=[extra_names_nach])
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("Создать материальный пропуск", on_click=btn_click),
                ft.ElevatedButton('Обновить', on_click=refresh_values)
            ]
        )

    )


if __name__ == '__main__':
    ft.app(target=main)
