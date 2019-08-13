from tkinter import *
from collections import namedtuple

obx_location_object = namedtuple('obx_location_object', ('name, temperature, wave_height'))

class obx_window():
    def __init__(self):
        self.window = Tk()
        self.window.title('OBX')
        self.window.resizable(False, False)
        self.slider_variable = IntVar()
        self.report_variable = StringVar()
        self.ideal_weather_variable = StringVar()
        self.create_window()
        self.running = True
        while self.running:
            self.window.update()
            self.obx_update()
            self.window.protocol("WM_DELETE_WINDOW", self.stop_program)
        self.window.destroy()
        self.window.mainloop()

    def stop_program(self):
        self.running = False

    def create_window(self):
        report_text = Label(self.window, width=27, height=20, relief=SUNKEN, background='white', textvariable=self.report_variable, anchor=NW, justify=LEFT, wraplength=200).grid(row=0, column=0, columnspan=3, pady=2)

        ideal_weather_entry = Entry(self.window, width=5, textvariable=self.ideal_weather_variable).grid(row=1, column=2)

        weather_label = Label(self.window, text='Weather ').grid(row=2, column=0)
        waves_label = Label(self.window, text=' Waves').grid(row=2, column=2)
        ideal_weather_label = Label(self.window, text='Ideal Temperature (%cF):           ' % chr(186)).grid(row=1, column=0, columnspan=2)
        obx_slider = Scale(self.window, from_=0, to=100, showvalue=0, orient=HORIZONTAL, sliderlength=20, resolution=25, variable=self.slider_variable).grid(row=2, column=1)

    def obx_update(self):
        locations = [obx_location_object('lmao', self.ideal_weather_variable.get(), i) for i in range(int(self.slider_variable.get()/25))]
        report_string = ''
        for location in locations:
            report_string += self.get_obx_list_object(location.name, location.temperature, location.wave_height, 1)
            for i in range(38):
                report_string += '_'
            report_string += '\n'
        self.report_variable.set(report_string)

    def get_obx_list_object(self, name, temp, wave_height, rank):
        r_string = ''
        r_string += 'Rank: %s\n' % str(rank)
        r_string += 'Name: %s\n' % name
        r_string += 'Temperature: %s%cF\n' % (str(temp), 186)
        r_string += 'Wave Height: %sft\n' % str(wave_height)
        return r_string

my_window = obx_window()