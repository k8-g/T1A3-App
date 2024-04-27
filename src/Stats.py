import os

class Stats:
    def __init__(self, _player_name):
        self._wins = 0
        self._losses = 0
        self._player_name = _player_name
        self._file_name = "stats.csv"

    # getter to get wins
    def get_wins(self):
        return self._wins
    
    # getter to get losses
    def get_losses(self):
        return self._losses
    
    # counting wins
    def add_win(self):
        self._wins += 1

    # counting losses
    def add_loss(self):
        self._losses += 1

    # save stats
    def save_stats(self):
        print("Save Stats")
        stat_file = open(self._file_name, "w")
        stat_file.write(self._wins + "," + self._losses)
        stat_file.close()

    # load stats
    def load_stats(self):
        print("load stats")
        if os.path.isfile(self._file_name):
            stat_file = open(self._file_name, "r")
            stats = stat_file.read()
            stats = stats.split(",")
            self._wins = int(stats [0])
            self._losses = int(stats [1])
            stat_file.close()