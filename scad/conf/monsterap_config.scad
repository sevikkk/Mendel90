//
// Mendel90
//
// GNU GPL v2
// nop.head@gmail.com
// hydraraptor.blogspot.com
//
// Configuration file
//
echo("Sturdy:");
Z_bearings = LM16UU;
Y_bearings = LM16UU;
X_bearings = LM16UU;

X_motor = NEMA17;
Y_motor = NEMA17;
Z_motor = NEMA17;

X_travel = 303;
Y_travel = 300;
Z_travel = 300;

bed_depth = 310;
bed_width = 310;
bed_pillars = M3x20_pillar;
bed_glass = glass2;
bed_thickness = 1.6 + sheet_thickness(bed_glass);    // PCB heater plus glass sheet
bed_holes = 305;

base = MDF18;
base_corners = 0;

frame = MDF12;
frame_corners = 0;
frame_nuts = false;

case_fan = fan80x38;
psu = KY240W;

single_piece_frame = true;
stays_from_window = false;

Y_carriage = DiBond;

extruder_width = 30;        // actually 28 but offset
nozzle_x_offset = 16;       // offset from centre of the extruder
nozzle_length = 50;         // from base of extruder to nozzle tip

X_belt = T5x8;
Y_belt = T5x8;

motor_shaft = 5;
Z_screw_dia = 12;            // Studding for Z axis

Y_carriage_depth = bed_depth + 10;
Y_carriage_width = bed_width + 10;

Z_nut_radius = M12_nut_radius;
Z_nut_depth = M12_nut_depth;
Z_nut = M12_nut;

//
// Default screw use where size doesn't matter
//
cap_screw = M4_cap_screw;
hex_screw = M4_hex_screw;
//
// Screw for the frame and base
//
frame_soft_screw = No6_screw;               // Used when sheet material is soft, e.g. wood
frame_thin_screw = M4_cap_screw;            // Used with nuts when sheets are thin
frame_thick_screw = M4_pan_screw;           // Used with tapped holes when sheets are thick and hard, e.g. plastic or metal
//
// Feature sizes
//
default_wall = 4;
thick_wall = 4;
