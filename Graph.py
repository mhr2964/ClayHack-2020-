import matplotlib.pyplot as plt
import numpy as np
from Equation import Expression
import io
import base64


class Graph:
    def __init__(self):
        self._equations = []

    def input(self, equations: list):
        self._equations = []
        for equation in equations:
            self._equations.append(str(equation))

    def plot(self):
        # Create the vectors X and Y
        x = np.array(range(10))
        for equation in self._equations:
            fn = Expression(equation, ["x"])
            y = fn(x)
            plt.plot(x, y)

        # Add X and y Label
        plt.xlabel('x axis')
        plt.ylabel('y axis')

        # Add a grid
        plt.grid(alpha=.4, linestyle='--')

        # Show the plot
        return plt

    def fig_to_base64(self, fig):
        img = io.BytesIO()
        fig.savefig(img, format='png',
                    bbox_inches='tight')
        img.seek(0)

        return base64.b64encode(img.getvalue())

    def output(self):
        fig = self.plot
        fig.savefig('my_plot.png')
        encoded = self.fig_to_base64(fig)
        my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))
        return my_html


if __name__ == '__main__':
    pass
