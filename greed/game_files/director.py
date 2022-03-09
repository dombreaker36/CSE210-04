from game_files.services.video_control import VideoServices
from game_files.services.input_manager import KeyboardServices
import csv
# from defaults import default_parameters

class Director:

    def __init__(self):
        window = VideoServices
        player_1_controller = KeyboardServices
        pass

    def start_game():
        defs_dict = {}
        with open("greed/game_files/defaults/default_parameters.csv") as file:
            reader = csv.DictReader(file)
            for line in reader:
                print(line)
        print(defs_dict)
        print("game started")

    def end_game():
        print("game ended")


        