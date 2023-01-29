import csv
import flet as ft
from movie_class import Movie


WELCOME = "Welcome to KinoPaís! \nThe best place to find global movies! \nPlease choose one of the countries below and revieve a list of the top ten movies from that country!\n"
COUNTS = ["Africa", "Balkans", "Benelux", "Central America", "Canada", "Germany", "Greater China", "Iberia", "India", "Italy", "Japan", "Korea", "Mexico", "Middle East", "Russia", "Scandinavia", "South America", "United Kingdom", "United States"]

COUNTRIES = ''
COUNTS = sorted(COUNTS)
for x in COUNTS:
  if x == COUNTS[len(COUNTS)-1]:
    COUNTRIES = COUNTRIES + x + '.'
  else:
    COUNTRIES = COUNTRIES + x + ', '

for x in range(len(COUNTS)):
  COUNTS[x] = COUNTS[x].lower()
  


def main(page: ft.Page):
  global count
  count = 0
  page.horizontal_alignment = 'center'
  def btn_click(e):
    global count
    if not txt_country.value:
        txt_country.error_text = "Please enter a country"
        page.update()
    elif txt_country.value.lower() not in COUNTS:
        txt_country.error_text = "Invalid Entry. Please Try Again"
        page.update()
    else:
        #this is where we take the users input
        if count != 0:
          try:
            page.controls.pop(5)
          except:
            pass

        count = 1 

        csv_filename = txt_country.value

        movie_list = []

        fp = open(csv_filename + ".csv", mode="r", encoding='latin 1')
        fp.readline()

        for line in fp:
          line = line.strip().split(',$,')
          film_title = line[0]
          release_year = int(line[1])
          director = line[2]
          cast = list(line[3])
          personal_rating = line[4]
          average_rating = float(line[5])
          url = line[6]
        
          movie_list.append(Movie(film_title, release_year, director, cast, personal_rating, average_rating, url))
        
        
      
        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        #this is where we add the algorithms output
        for i in range(10):
          lv.controls.append(ft.Text(f"{movie_list[i]}",text_align='center'))
        page.add(lv)

            


  title =  ft.Row([ft.Text('KinoPaís', style=ft.TextThemeStyle.DISPLAY_LARGE)],alignment=ft.MainAxisAlignment.CENTER, wrap=True)
  welcome = ft.Row([ft.Text(WELCOME, style=ft.TextThemeStyle.TITLE_SMALL, text_align='center')],alignment=ft.MainAxisAlignment.CENTER, wrap=True)
  instructions = ft.Row([ft.Text(COUNTRIES, style=ft.TextThemeStyle.TITLE_SMALL, text_align='center')],alignment=ft.MainAxisAlignment.CENTER, wrap=True)

  txt_country = ft.TextField(label="Country")

  page.add(title, welcome, instructions,
  txt_country, ft.Row([ft.ElevatedButton("GO!", icon="MOVIE", bgcolor='BLACK', on_click=btn_click)], alignment=ft.MainAxisAlignment.CENTER))

  
if __name__ == "__main__":
    ft.app(target=main)

