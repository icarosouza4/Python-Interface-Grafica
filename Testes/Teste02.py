# Teste 2

from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img = AsyncImage(source = "https://i.pinimg.com/1200x/e8/67/d7/e867d7379f584fac79fa89946e2b7857.jpg",
            size_hint = (1, 1),
            pos_hint = {"center_x":.5, "center_y":.5})
        return img

if __name__ == "__main__":
    app = MainApp()
    app.run()
    