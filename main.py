
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class CalculatorForm(BoxLayout):
    text_input = ObjectProperty()
    start = False

    def pressed(self, text):
        try:
            if text == 'C':
                self.text_input.text = '0'
                self.start = False
            elif text == '=':
                self.text_input.text = str(eval(self.text_input.text))
                self.start = False
            elif text == '<-':
                if len(self.text_input.text) == 1:
                    self.text_input.text = '0'
                    self.start = False
                else:
                    self.text_input.text = self.text_input.text[:len(self.text_input.text)-1]
            else:
                if not self.start:
                    self.text_input.text  = text
                    self.start = True
                else:
                    self.text_input.text += text
        except:
            self.text_input.text = 'Error'
            self.start = False

class CalculatorApp(App):
    pass

if __name__ == '__main__':
    CalculatorApp().run()