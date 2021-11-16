import matplotlib as mlp
import matplotlib.pyplot as plt

class Diagram:

    def __init__(self, title, xMax, yMax):
        # Label für die y-Achse vergeben:
        plt.ylabel('Quadratzahlen')

        # Einen x-y-Plot erstellen:
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')

        # Achsen-Bereiche manuell festlegen
        # Syntax: plt.axis([xmin, xmax, ymin, ymax])
        plt.axis([0, 5, 0, 20])

        # Ein gepunktetes Diagramm-Gitter einblenden:
        plt.grid(True)

        # Diagramm anzeigen:
        plt.show()