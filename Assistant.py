'''
Author:
Jacob Gonzalez
Contributers:
Sam Lewis
Jake Lane
'''

import sublime, sublime_plugin

'''
header files will be to the right/bottom
source files will be to the left/top
'''

class AssistantListener(sublime_plugin.EventListener):
    '''EventListener class for events'''

    def __init__(self):
        self.layouts = ['2 columns', '2 rows']
        self.current = '2 columns'
        sublime.active_window().show_quick_panel(self.layouts, self.on_done)

    def on_done(self, index):
        self.current = self.layouts[index]

    def layout_panes(self, layout, view):
        #cols
        if layout == self.layouts[0]:
            view.window().set_layout({"cols": [0, 0.5, 1], "rows": [0, 1], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]})
        #rows
        elif layout == self.layouts[1]:
            view.window().set_layout({"cols": [0 ,1], "rows": [0, 0.5, 1], "cells": [[0, 0, 1, 1], [0, 1, 1, 2]]})
            
    def on_activated(self, view):
        file_name = view.file_name()
        # custom layout name

        if file_name != None:
            # source file, move header to right, source to left
            if file_name.endswith(".cpp"):
                header = view.window().find_open_file(file_name.replace('.cpp', '.h'))
                if header != None:
                    self.layout_panes(self.current, view)
                    view.window().set_view_index(header, 1, 0)
                    view.window().set_view_index(view, 0, view.window().get_view_index(view)[1])

            # header file, move header to right, source to left
            if file_name.endswith(".h"):
                source = view.window().find_open_file(file_name.replace('.h', '.cpp'))
                if source != None:
                    self.layout_panes(self.current, view)
                    view.window().set_view_index(source, 0, 0)
                    view.window().set_view_index(view, 1, view.window().get_view_index(view)[1])
