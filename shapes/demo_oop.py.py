import sys
import json
import turtle
import os
import yaml

from figures.base import Figure
from figures.simple import Circle, Square, Rectangle, NSide, Pie

FIGURE_TYPES = {
    "circle": Circle,
    "square": Square,
    "rectangle": Rectangle,
    "nside": NSide,
    "pie": Pie,

}


class Loader:
    def __init__(self, filename):
        # base validations
        if os.access(filename, os.R_OK) and os.path.isfile(filename):
            self.filename = filename
        else:
            raise ValueError("Inaccessible file '{}'".format(filename))

    def load(self):
        raise NotImplementedError()


class JSONLoader(Loader):

    def load(self):
        with open(self.filename) as f:
            input_data = json.load(f)
            return input_data


class YAMLLoader(Loader):

    def load(self):
        with open(self.filename) as f:
            input_data = yaml.load(f)
            return input_data


def main():
    if len(sys.argv) < 2:
        print("Usage: {} input-file.json".format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        figures = create_figures(input_data)
        draw_figures(figures)
    except Exception as e:
        print("Invalid input file provided! Error: " + str(e))
        return 2


def load_input_data(input_filename):
    # os.path.splitext връща tuple с 2 стойности - име и разширение на файла
    filename, extension = os.path.splitext(input_filename)
    loader = None
    if extension == '.json':
        loader = JSONLoader(input_filename)
    elif extension == '.yaml':
        loader = YAMLLoader(input_filename)# ... тук по същия начин ще се добави обработване на YAML файлове


    if loader is not None:
        return loader.load()
    else:
        raise ValueError("Unsupported file format: {}".format(extension))


def create_figures(input_data: dict):
    result = []
    for f_info in input_data:
        figure_type = f_info['type']
        if figure_type in FIGURE_TYPES:
            figure_class = FIGURE_TYPES[figure_type]
            result.append(figure_class(**f_info))
        else:
            raise ValueError("Unsupported figure")
    return result


def draw_figures(figures):
    for figure in figures:
        t = turtle.Turtle()
        t.speed('slow')
        figure.draw(t)
    turtle.exitonclick()

if __name__ == "__main__":
    sys.exit(main())