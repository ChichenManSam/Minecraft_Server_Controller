import tkinter as tk
from tkinter import font as tkfont

import Servers
import sqlite3

server = Servers.Server()

class MinecraftController(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Comic Sans MS', size=18, weight="bold", slant="italic")
        self.subtitle_font = tkfont.Font(family='Comic Sans MS', size=10, weight="bold")
        self.button_font = tkfont.Font(family='Comic Sans MS', size=10, weight='bold')
        self.title('Minecraft Controller')
        self.resizable(False, False)
        self.iconbitmap('app.ico')
        self.configure(bg='cyan3')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, NewServer, ManageServer):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        self.title(page_name)
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='cyan3')
        self.rowconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)


        title = tk.Label(self, text="Would you like to add or manage a server?", font=controller.title_font,
                         bg='cyan3', fg='gray28')
        manage_server_button = tk.Button(self, text='Manage Servers', width=60,  bg='tan2', fg='gray24',
                                         font=controller.button_font,
                                         command=lambda: controller.show_frame('ManageServer'))
        new_server_button = tk.Button(self, text="Create new server", width=60, bg='tan2', fg='gray24',
                                      font=controller.button_font, command=lambda: controller.show_frame('NewServer'))
        close = tk.Button(self, text='EXIT', width=60, bg='red', fg='white', font=controller.button_font,
                          command=self.quit)

        title.grid(row=0, columnspan=2, padx=5, pady=10)
        manage_server_button.grid(row=1, columnspan=2, padx=5, pady=10)
        new_server_button.grid(row=2, columnspan=2, padx=5, pady=10)
        close.grid(row=3, columnspan=2, padx=5, pady=10)


