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
            self._equations.append(str(equation).replace(" ", "").replace("y=", "").replace("f(x)=", ""))

    def plot(self, upper_left_coord: tuple, lower_right_coord: tuple):
        # Create the vectors X and Y
        x = np.array(range(lower_right_coord[0]-upper_left_coord[0]))
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

    def output(self, upper_left_coord: tuple, lower_right_coord: tuple):
        """
        plots the graph and places it in a .png file for the HTML code to show
        outputs the image in an HTML statement that is the image
        :param upper_left_coord: (tuple) the upper right coordinate point
        :param lower_right_coord: (tuple) the lower right coordinate point
        :return: an HTML image statement
        """
        # gets the graph
        fig = self.plot(upper_left_coord, lower_right_coord)

        # saves the graph as a .png
        fig.savefig('my_plot.png')

        # encodes and outputs the image as an HTML statement
        encoded = self.fig_to_base64(fig)
        my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))
        return my_html


if __name__ == '__main__':
    graph = Graph()
    graph.input(["y=sin(x)"])
    print(graph.output((0, 10), (20, -10)))
