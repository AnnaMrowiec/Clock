import tkinter as tk
from datetime import datetime
from pytz import timezone                                                 # do wykorzystania jesli postanowimy wyświetlić czas z innej strefy czasowej

def display_time():
    current_time = datetime.now(timezone('US/Eastern')).strftime('\n \n %A %d %Y %H:%M:%S')
    clock_name = 'Current time in New York:'
    clock_label['text'] = clock_name + current_time
    my_window.after(1000, display_time)                                     #to określa liczbę milisekund do ponownego uruchomienia funkcji. Zamiast pętli



my_window = tk.Tk()                                                         # To nam tworzy zasadnicze okno, w którym bedzie wyświetlać sie zegar
my_window.title('Digital Clock')                                            # Tutaj określamy tytuł naszego okna
my_window.configure(background='white')                                     # dzięki ustaleniu tego samego koloru po rozciągnięciu okna całe tło będzie jednolitego koloru
clock_name = tk.Label(my_window, font='arial 30', bg='white', fg='black')
clock_name.grid(row=0, column=0)
clock_label = tk.Label(my_window, font='arial 30', bg='white', fg='black')  # Tu zaś mamy określną kolorystykę wypełnienia
clock_label.grid(row=0, column=0)
display_time()                                                              # polecenie wcześniej napisanej funkcji określa nam obecny czas do wyświetlenia

my_window.mainloop()                                                        # to polecenie wyświetla wszystko określone powyżej