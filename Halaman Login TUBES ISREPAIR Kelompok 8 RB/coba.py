from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

available_brands = ['Apple', 'Samsung', 'Xiaomi', 'Huawei', 'LG', 'Motorola']
available_locations = ['Home', 'Office', 'Store', 'Others']

print("Please enter your desired electronic service service options.")


#Menu
input_menu = int(input("Menu Options (1: Service, 2: Upgrade, 3: sell): "))
#merek hp
smartphone_brand = input("Brand Smartphone (Apple, Samsung, Xiaomi, Huawei, LG, Motorola) : ")
while smartphone_brand not in available_brands:
    print("Invalid input. Please choose from the following options: ", available_brands)
    smartphone_brand = input("Brand Smartphone :  ")
#Lokasi
location = input("Lokasi (Home, Office, Store, Others): ")
while location not in available_locations:
    print("Invalid input. Please choose from the following options: ", available_locations)
    location = input("Lokasi: ")
#Kerusakan
complaints = input("Kerusakan : ")
#Budget
maximum_budget = float(input("Maximum Budget: "))
#hasil
if input_menu == 1:
    print("Your smartphone service has been booked.")
elif input_menu == 2:
    print("Your smartphone upgrade has been booked.")
elif input_menu == 3:
    print("Your smartphone sell has been booked.")
else:
    print("Invalid menu option selected.")

class MyForm(BoxLayout):
    def __init__(self, **kwargs):
        super(MyForm, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.menu_label = Label(text='Menu Option: 1.Service 2.Upgrade 3.Konsul')
        self.add_widget(self.menu_label)

        self.menu_input = TextInput(multiline=False)
        self.add_widget(self.menu_input)

        self.merek_label = Label(text='Brand Smartphone (Apple, Samsung, Xiaomi, Huawei, LG, Motorola) :')
        self.add_widget(self.merek_label)

        self.merek_input = TextInput(multiline=False)
        self.add_widget(self.merek_input)

        self.lokasi_label = Label(text='Lokasi (Home, Office, Store, Others):')
        self.add_widget(self.lokasi_label)

        self.lokasi_input = TextInput(multiline=False)
        self.add_widget(self.lokasi_input)

        self.budget_label = Label(text='Maximum Budget :')
        self.add_widget(self.budget_label)

        self.budget_input = TextInput(multiline=False)
        self.add_widget(self.budget_input)

        self.submit_button = Button(text='Submit')
        self.submit_button.bind(on_press=self.submit)
        self.add_widget(self.submit_button)

    def submit(self, instance):
        menu = self.menu_input.text
        merek = self.merek_input.text
        lokasi = self.lokasi_input.text
        budget = self.budget_input.text
        print('Submitted data:',menu, merek, lokasi, budget)
        self.menu_input.text = ''
        self.merek_input.text = ''
        self.lokasi_input.text = ''
        self.budget_input.text = ''

class MyApp(App):
    def build(self):
        return MyForm()

if __name__ == '__main__':
    MyApp().run()




