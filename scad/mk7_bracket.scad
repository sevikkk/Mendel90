depth = 30;
thick = 7;
height = 80;
rad = 5;
dx = 22.5;
offset = 3;



module base(){

	linear_extrude(height = depth) {
	       translate([-thick*0.5 + offset, 0]) square([dx/2+thick*2-offset, thick]);
		translate([-(dx/2+thick*1.5) + offset,height]) square([dx/2+thick*2-offset, thick]);
		translate([-thick*0.5+offset,0]) square([thick, height + thick]);
	};
}

module a() {
	difference() {
		base();
		translate([dx/2, -1, depth/2])  rotate ([-90, 0, 0]) cylinder(r = 3, h= thick + 2);
		translate([-dx/2, -1+height, depth/2])  rotate ([-90, 0, 0]) cylinder(r = 3, h= thick + 2);
	}
}

module mk7_bracket_stl() {
	translate([40, 5, 0]) rotate([0,0,90]) {
		a();
		translate([-15,-13,0]) a();
	}
}

mk7_bracket_stl();
