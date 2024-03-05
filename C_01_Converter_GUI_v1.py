from tkinter import *


class Converter:

    def __init__(self):
        button_font = ("Arial", "14", "bold")
        button_fg = "#ffffff"

        self.to_farenheit = None
        self.button_frame = None
        self.temp_error = None
        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Convertor",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and then press " \
                       "one of the buttons to convert it from centigrade " \
                       "to Fahrenheit."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       width=40, wrap=250,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )

        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text=error,
                                fg="#9C0000")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To  Celsius",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font, width=12)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheit_button = Button(self.button_frame,
                                          text="to Farenheit",
                                          bg="#009900",
                                          fg=button_fg,
                                          font=button_font, width=12)
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#006600",
                                     fg=button_fg,
                                     font=button_font, width=12)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004099",
                                        fg=button_fg,
                                        font=button_font, width=12)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)


    def check_temp(self, min_value):
        error = "Please enter a number that is more " \
                "than {}".format(min_value)

        try:
            response = float(input("Choose a number"))

            if response < min_value:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
