import numpy as np
from random import choice
from sklearn.neural_network import MLPClassifier
from EntityNames import EntityNames
from Actions import Actions


class DefaultBehavior:
    default_model = None

    @staticmethod
    def GetModel():
        if DefaultBehavior.default_model == None:
            x = np.array([])
            for _ in range(100):
                x = np.append(x, [choice([member.value for member in EntityNames]) for _ in range(8)])
            x = x.reshape(100, 8)
            y = np.array([choice([member.value for member in Actions]) for _ in range(100)]).ravel()

            model = MLPClassifier(max_iter=1200)
            model.fit(x, y)
            DefaultBehavior.default_model = model
        return DefaultBehavior.default_model
