from tfstate_classes.tfstate_input import abstract_tfstate


class terraform_states(abstract_tfstate):

    def __init__(self, path_input: str):
        """
        path_input: s3 bucket name
        """
        super(terraform_states, self).__init__(path_input)

    def _get(self):
        """
        Override this method to implement TFE state input
        """
        raise NotImplementedError()