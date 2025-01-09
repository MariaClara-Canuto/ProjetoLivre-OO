import json
import os

class SaveSystem:
    def __init__(self, saveFile = 'savedGame.json'):
        self.saveFile = saveFile
        self.data = {
            'coins': 0,
            'flag': 0,
            'task1Progress': 0,
            'task2Progress': 0,
            'task3Progress': 0,
            'task4Progress': 0,
            'leng1': 0,
            'leng2': 0,
            'leng3': 0,
            'leng4': 0,
            'owned1': 0,
            'owned2': 0,
            'owned3': 0,
            'owned4': 0
        }

    def load_game(self):
        if os.path.exists(self.saveFile):
            with open(self.saveFile, 'r') as file:
                self.data = json.load(file)

        else: pass

    def save_game(self):
        with open(self.saveFile, 'w') as file:
            json.dump(self.data, file)

    def update(self, coins, flag, task1Progress, task2Progress, task3Progress, task4Progress, leng1, leng2, leng3, leng4, owned1, owned2, owned3, owned4):
        self.data['coins'] = coins
        self.data['flag'] = flag
        self.data['task1Progress'] = task1Progress
        self.data['task2Progress'] = task2Progress
        self.data['task3Progress'] = task3Progress
        self.data['task4Progress'] = task4Progress
        self.data['leng1'] = leng1
        self.data['leng2'] = leng2
        self.data['leng3'] = leng3
        self.data['leng4'] = leng4
        self.data['owned1'] = owned1
        self.data['owned2'] = owned2
        self.data['owned3'] = owned3
        self.data['owned4'] = owned4
        self.save_game()

    def get_data(self):
        return self.data