class NewServer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='cyan3')
        self.rowconfigure(0, weight=1)
        self.rowconfigure(6, weight=1)

        title = tk.Label(self, text='Add a New Server to Manage', font=controller.title_font,
                         bg='cyan3', fg='gray28')
        name = tk.Label(self, text='Enter Name for Server', font=controller.subtitle_font, bg='cyan3', fg='gray28')
        name_box = tk.Entry(self, width=30, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        server_bat = tk.Label(self, text='Enter the Path and serverstart.bat', font=controller.subtitle_font,
                              bg='cyan3', fg='gray28')
        server_bat_box = tk.Entry(self, width=30, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        server_directory = tk.Label(self, text='Enter the Path to Server Directory', font=controller.subtitle_font,
                                    bg='cyan3', fg='gray28')
        server_directory_box = tk.Entry(self, width=30, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        server_port = tk.Label(self, text='Enter the Minecraft Rcon Port Number', font=controller.subtitle_font,
                               bg='cyan3', fg='gray28')
        server_port_box = tk.Entry(self, width=30, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        server_password = tk.Label(self, text='Enter the Password for Rcon', font=controller.subtitle_font,
                                   bg='cyan3', fg='gray28')
        server_password_box = tk.Entry(self, width=30, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        add_button = tk.Button(self, width=30, text='Add Server', font=controller.button_font, bg='tan2', fg='gray24',
                               command=lambda: add_server((name_box.get(), server_bat_box.get(), server_directory_box.get(),
                                                           int(server_port_box.get()), server_password_box.get())))
        back_button = tk.Button(self, width=30, text='Main Menu', font=controller.button_font, bg='tan2', fg='gray24',
                                command=lambda: controller.show_frame('MainMenu'))
        status = tk.Label(self, text='', font=controller.subtitle_font,
                          bg='cyan3', fg='gray28')

        def add_server(server):
            conn = sqlite3.connect('Servers.db')
            with conn:
                sql = '''INSERT INTO server(name,server_start_bat,server_directory,port,password) VALUES(?,?,?,?,?)'''
                cur = conn.cursor()
                cur.execute(sql, server)
            status.configure(text='Server added Successfully')

        title.grid(row=0, columnspan=2, padx=10, pady=10)
        name.grid(row=1, column=0, padx=10, pady=10)
        name_box.grid(row=1, column=1, padx=5, pady=10)
        server_bat.grid(row=2, column=0, padx=5, pady=10)
        server_bat_box.grid(row=2, column=1, padx=5, pady=10)
        server_directory.grid(row=3, column=0, padx=5, pady=10)
        server_directory_box.grid(row=3, column=1, padx=5, pady=10)
        server_port.grid(row=4, column=0, padx=5, pady=10)
        server_port_box.grid(row=4, column=1, padx=5, pady=10)
        server_password.grid(row=5, column=0, padx=5, pady=10)
        server_password_box.grid(row=5, column=1, padx=5, pady=10)
        add_button.grid(row=6, column=0, padx=5, pady=10)
        back_button.grid(row=6, column=1, padx=5, pady=10)
        status.grid(row=7, columnspan=2, padx=5, pady=5)


class ManageServer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='cyan3')
        server = Servers.Server()

        def fetch_options():
            option_list = []
            conn = sqlite3.connect('Servers.db')
            cur = conn.cursor()
            cur.execute("SELECT name FROM server")
            rows = cur.fetchall()
            for row in rows:
                row = ''.join(row)
                option_list.append(row)
            return option_list

        def remove_server(server_name):
            conn = sqlite3.connect('Servers.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM server WHERE name = ?", (server_name,))
            conn.commit()

        def refresh_options():
            variable.set('Select a Server')
            option['menu'].delete(0, 'end')
            new_options = fetch_options()
            for item in new_options:
                option['menu'].add_command(label=item, command=tk._setit(variable, item))

        def start_server(server_name):
            conn = sqlite3.connect('Servers.db')
            cur = conn.cursor()
            cur.execute("SELECT server_start_bat FROM server WHERE name = ?", (server_name,))
            server_start_bat = cur.fetchall()
            server_start_bat = str(server_start_bat)
            server_start_bat = server_start_bat.strip("[(',)]")

            cur.execute("SELECT server_directory FROM server WHERE name = ?", (server_name,))
            server_directory = cur.fetchall()
            server_directory = str(server_directory)
            server_directory = server_directory.strip("[(',)]")

            global server
            server.server_start_bat = server_start_bat
            server.directory = server_directory
            server.start_server()

        def set_port_and_password(server_name):
            conn = sqlite3.connect('Servers.db')
            cur = conn.cursor()

            cur.execute("SELECT port FROM server WHERE name = ?", (server_name,))
            server_port = cur.fetchall()
            server_port = str(server_port)
            server_port = server_port.strip("[(',)]")
            server_port = int(server_port)

            cur.execute("SELECT password FROM server WHERE name = ?", (server_name,))
            password = cur.fetchall()
            password = str(password)
            password = password.strip("[(',)]")

            return server_port, password

        def stop():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.stop_server()

        def run_command():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.run_command(command_box.get())

        def set_day():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.set_time_day()

        def set_night():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.set_time_night()

        def peaceful():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.difficulty_peaceful()

        def easy():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.difficulty_easy()

        def normal():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.difficulty_normal()

        def hard():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.difficulty_hard()

        def clear():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.clear_weather()

        def rain():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.rainy_weather()

        def tp():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.tp(tp_box_1.get(), tp_box_2.get())

        def op():
            global server
            server.port, server.password = set_port_and_password(variable.get())
            server.op_user(op_box.get())


        option_list = fetch_options()
        variable = tk.StringVar(self)
        variable.set('Select a Server')
        option = tk.OptionMenu(self, variable, *option_list)
        title = tk.Label(self, text="Select a Server to Manage", font=controller.title_font, bg='cyan3',
                         fg='gray28')
        option.config(width=26, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        refresh = tk.Button(self, text='Refresh Servers', width=30, bg='tan2', fg='gray24',
                            font=controller.button_font, command=refresh_options)
        delete_server = tk.Button(self, text='Delete Server', width=30, bg='tan2', fg='gray24',
                                  font=controller.button_font, command=lambda: remove_server(variable.get()))
        start = tk.Button(self, text='Start Server', width=30, font=controller.button_font, bg='tan2', fg='gray24',
                          command=lambda: start_server(variable.get()))
        stop = tk.Button(self, text='Stop Server', width=30, font=controller.button_font, bg='tan2', fg='gray24',
                          command=stop)
        command_box = tk.Entry(self, width=31, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        run_command = tk.Button(self, text='Execute Command', width=30, font=controller.button_font, bg='tan2', fg='gray24',
                          command=run_command)
        day = tk.Button(self, text='Set Time to Day', width=30, font=controller.button_font, bg='tan2', fg='gray24',
                          command=set_day)
        night = tk.Button(self, text='Set Time to night', width=30, font=controller.button_font, bg='tan2', fg='gray24',
                          command=set_night)
        peaceful = tk.Button(self, text='Peaceful', width=12, font=controller.button_font, bg='tan2', fg='gray24',
                             command=peaceful)
        easy = tk.Button(self, text='Easy', width=12, font=controller.button_font, bg='tan2', fg='gray24',
                             command=easy)
        normal = tk.Button(self, text='Normal', width=12, font=controller.button_font, bg='tan2', fg='gray24',
                             command=normal)
        hard = tk.Button(self, text='Hard', width=12, font=controller.button_font, bg='tan2', fg='gray24',
                             command=hard)
        clear = tk.Button(self, text='Clear Weather', width=30, font=controller.button_font, bg='tan2', fg='gray24',
                          command=clear)
        rain = tk.Button(self, text='Rainy Weather', width=30, font=controller.button_font, bg='tan2', fg='gray24',
                         command=rain)
        tp_box_1 = tk.Entry(self, width=16, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        tp_box_2 = tk.Entry(self, width=16, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        teleport = tk.Button(self, text='Teleport', width=12, font=controller.button_font, bg='tan2', fg='gray24',
                             command=tp)
        to = tk.Label(self, text="to", font=controller.subtitle_font, bg='cyan3', fg='gray28')
        op_user = tk.Button(self, text='OP User', width=30, font=controller.button_font, bg='tan2', fg='gray24',
                            command=op)
        op_box = tk.Entry(self, width=31, font=controller.button_font, bg='LightSteelBlue2', fg='gray28')
        main_menu = tk.Button(self, text='Main Menu', width=60, font=controller.button_font, bg='tan2', fg='gray24',
                            command=lambda: controller.show_frame('MainMenu'))
        title.grid(row=0, columnspan=4, padx=10, pady=10)
        option.grid(row=1, column=0, columnspan=4, padx=5, pady=10)
        refresh.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        delete_server.grid(row=2, column=2, columnspan=2, padx=5, pady=10)
        start.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        stop.grid(row=3, column=2, columnspan=2, padx=5, pady=10)
        command_box.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
        run_command.grid(row=4, column=2, columnspan=2, padx=5, pady=10)
        day.grid(row=5, column=0, columnspan=2, padx=5, pady=10)
        night.grid(row=5, column=2, columnspan=2, padx=5, pady=10)
        peaceful.grid(row=6, column=0, padx=5, pady=10)
        easy.grid(row=6, column=1, padx=5, pady=10)
        normal.grid(row=6, column=2, padx=5, pady=10)
        hard.grid(row=6, column=3, padx=5, pady=10)
        clear.grid(row=7, column=0, columnspan=2, padx=5, pady=10)
        rain.grid(row=7, column=2, columnspan=2, padx=5, pady=10)
        teleport.grid(row=8, column=0, padx=5, pady=10)
        tp_box_1.grid(row=8, column=1, padx=5, pady=10)
        to.grid(row=8, column=2, padx=5, pady=10)
        tp_box_2.grid(row=8, column=3, padx=5, pady=10)
        op_user.grid(row=9, column=0, columnspan=2, padx=5, pady=10)
        op_box.grid(row=9, column=2, columnspan=2, padx=5, pady=10)
        main_menu.grid(row=10, columnspan=4, padx=5, pady=10)


if __name__ == '__main__':
    app = MinecraftController()
    app.mainloop()
