from tkinter import *
from collections import namedtuple
from obx_web_scraping import *
from obx_math_functions import *

obx_location_object = namedtuple('obx_location_object', ['name', 'temperature', 'wave_height'])

class obx_window():
    def __init__(self):
        self.window = Tk()
        self.window.title('OBX')
        self.window.resizable(False, False)
        self.slider_variable = IntVar()
        self.report_variable = StringVar()
        self.ideal_weather_variable = StringVar()
        self.create_window()
        self.window.update()
        self.height_surf = get_obx_list(get_height_surf())
        self.location_objects = [obx_location_object(location[0], location[1], location[2]) for location in self.height_surf]
        self.running = True
        while self.running:
            self.window.update()
            self.obx_update(rank(get_temperature_list(self.get_ideal_weather_variable(), self.location_objects), get_wave_list(self.location_objects), self.slider_variable.get()))
            self.window.protocol("WM_DELETE_WINDOW", self.stop_program)
        self.window.destroy()
        self.window.mainloop()

    def get_ideal_weather_variable(self):
        try:
            if not self.ideal_weather_variable.get() == '':
                int(self.ideal_weather_variable.get())
        except ValueError:
            self.ideal_weather_variable.set('0')
            return 0
        except TypeError:
            self.ideal_weather_variable.set('0')
            return 0
        else:
            if self.ideal_weather_variable.get() == '':
                return 0
            else:
                return int(self.ideal_weather_variable.get())

    def stop_program(self):
        self.running = False

    def create_window(self):
        Label(self.window, width=27, height=20, relief=SUNKEN, background='white', textvariable=self.report_variable, anchor=NW, justify=LEFT, wraplength=200).grid(row=0, column=0, columnspan=3, pady=2)

        Entry(self.window, width=5, textvariable=self.ideal_weather_variable).grid(row=1, column=2)

        Label(self.window, text='Weather ').grid(row=2, column=0)
        Label(self.window, text=' Waves').grid(row=2, column=2)
        Label(self.window, text='Ideal Temperature (%cF):           ' % chr(186)).grid(row=1, column=0, columnspan=2)
        Scale(self.window, from_=0, to=100, showvalue=0, orient=HORIZONTAL, sliderlength=20, resolution=25, variable=self.slider_variable).grid(row=2, column=1)

        self.ideal_weather_variable.set('0')
        self.report_variable.set('Fetching report data...')

    def obx_update(self, obx_master_list):
        set_string = ''
        for cur_loc in range(4):
            set_string += self.get_obx_list_object_string(obx_master_list[cur_loc], cur_loc)
            for _ in range(38):
                set_string += '_'
            set_string += '\n'
        self.report_variable.set(set_string)

    def get_obx_list_object_string(self, obx_list_object, rank):
        r_string = ''
        r_string += 'Rank: %s\n' % str(rank + 1)
        r_string += 'Name: %s\n' % obx_list_object[0]
        r_string += 'Temperature: %s%cF\n' % (str(obx_list_object[1]), 186)
        r_string += 'Wave Height: %sft\n' % str(obx_list_object[2])
        return r_string