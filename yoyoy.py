from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast


kv='''
#: import Factory kivy.factory.Factory

<ContentNavigationDrawer@BoxLayout>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height
        FitImage:
            id: avatar

            source:"C:/Users/LUCKY/Pictures/Screenshots/download.jfif"
    MDLabel:
        text: "MUSIC PLAYER"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
    MDLabel:
        text: "Developed using kivy"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:"vertical"
                    MDToolbar:
                        title:"Navigation box"
                        left_action_items: [['menu', lambda x: navigat.set_state("open")]]
                    Widget:
                    Screen:
                        MDBottomNavigation:
                            text_color_normal:(255/255.0, 238/255.0, 0,1)
                            text_color_active:(0, 1, 0,1)
                            MDBottomNavigationItem:
                                name:"PLAYLIST"
                                text:"PLAY SONGS"
                                icon:"music-box"
                                theme_text_color:"Custom"
                                text_color:(1,0,0,1)
                                ScrollView
                                    MDList:
                                        id:list1
                                MDFloatingActionButton:
                                    pos_hint:{"x":0.9,"bottom":1}
                                    icon:"language-python"
                                    theme_text_color: "Custom"
                                    text_color: (0,0,0,1)
                                    elevation:20
                                    md_bg_color:(1,0,0,1)
                            MDBottomNavigationItem:
                                name:"FAVOURITES"
                                text:"Favourites"
                                icon:"heart"
                                ScrollView:
                                    MDList:
                                        id:list2
                                MDFloatingActionButton:
                                    pos_hint:{"x":0.9,"bottom":1}
                                    icon:"language-python"
                                    theme_text_color: "Custom"
                                    text_color: (0,0,0,1)
                                    elevation:20
                                    md_bg_color:(1,0,0,1)

        MDNavigationDrawer:
            id:navigat
            ContentNavigationDrawer:
                ScrollView:
                    MDList:
                        spacing:"20dp"
                        MDRectangleFlatIconButton:
                            id:nigga
                            on_press:app.lol()
                            text:"ADD MUSIC"
                            size_hint_x:0.9
                            icon:"music"
                        MDRectangleFlatIconButton:
                            id:lol
                            size_hint_x:0.9
                            text:"REMOVE MUSIC"

                            icon:"music-off"
                        MDRectangleFlatIconButton:
                            text:"CLEAR MUSIC"
                            size_hint_x:0.9
                            icon:"playlist-music"
                        MDRectangleFlatIconButton:
                            text:"THEME"
                            size_hint_x:0.9
                            icon:"moon-last-quarter"
                        MDRectangleFlatIconButton:
                            text:"ABOUT"
                            size_hint_x:0.9
                            icon:"information"

'''
class ContentNavigationDrawer(BoxLayout):
    pass
class TestNavigationDrawer(MDApp):
    def build(self):
        self.file=False
        self.screen= Builder.load_string(kv)
        self.theme_cls.theme_style="Dark"
        self.manger_open=False
        self.manger=MDFileManager(
            icon="android",
            preview=False,
            exit_manager=self.exit,
            select_path=self.path,
            show_hidden_files=False,
            ext=[".mp3"]
        )
        return self.screen
    def lol(self,*args):
        self.manger.show("/")
        self.manger_open=True
    def path(self,pathfile):
        self.exit()
        toast(pathfile)
        a="\a"
        self.file="C:"+str(pathfile).replace(str("\\"),"/")

        print(self.file)
    def exit(self,*args):
        self.manger.close()
        self.manger_open=False

TestNavigationDrawer().run()