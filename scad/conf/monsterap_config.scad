//
// Mendel90
//
// GNU GPL v2
// seva@sevik.org
//
// Configuration file for Monsterap
//
// https://picasaweb.google.com/114257244810512271993/Monsterap
//
echo("Monsterap:");
// Local vitamins

M12_nut_depth = 9.5;
M12_nut_radius = 11;
M12_washer =      [12, 22, 1.5, false];
M12_nut = [12, 21,  9.5, 8, M12_washer, M12_nut_depth];
LM16UU = [30, 24, 16];
T5x8 =  [5, 8,  2.25];
MDF18    = [ "MD", "MDF sheet",    18, [0.4, 0.4, 0.2, 1    ], true];
NEMA17M  = [42.3, 39.5,   53.6/2, 25,     11,     2,     5,     24,     31 ];


Z_bearings = LM16UU;
Y_bearings = LM16UU;
X_bearings = LM16UU;

X_motor = NEMA17M;
Y_motor = NEMA17M;
Z_motor = NEMA17M;

X_travel = 303;
Y_travel = 250;
Z_travel = 300 + (500-426.5);

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
Z_screw_dia = 8;            // Studding for Z axis

Y_carriage_depth = bed_depth + 10;
Y_carriage_width = bed_width + 10;

Z_nut_radius = M8_nut_radius;
Z_nut_depth = M8_nut_depth;
Z_nut = M8_nut;

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
