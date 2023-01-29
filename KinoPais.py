import flet as ft


WELCOME = "Welcome to KinoPaís! \nThe best place to find global movies! \nPlease choose one of the countries below. \n"
COUNTRIES = ["Africa", "Balkans", "Benelux", "Central America", "Canada", "France", "Germany", "Greater China", "Iberia", "India", "Italy", "Japan", "Korea", "Mexico", "Middle East", "Russia", "Scandinavia", "South America", "United Kingdom", "United States"]


def main(page):
    def btn_click(e):
        if not txt_country.value:
            txt_country.error_text = "Please enter a country"
            page.update()
        else:
            #this is where we take the users input
            pais = txt_country.value
           
            #this is where we add the algorithms output
            page.add(ft.Text(f"this is were we will output the moveis from {pais}!"))

    title =  ft.Row([ft.Text('KinoParis', style=ft.TextThemeStyle.DISPLAY_LARGE)],wrap=True)
    welcome = ft.Row([ft.Text(WELCOME, style=ft.TextThemeStyle.TITLE_SMALL)],wrap=True)
    instructions = ft.Row([ft.Text(COUNTRIES, style=ft.TextThemeStyle.TITLE_SMALL)], wrap=True,)

    txt_country = ft.TextField(label="Country")

    page.add(title, welcome, instructions,
    txt_country, ft.ElevatedButton("GO!", icon="MOVIE", bgcolor='BLACK', on_click=btn_click))


ft.app(target=main, scroll=True)