import pickle
import os


class Handler:
    @staticmethod
    def rootInstance():
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/root.dat'):
            data = []
            with open('data/root.dat', 'wb') as file:
                pickle.dump(data, file)
            return []
        with open('data/root.dat', 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def rootUpdate(databases):
        file = open('data/root.dat', 'wb')
        pickle.dump(databases, file)
        file.close()
        return databases

    @staticmethod
    def leerArchivoDB() -> list:
        try:
            if os.path.getsize('databases') > 0:
                with open('databases', 'rb') as f:
                    return pickle.load(f)
            return []
        except:
            f = open("databases", 'wb')
            f.close()
