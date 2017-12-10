from solid import scad_render, use, union, multmatrix, translate
from solid.solidpython import extract_callable_signatures, scad_render_to_file
from solid.utils import draw_segment, Point3, euclidify, Red, Vector3, transform_to_point, Matrix4, scad_matrix, Green


class Connector(object):
    def __init__(self, position, direction, up=None, meta=None):
        self.position = position
        self.direction = direction.normalized()
        self.meta = meta
        self.up = up

    def generate(self):
        out = union()(
            draw_segment(
                [self.position, -self.direction * 50],
                vec_color=Red,
                arrow_rad=3
            )
        )

        if self.up:
            out.add(draw_segment(
                [self.position, -self.up * 20],
                vec_color=Green,
                arrow_rad=2
            ))

        return out

    def transform(self, m):
        new_position = m * self.position
        new_direction = m * self.direction
        if self.up:
            new_up = m * self.up
        else:
            new_up = self.up
        return Connector(new_position, new_direction, new_up, self.meta)

class Part(object):
    origin = Connector(
        Point3(0, 0, 0),
        Vector3(0, 1, 0),
        Vector3(0, 0, 1)
    )

    output_connectors = {}

    def __init__(self, input_connectors=None):
        self.position = None

        self.adjust_to_input(input_connectors)

    def adjust_to_input(self, input_connectors):
        self.position = self.origin

    def generate_at_origin(self):
        return union()

    def generate(self):
        obj = self.generate_at_origin()

        m = self.transform_matrix()

        sc_matrix = scad_matrix(m)
        return multmatrix(m=sc_matrix)(obj)

    def generate_output_connectors(self):
        m = self.transform_matrix()
        def _transform(v):
            if not v:
                return v
            if isinstance(v, Connector):
                return v.transform(m)
            elif isinstance(v, dict):
                new_v = {}
                for k, v1 in v.items():
                    new_v[k] = _transform(v1)
                return new_v
            elif isinstance(v, list):
                new_v = []
                for v1 in v:
                    new_v.append(_transform(v1))
                return new_v
            else:
                raise RuntimeError("Unsupported type")

        return _transform(self.output_connectors)

    def transform_matrix(self):
        m_rotate_base = Matrix4.new_look_at(
            Point3(0, 0, 0),
            -self.origin.direction,
            self.origin.up).inverse()
        m = Matrix4.new_look_at(
            Point3(0, 0, 0),
            -self.position.direction,
            self.position.up) * m_rotate_base
        move = self.position.position - self.origin.position
        m.d, m.h, m.l = move.x, move.y, move.z
        return m


class PartXIdlerBracket(Part):
    origin = Connector(
        Point3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(-1, 0, 0)
    )

    output_connectors = {
        "x_rods": [
            Connector(Point3(-10, -30, 10), Vector3(1, 0, 0), Vector3(0,0,1)),
            Connector(Point3(-10,  30, 10), Vector3(1, 0, 0), Vector3(0,0,1)),
        ]
    }

    def adjust_to_input(self, input_connectors):
        rod = input_connectors["rod"]
        screw = input_connectors["screw"]
        left = (screw.position - rod.position).cross(rod.direction)
        up = rod.direction.cross(left).normalize()

        self.position = Connector(rod.position, rod.direction, up)

    def generate_at_origin(self):
        return x_idler_bracket_stl()


fn = '../scad/x-end.scad'
use(fn)

rod = Connector(Point3(200,0,0), Vector3(1,1,1))
screw = Connector(Point3(190,10,0), Vector3(1,1,1))

a = PartXIdlerBracket({
    "rod": rod,
    "screw": screw
})

out = union()(
    a.origin.generate(),
    a.generate_at_origin(),
    a.generate(),
    a.position.generate(),
    rod.generate(),
    screw.generate()
)
connectors = a.output_connectors["x_rods"]
new_conns = a.generate_output_connectors()
connectors += new_conns["x_rods"]
for conn in connectors:
    out.add(conn.generate())

scad_render_to_file(out, "/tmp/render.scad", include_orig_code=False)

