from solid import use, union
from solid.connectors import Container, Connector
from solid.solidpython import scad_render_to_file
from solid.utils import Point3, Vector3


class PartXIdlerBracket(Container):
    origin = Connector(
        Point3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(-1, 0, 0)
    )

    origin_output_connectors = {
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
    a.origin,
    a.generate_at_origin(),
    a,
    a.position,
    rod,
    screw
)
connectors = a.origin_output_connectors["x_rods"]
new_conns = a.output_connectors
connectors += new_conns["x_rods"]
for conn in connectors:
    out.add(conn)

scad_render_to_file(out, "/tmp/render.scad", include_orig_code=False)

