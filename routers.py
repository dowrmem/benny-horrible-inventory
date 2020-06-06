class CiscoRouter:

    def __init__(self, model):
        # Does model begin with alphanumeric
        if not model[:2].isalpha():
            raise ValueError(f"No series specified in '{model}'")
        # Is model uppercase
        if not model[:2].isupper():
            raise ValueError(f"Model number is not uppercase in '{model}'")
        #  Is model a number
        if not (model[2:].isdigit() and int(model[2:]) <= 9999):
            raise ValueError(f"Invalid model number '{model}'")
        self._model = model

    def model(self):
        return self._model

    def series(self):
        return self._model[:2]


class RouterLine:

    def __init__(self, series):
        self._series = series

    def series(self):
        return self._series
