import json
from os import walk
from tfstate_classes.tfstate_input import abstract_tfstate


class terraform_states(abstract_tfstate):

    def __init__(self, path_input: str):
        super(terraform_states, self).__init__(path_input)

    def _get(self):
        f = []
        dirpath, _, filenames = next(walk(self.path_input))
        for index, filename in enumerate(filenames):
            with open(f"{dirpath}/{filename}") as file:
                content = json.load(file)
                content["graph_index"] = index
                self.tfstates[filename] = content
                self.mapping[index] = filename
                self.filename = filename

