import pandas

DATA_FILE = 'data/french_words.csv'
SAVE_FILE = 'data/words_to_learn.csv'


class SaveFileNotFoundError(Exception):
    """Raised when the save file has not been created yet"""
    pass


class FlashyModel:
    def __init__(self):
        self.dataframe = None
        self.load_words()

    def load_from_save(self):
        try:
            self.dataframe = pandas.read_csv(SAVE_FILE)
        except FileNotFoundError:
            raise SaveFileNotFoundError

    def load_initial_data(self):
        try:
            self.dataframe = pandas.read_csv(DATA_FILE)
        except FileNotFoundError:
            print('Error: Initial data file does not exists')
            exit(0)

    def load_words(self):
        try:
            self.load_from_save()
        except SaveFileNotFoundError:
            self.load_initial_data()

    def get_words(self):
        return self.dataframe.to_dict(orient="records")

    def delete(self, word):
        index = self.dataframe[self.dataframe['French'] == word['French']].index
        self.dataframe.drop(index, inplace=True)
        self.dataframe.to_csv(SAVE_FILE, index=False)
