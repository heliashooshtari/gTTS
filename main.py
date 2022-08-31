from kivymd.app import MDApp
from kivy.lang import Builder
import gtts
from playsound import playsound
from kivy.core.window import Window
#import mdlistitem
from kivymd.uix.list import OneLineIconListItem
Window.size = (360, 640)
text = """
MDGridLayout:
    cols: 1
    rows: 2
    ScrollView:
        #like a message bubble
        MDList:
            id: list
            
    MDBoxLayout:
        cols: 2
        rows: 1
        size_hint_y: None
        height: self.minimum_height
        padding: dp(10)
        spacing: dp(10)
        MDTextField:
            hint_text: "Your text here"
            id: text_field
            multiline: True
            on_text_validate: app.on_text_validate(self.text)
        MDRaisedButton:
            text: "Speak"
            on_release: app.speak()
"""


class MYAPP(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "500"
        self.title = "Text to Speech"
        return Builder.load_string(text)

    def speak(self):
        print(self.root.ids.text_field.text)
        tts = gtts.gTTS(text=self.root.ids.text_field.text,
                        lang='en', slow=False)
        self.root.ids.list.add_widget(
            OneLineIconListItem(text=self.root.ids.text_field.text))
        self.root.ids.text_field.text = ""
        tts.save("temp.mp3")
        playsound("temp.mp3")


if __name__ == "__main__":
    MYAPP().run()
