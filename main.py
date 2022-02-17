from email.errors import StartBoundaryNotFoundDefect
from logging import StrFormatStyle, root
from kivy.app import App
from kivy.core import text
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget, WidgetException
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
import subprocess
import time
from kivy.lang.builder import Builder
from kivy.core.window import Window
import random

class PhoneScreen(Widget):
   
    Builder.load_file("Projects/BinaryGame.kv")
    Window.size = (450, 650)
 
    def __init__(self, **kwargs):
        super(PhoneScreen, self).__init__(**kwargs)
    


    
    numbers = {
        "ote": 0,
        "sf": 0,
        "thw": 0,
        "st": 0,
        "e": 0,
        "f": 0,
        "t": 0,
        "o": 0
    }
    

    def onetwoeight(self):
        if self.ids.one_two_eight.state == "down":
            self.ids.one_two_eight.text = "1"
            ote = 128
            self.numbers["ote"] = ote
        else:
            self.ids.one_two_eight.text = "0"
            self.numbers["ote"] = 0
            
    def sixfour(self):
        if self.ids.sixty_four.state == "down":
            self.ids.sixty_four.text = "1"
            sf = 64
            self.numbers["sf"] = sf
        else: 
            self.ids.sixty_four.text = "0"
            self.numbers["sf"] = 0
    def thirty_two(self):
        if self.ids.thirty_two.state == "down":
            self.ids.thirty_two.text = "1"
            thw = 32
            self.numbers["thw"] = thw
        else: 
            self.ids.thirty_two.text = "0"
            self.numbers["thw"] = 0
            
    def sixteen(self):
        if self.ids.sixteen.state == "down":
            self.ids.sixteen.text = "1"
            st = 16
            self.numbers["st"] = st
        else:
            self.ids.sixteen.text ="0"
            self.numbers["st"] = 0
    def eight(self):
        if self.ids.eight.state == "down":
            self.ids.eight.text = "1"
            e = 8
            self.numbers["e"] = e
        else:
            self.ids.eight.text = "0"
            self.numbers["e"] = 0
    def four(self):
        if self.ids.four.state == "down":
            self.ids.four.text = "1"
            f = 4
            self.numbers["f"] = f
        else: 
            self.ids.four.text = "0"
            self.numbers["f"] = 0
    def two(self):
        if self.ids.two.state == "down":
            self.ids.two.text = "1"
            t = 2
            self.numbers["t"] = t
        else:
            self.ids.two.text = "0"
            self.numbers["t"] = 0
    def one(self):
        if self.ids.one.state == "down":
            self.ids.one.text = "1"
            o = 1
            self.numbers["o"] = o   
        else:
            self.ids.one.text = "0"
            self.numbers["o"] = 0
    
    def solve(self):
        values = [n for n in self.numbers.values()]
        self.add_no = sum(values)
        self.output()

    # Change the text of the start button text input fields 
    # to Start or Stop as well as 0 or a number respectivily.
    def startBtn_Main_Event(self):
        if self.ids.Start_Button.state == "down":
            self.ids.Start_Button.text = "Stop"
        elif self.ids.Start_Button.state == "normal":
            self.ids.Start_Button.text = "Start"
            self.ids.text_input.text = "0"
            self.ids._text_input.text = "0"

    def num_to_solve(self):
        self.solve_this_num = random.randint(1,255)
        self.ids.text_input.text = str(self.solve_this_num)
        self.startBtn_Main_Event()

        
    def output(self):
        if self.ids.Start_Button.state == "down": 
            if self.add_no == self.solve_this_num:    
                self.ids.some_text.text = "Correct [+]"
                self.answer = True
            else: 
                self.num_to_solve()
                self.ids.some_text.text = "Incorrect"
                self.answer = False
        elif self.ids.Start_Button.state == "normal":        
            self.startBtnNotClicked()
            
    def startBtnNotClicked(self):
        self.ids.some_text.text = "Please Click Start"
        self.ids.text_input.text = "0"
        self.ids._text_input.text = "0"
       
       
       #second row 
    _numbers = {
        "ote": 0,
        "sf": 0,
        "thw": 0,
        "st": 0,
        "e": 0,
        "f": 0,
        "t": 0,
        "o": 0
    }

    def _onetwoeight(self):
        if self.ids._one_two_eight.state == "down":
            self.ids._one_two_eight.text = "1"
            _ote = 128
            self._numbers["ote"] = _ote
        else:
            self.ids._one_two_eight.text = "0"
            self._numbers["ote"] = 0
            
    def _sixfour(self):
        if self.ids._sixty_four.state == "down":
            self.ids._sixty_four.text = "1"
            _sf = 64
            self._numbers["sf"] = _sf
        else: 
            self.ids._sixty_four.text = "0"
            self._numbers["sf"] = 0
    def _thirty_two(self):
        if self.ids._thirty_two.state == "down":
            self.ids._thirty_two.text = "1"
            thw = 32
            self._numbers["thw"] = thw
        else: 
            self.ids._thirty_two.text = "0"
            self._numbers["thw"] = 0
            
    def _sixteen(self):
        if self.ids._sixteen.state == "down":
            self.ids._sixteen.text = "1"
            st = 16
            self._numbers["st"] = st
        else:
            self.ids._sixteen.text ="0"
            self._numbers["st"] = 0
    def _eight(self):
        if self.ids._eight.state == "down":
            self.ids._eight.text = "1"
            e = 8
            self._numbers["e"] = e
        else:
            self.ids._eight.text = "0"
            self._numbers["e"] = 0
    def _four(self):
        if self.ids._four.state == "down":
            self.ids._four.text = "1"
            f = 4
            self._numbers["f"] = f
        else: 
            self.ids._four.text = "0"
            self._numbers["f"] = 0
    def _two(self):
        if self.ids._two.state == "down":
            self.ids._two.text = "1"
            t = 2
            self._numbers["t"] = t
        else:
            self.ids._two.text = "0"
            self._numbers["t"] = 0
    def _one(self):
        if self.ids._one.state == "down":
            self.ids._one.text = "1"
            o = 1
            self._numbers["o"] = o   
        else:
            self.ids._one.text = "0"
            self._numbers["o"] = 0
            
    #solve the bits
    def _solve(self):
        _values = [n for n in self._numbers.values()]
        self._add_no = sum(_values)
        self._output()
        
    def _num_to_solve(self):
        self.num_to_solve()
        self._solve_this_num = random.randint(1,255)
        self.ids._text_input.text = str(self._solve_this_num)
        self.startBtn_Main_Event()
    
    # Reason for the duplication: This is to prevent the 
    # 2nd row add button from changing the value of the 
    # first row input text field.
    def secondRow_text_fieldRestart(self):
        self._solve_this_num = random.randint(1,255)
        self.ids._text_input.text = str(self._solve_this_num)
        self.startBtn_Main_Event()
    
    def _output(self):
        if self.ids.Start_Button.state == "down": 
            if self._add_no == self._solve_this_num:    
                self.ids.some_text.text = "Correct [++]"
                self._answer = True
            else:
                self.ids._text_input.background_color = (1,0,0,1) # remove this and instead make the text input red to indicate incorrect answer
                self.secondRow_text_fieldRestart()
                time.sleep(2)
                self.ids._text_input.background_color = (0,0,0,1 )
                self._answer = False
        elif self.ids.Start_Button.state == "normal":
            self.startBtnNotClicked()

    def game_checker(self):
        if self._answer and self.answer  == True:
            self.some_text.text = "Congratulations"
        else: 
            self.some_text.text = "Check your answers"

class BinaryGame(App):
    def build(self):
        return PhoneScreen()


if __name__ == '__main__':
    BinaryGame().run() 