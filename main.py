import os
import math
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (400, 800)

KV = '''
ScreenManager:
    SplashScreen:
    MainScreen:

<SplashScreen>:
    name: "splash"
    FitImage:
        source: "splash.png"   # ضع هنا اسم ملف الصورة
        size_hint: 1, 1

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: "vertical"
        spacing: "15dp"
        padding: "20dp"

        MDTextField:
            id: length_input
            hint_text: "Enter length (L)"
            mode: "filled"
            text_color: 0, 0, 0, 1
            hint_text_color: 0, 0, 0, 0.7
            font_size: "18sp"

        MDTextField:
            id: width_input
            hint_text: "Enter width (W)"
            mode: "filled"
            text_color: 0, 0, 0, 1
            hint_text_color: 0, 0, 0, 0.7
            font_size: "18sp"

        MDButton:
            style: "filled"
            md_bg_color: 0.6, 0.6, 0.6, 1
            on_release: root.calculate_diameter()
            MDButtonText:
                text: "Calculate equivalent circle diameter"
                text_color: 0, 0, 0, 1
                font_size: "18sp"

        MDLabel:
            id: result
            halign: "center"
            md_bg_color: 1, 1, 1, 1
            text_color: 0, 0, 0, 1
            font_size: "18sp"

        Widget:
            size_hint_y: None
            height: "2dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

        MDTextField:
            id: circle_d
            hint_text: "Enter one circle diameter"
            mode: "filled"
            text_color: 0, 0, 0, 1
            hint_text_color: 0, 0, 0, 0.7
            font_size: "18sp"

        MDButton:
            style: "filled"
            md_bg_color: 0.6, 0.6, 0.6, 1
            on_release: root.split_circle()
            MDButtonText:
                text: "Calculate two diameters"
                text_color: 0, 0, 0, 1
                font_size: "18sp"

        MDLabel:
            id: result_split
            halign: "center"
            md_bg_color: 1, 1, 1, 1
            text_color: 0, 0, 0, 1
            font_size: "18sp"

        Widget:
            size_hint_y: None
            height: "2dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

        MDTextField:
            id: reverse_d
            hint_text: "Enter circle diameter for reverse conversion"
            mode: "filled"
            text_color: 0, 0, 0, 1
            hint_text_color: 0, 0, 0, 0.7
            font_size: "18sp"

        MDButton:
            style: "filled"
            md_bg_color: 0.6, 0.6, 0.6, 1
            on_release: root.reverse_convert()
            MDButtonText:
                text: "Reverse convert (to rectangle)"
                text_color: 0, 0, 0, 1
                font_size: "18sp"

        MDLabel:
            id: result_reverse
            halign: "center"
            md_bg_color: 1, 1, 1, 1
            text_color: 0, 0, 0, 1
            font_size: "18sp"
'''

class SplashScreen(Screen):
    pass

class MainScreen(Screen):
    def calculate_diameter(self):
        try:
            L = float(self.ids.length_input.text)
            W = float(self.ids.width_input.text)
            area = L * W
            r = math.sqrt(area / math.pi)
            D = 2 * r
            self.ids.result.text = f" {D:.4f}"
        except:
            self.ids.result.text = "⚠️ Enter valid values"

    def split_circle(self):
        try:
            D = float(self.ids.circle_d.text)
            A = math.pi * (D/2)**2
            A_half = A/2
            r_small = math.sqrt(A_half / math.pi)
            d_small = 2 * r_small
            self.ids.result_split.text = f" {d_small:.4f} , {d_small:.4f}"
        except:
            self.ids.result_split.text = "⚠️ Enter valid values"

    def reverse_convert(self):
        try:
            D = float(self.ids.reverse_d.text)
            A = math.pi * (D/2)**2
            side = math.sqrt(A)
            self.ids.result_reverse.text = f"Equivalent rectangle: length ≈ {side:.4f}, width ≈ {side:.4f}"
        except:
            self.ids.result_reverse.text = "⚠️ Enter valid values"

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"

        font_file = "fonts/arial.ttf"
        if os.path.exists(font_file):
            self.font_path = font_file
        else:
            self.font_path = ""  # fallback to default font

        sm = Builder.load_string(KV)
        Clock.schedule_once(lambda dt: self.switch_to_main(sm), 3)
        return sm

    def switch_to_main(self, sm):
        sm.current = "main"

if __name__ == "__main__":
    MyApp().run()