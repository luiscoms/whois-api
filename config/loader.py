import varyaml


class Loader:

    def load_from_file(self, file):
        with open(file, 'r') as f:
            return varyaml.load(f)
