"""
Functions required to manage servers for minecraft
"""
import subprocess
from mcipc.rcon import Client as RconClient
import socket

class Server:
    server_start_bat = None
    directory = None
    port = None
    password = None

    def __init__(self):
        hostname = socket.gethostname()
        self.ip = socket.gethostbyname_ex(hostname)
        self.ip = self.ip[0]


    def start_server(self):
        self.server = subprocess.Popen(self.server_start_bat, cwd=self.directory, shell=True, universal_newlines=True,
                                       text=True)

    def stop_server(self):
        self.run_command('stop')

    def op_user(self, user):
        self.run_command(f'op {user}')

    def clear_weather(self):
        self.run_command('weather clear 1000000')

    def rainy_weather(self):
        self.run_command('weather rain 1000000')

    def mob_griefing_on(self):
        self.run_command('gamerule mobGriefing true')

    def mob_griefing_off(self):
        self.run_command('gamerule mobGriefing false')

    def set_time_day(self):
        self.run_command('time set day')

    def set_time_night(self):
        self.run_command('time set night')

    def difficulty_peaceful(self):
        self.run_command('difficulty peaceful')

    def difficulty_easy(self):
        self.run_command('difficulty easy')

    def difficulty_normal(self):
        self.run_command('difficulty normal')

    def difficulty_hard(self):
        self.run_command('difficulty hard')

    def tp(self, user1, user2):
        with RconClient(self.ip, port) as client:
            client.login(password)
            client.teleport(player=user1, dst_player=user2)

    def run_command(self, command):
        command = str(command)
        with RconClient(self.ip, self.port) as client:
            client.login(self.password)
            client.run(command)