import abc
#библиотека для абстрактных классов и их методов

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Color:
    ALLOWED = {"red", "green", "blue", "white", "black", "pink", "purple", "grey", "none"}

    def __init__(self, *args):

        # RGB
        if len(args) == 3:
            self.red = args[0]
            self.green = args[1]
            self.blue = args[2]

            if not (0 <= self.red <= 255
                and 0 <= self.green <= 255
                and 0 <= self.blue <= 255):
                print("RGB value must be between 0 and 255.")

            self.text_color = None

        # Text color
        elif len(args) == 1:
            color = args[0]

            flag = 1
            for i in self.ALLOWED:
                if color == i:
                    flag = 0
                    break
            
            if flag:
                print("Wrong color arg.")

            self.text_color = color

            self.red = 0
            self.green = 0
            self.blue = 0

        else:
            print("Що за цвет?")

    def to_svg(self):

        if self.text_color is not None:
            return self.text_color

        return f"rgb({self.red},{self.green},{self.blue})"

#класс родитель с абстракцией
class Object(abc.ABC):

    def __init__(self, fill_color, stroke_color, stroke_width):
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width

    def obj_print(self):
        return (
            f'fill="{self.fill_color.to_svg()}" '
            f'stroke="{self.stroke_color.to_svg()}" '
            f'stroke-width="{self.stroke_width}"'
        )

    #абстракция, ура!
    @abc.abstractmethod
    def print(self): pass


class Text(Object):
    def __init__(
        self,
        fill_col,
        stroke_col,
        stroke_wid,
        point,
        offset,
        font_size,
        font_family,
        data
    ):

        #используем super для метода родительского класса
        super().__init__(
            fill_col,
            stroke_col,
            stroke_wid
        )

        self.point = point
        self.offset = offset
        self.font_size = font_size
        self.font_family = font_family
        self.data = data

    #перегруз
    def print(self):

        return (
            f'    <text '
            f'x="{self.point.x}" '
            f'y="{self.point.y}" '
            f'dx="{self.offset.x}" '
            f'dy="{self.offset.y}" '
            f'font-size="{self.font_size}" '
            f'font-family="{self.font_family}" '
            f'{self.obj_print()}>\n'
            f'        {self.data}\n'
            f'    </text>'
        )

#опять наследуемся
class Polyline(Object):

    def __init__(
        self,
        fill_col,
        stroke_col,
        stroke_wid,
        points
    ):

        super().__init__(
            fill_col,
            stroke_col,
            stroke_wid
        )

        self.points = points

    def print(self):

        for p in self.points:
            points_str = " ".join(f"{p.x}, {p.y}")

        return f"    <polyline points={points_str} {self.obj_print()} />"

class Circle(Object):

    def __init__(
        self,
        fill_col,
        stroke_col,
        stroke_wid,
        center,
        radius
    ):

        super().__init__(
            fill_col,
            stroke_col,
            stroke_wid
        )

        self.center = center
        self.radius = radius

    def print(self):

        return (
            f"    <circle cx={self.center.x} cy={self.center.y} r={self.radius} {self.obj_print()} />"
        )


# =========================
# Document
# =========================

class Document:

    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def print(self):

        result = []

        result.append(
            '<?xml version="1.0" encoding="UTF-8" ?>'
        )

        result.append(
            '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">'
        )

        for obj in self.objects:
            result.append(obj.print())

        result.append("</svg>")

        return "\n".join(result)

    def save(self, filename):

        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.print())


# =========================
# Reader utils
# =========================

def in_color():

    raw = input().strip().split()

    if len(raw) == 1:
        return Color(raw[0])

    if len(raw) == 3:
        return Color(
            float(raw[0]),
            float(raw[1]),
            float(raw[2])
        )

    print("Гадость в цвете.")


def in_double():
    return input().strip()


def in_point():

    x = float(input())
    y = float(input())

    return Point(x, y)


def poly_points(input_string):

    if input_string.strip() == "":
        print("Пустая точка?")

    result = []

    pairs = input_string.split()

    for pair in pairs:

        x, y = pair.split(",")

        result.append(
            Point(float(x), float(y))
        )

    return result



tags = {
    "print": 1,
    "test": 2,
    "text": 3,
    "polyline": 4,
    "circle": 5
}

fine_doc = Document()

print("Tags: test, print, text, polyline, circle")

while True:

    try:
        tag_input = input("\nEnter tag: ").strip()

        if tag_input == "":
            continue

        match tags.get(tag_input, -1):

            case 1:
                print(fine_doc.print())

            case 2:
                print("\nTest!\n")

            case 3:

                print("Enter fill-color:")
                fill = in_color()

                print("Enter stroke-color:")
                stroke_col = in_color()

                print("Enter stroke-width:")
                stroke_wid = in_double()

                print("Enter start-point:")
                point = in_point()

                print("Enter offset:")
                offset = in_point()

                print("Enter font-size:")
                font_size = in_double()

                font_family = input(
                    "Enter font-family: "
                )

                data = input(
                    "Enter text: "
                )

                fine_doc.add_object(
                    Text(
                        fill,
                        stroke_col,
                        stroke_wid,
                        point,
                        offset,
                        font_size,
                        font_family,
                        data
                    )
                )

                print(
                    "\nНовый text тег!\n"
                )

            case 4:

                print("Enter fill-color:")
                fill = in_color()

                print("Enter stroke-color:")
                stroke_col = in_color()

                print("Enter stroke-width:")
                stroke_wid = in_double()

                points = input(
                    "Enter points: "
                )

                fine_doc.add_object(
                    Polyline(
                        fill,
                        stroke_col,
                        stroke_wid,
                        poly_points(points)
                    )
                )

                print(
                    "\nНовый polyline тег!\n"
                )

            case 5:

                print("Enter fill-color:")
                fill = in_color()

                print("Enter stroke-color:")
                stroke_col = in_color()

                print("Enter stroke-width:")
                stroke_wid = in_double()

                print("Enter center:")
                center = in_point()

                print("Enter radius:")
                radius = in_double()

                fine_doc.add_object(
                    Circle(
                        fill,
                        stroke_col,
                        stroke_wid,
                        center,
                        radius
                    )
                )

                print(
                    "\Новый круг!\n"
                )

            case _:
                print("Че с тегом?")

    except KeyboardInterrupt:
        print("\nExit.")
        break

    except Exception as e:
        print(f"\nError:\n{e}")

print("\nFinal SVG:\n")
print(fine_doc.print())

fine_doc.save("output.svg")

print("\nSaved to output.svg")