from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.app import App

# Aqui você define a GUI usando Kivy Language
KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    Label:
        text: 'Titulo do produto:'
    TextInput:
        id: produto
        hint_text: 'Digite o titulo do produto...'
    
    Label:
        text: 'Quantidade'
    TextInput:
        id: quantidade
        hint_text: 'Digite a quantidade do produto'
    
    Button:
        text: 'CADASTRAR'
        on_release: app.add_new_product()

    ScrollView:
        size_hint: (1, None)
        height: 400
        BoxLayout:
            id: lista_produtos
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: 10
'''

class MainApp(App):
    def build(self):
        self.title = 'Lista de compras'
        return Builder.load_string(KV)

    def add_new_product(self):
        produto = self.root.ids.produto.text
        quantidade = self.root.ids.quantidade.text
        if produto and quantidade:
            self.root.ids.lista_produtos.add_widget(
                Label(text=f'{produto} - {quantidade}')
            )
            self.root.ids.produto.text = ''
            self.root.ids.quantidade.text = ''
        else:
            popup = Popup(
                title='Erro',
                content=Label(text='Por favor, preencha todos os campos.'),
                size_hint=(0.8, 0.2)
            )
            popup.open()

if __name__ == '__main__':
    MainApp().run()
