import matplotlib.pyplot as plt
import numpy as np
from Equation import Expression
import io
import base64


class Graph:
    def input(self, equations: list):
        # Create the vectors X and Y
        x = np.array(range(10))
        for equation in equations:
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


if __name__ == '__main__':
    graph = Graph()
    fig = graph.input(["x**2"])
    fig.savefig('my_plot.png')
    encoded = graph.fig_to_base64(fig)
    my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))
