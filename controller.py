from model import Model
from view import View
import tkinter as tk


class Controller():
    def __init__(self):
        # 1> connection database connection

        # 2> create model instance
        self.model = Model

        # 3> create view instance
        self.view = View()

        # 4> set default value

        # 5> create event handler

        # 6> run Tkinter application
        self.view.root.mainloop()
