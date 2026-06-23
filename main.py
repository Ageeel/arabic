import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "تطبيقي الأول"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # متغير العداد
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100, read_only=True)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    # واجهة التطبيق
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# تشغيل التطبيق
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
