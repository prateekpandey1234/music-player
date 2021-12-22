from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.uix.behaviors import ButtonBehavior
import pygame
from kivymd.utils.fitimage import FitImage
from kivymd.uix.label import MDIcon
pygame.init()
kv='''
#: import Factory kivy.factory.Factory
<iconlabel@MDFlaotingActionButton+FitImage+MDSpinner>
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
                        md_bg_color:(247/255.0, 32/255.0, 32/255.0,1)
                        left_action_items: [['menu', lambda x: navigat.set_state("open")]]
                        
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
                                iconlabel:
                                    id:label
                                    active:False
                                    source:"C:/Users/LUCKY/Pictures/Screenshots/download.jfif"
                                    
                                    user_font_size:"62sp"
                                    pos_hint:{"center_x":0.5,"center_y":0.3}
                                    palette:[(1,0,0,1),(0,1,0,1),(0,0,1,1),(0,0,0,1),(1,1,1,1)]
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
class iconlabel(FitImage,MDSpinner,MDFloatingActionButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class listitem(OneLineIconListItem,ButtonBehavior):
    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        self.background_normal=""

        self.background_color=(0,0,0,1)
class ContentNavigationDrawer(BoxLayout):
    pass
class TestNavigationDrawer(MDApp):
    def build(self):
        self.current_song=False
        self.file=False
        self.song_playing=False
        self.l=[]
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
        self.manger.show("C:/Users/Lucky/kivymdproject/music folder/")
        self.manger_open=True
    def path(self,pathfile):
        self.exit()
        a="\a"
        self.file="C:"+str(pathfile).replace(str("\\"),"/")

        self.file=self.file[len(self.file)-1-self.file[::-1].index("/")+1:]
        widget=listitem(
            text=self.file,
            theme_text_color="Custom",
            text_color=(0,1,0,1),
            divider="Full",
        )
        widget.on_press=lambda *args:self.play(widget.text,self.song_playing)

        if widget.text in self.l:
            toast("SONG IS ALREADY ADDED")
        else:
            self.screen.ids.list1.add_widget(widget)
            for j in (self.screen.ids.list1.children):
                self.l.append(j.text)
    def exit(self,*args):
        self.manger.close()
        self.manger_open=False
    def play(self,song_name,song_play):
        if   self.current_song!=song_name :
            self.current_song = song_name
            song = "C:/Users/Lucky/kivymdproject/music folder/" + song_name
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            self.screen.ids.label.active=True
            self.song_play=True
        elif self.song_play==True and self.current_song==song_name :
            self.stop()

    def stop(self,*args):
        pygame.mixer.music.stop()
        self.song_play=False
        self.current_song = False
        self.screen.ids.label.active = False

TestNavigationDrawer().run()