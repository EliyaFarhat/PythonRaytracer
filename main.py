#!/usr/bin/env python
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material, Check

def main():
    WIDTH = 960
    HEIGHT = 540

    RENDERED_IMG = "2balls.ppm"
    CAMERA = Vector(0, -0.35, -1)

    OBJECTS = [
        # GROUND
        Sphere(Point(0, 10000.5, 1), 10000.0, Check(color1=Color.from_hex("#A7A7A7"),
                                                        color2=Color.from_hex("#BCD7D6"),
                                                        ambient=0.2,
                                                        reflection=0.2,)),
        Sphere(Point(0.75, -0.1, 1.0), 0.6, Material(Color.from_hex("#0000FF"))),
        Sphere(Point(0.10, -0.5, 0.5), 0.35, Material(Color.from_hex("#FF7355"))),
        Sphere(Point(-1, -0.1, 1.3), 0.6, Material(Color.from_hex("#000000"))),
        Sphere(Point(0.0, 0.0, -0.2), 0.2, Material(Color.from_hex("#076300")))
    ]
    LIGHTS = [Light(Point(1.5, -0.5, -10.0), Color.from_hex("#FFFFFF")),
              Light(Point(-0.5, -10.5, 0.0), Color.from_hex("#E6E6E6"))]
    scene = Scene(CAMERA, OBJECTS, LIGHTS, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()