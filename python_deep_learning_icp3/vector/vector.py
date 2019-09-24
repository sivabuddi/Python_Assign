import numpy as np


class Vector:

    def generate_random(self, input_size):
        x = np.random.random_integers(1, 20, input_size)
        print(x)
        return x

    def reshape(self, array, rows, columns):
        output = array.reshape((rows, columns))
        print(output)
        return output

    def replace_maxmium(self, array, replace_value, axis):
        output = np.where(array == np.max(array, axis=1).reshape(-1, 1),0 * array,array)
        print(output)
