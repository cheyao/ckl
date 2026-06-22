#!/bin/env python3
from uuid import uuid4 as uuid
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print(f"Usage: {sys.argv[0]} [pitch] [number_of_rows]")
    pitch = float(sys.argv[1])
    rows = int(sys.argv[2])

    header =  \
        f"""(footprint "Castellated_1x{rows:02d}_P{pitch:.2f}mm_Vertical"
        (version 20260206)
        (generator "pcbnew")
        (generator_version "10.0")
        (layer "F.Cu")
        (descr "Through hole straight pin header, 1x{rows:02d}, {pitch:.2f}mm pitch, single row")
        (tags "Through hole pin header THT 1x{rows:02d} {pitch:.2f}mm single row")
        (property "Reference" "REF**"
            (at 0 -2.38 0)
            (layer "F.SilkS")
            (uuid "{uuid()}")
            (effects
                (font
                    (size 1 1)
                    (thickness 0.15)
                )
            )
        )
        (property "Value" "Castellated_1x10_P2.54mm_Vertical"
            (at 0 {pitch*(rows-0.5) + 1:.2f} 0)
            (layer "F.Fab")
            (uuid "{uuid()}")
            (effects
                (font
                    (size 1 1)
                    (thickness 0.15)
                )
            )
        )
        (property "Datasheet" ""
            (at 0 0 0)
            (layer "F.Fab")
            (hide yes)
            (uuid "{uuid()}")
            (effects
                (font
                    (size 1.27 1.27)
                )
            )
        )
        (property "Description" ""
            (at 0 0 0)
            (layer "F.Fab")
            (hide yes)
            (uuid "{uuid()}")
            (effects
                (font
                    (size 1.27 1.27)
                )
            )
        )
        (property "KiLib_Generator" "connector/pin_header_socket"
            (at 0 0 0)
            (layer "F.SilkS")
            (hide yes)
            (uuid "{uuid()}")
            (effects
                (font
                    (size 1 1)
                    (thickness 0.15)
                )
            )
        )
        (attr through_hole)
        (duplicate_pad_numbers_are_jumpers no)
        (fp_rect
            (start -{pitch/2+0.5:.2f} -{pitch/2:.2f})
            (end {pitch/2+0.5:.2f} {pitch*(rows-0.5):.2f})
            (stroke
                (width 0.05)
                (type solid)
            )
            (fill no)
            (layer "F.CrtYd")
            (uuid "{uuid()}")
        )
        (fp_line
            (start -{pitch/4:.3f} -{pitch/2:.2f})
            (end -{pitch/2:.2f} -{pitch/4:.3f})
            (stroke
                (width 0.1)
                (type solid)
            )
            (layer "F.Fab")
            (uuid "{uuid()}")
        )
        (fp_line
            (start -{pitch/2:.2f} {pitch*(rows-0.5):.2f})
            (end -{pitch/2:.2f} -{pitch/4:.3f})
            (stroke
                (width 0.1)
                (type solid)
            )
            (layer "F.Fab")
            (uuid "{uuid()}")
        )
        (fp_line
            (start -{pitch/4:.3f} -{pitch/2:.2f})
            (end {pitch/2:.2f} -{pitch/2:.2f})
            (stroke
                (width 0.1)
                (type solid)
            )
            (layer "F.Fab")
            (uuid "{uuid()}")
        )
        (fp_line
            (start {pitch/2:.2f} -{pitch/2:.2f})
            (end {pitch/2:.2f} {pitch*(rows-0.5):.2f})
            (stroke
                (width 0.1)
                (type solid)
            )
            (layer "F.Fab")
            (uuid "{uuid()}")
        )
        (fp_line
            (start {pitch/2:.2f} {pitch*(rows-0.5):.2f})
            (end -{pitch/2:.2f} {pitch*(rows-0.5):.2f})
            (stroke
                (width 0.1)
                (type solid)
            )
            (layer "F.Fab")
            (uuid "{uuid()}")
        )
        (fp_text user "${{REFERENCE}}"
            (at 0 {pitch*(rows/2-0.5):.2f} 90)
            (layer "F.Fab")
            (uuid "{uuid()}")
            (effects
                (font
                    (size 1 1)
                    (thickness 0.15)
                )
            )
        )
    """

    footer = \
    f"""	(embedded_fonts no)
        (model "${{KICAD10_3DMODEL_DIR}}/Connector_PinHeader_{pitch:.2f}mm.3dshapes/PinHeader_1x{rows:02d}_P{pitch:.2f}mm_Vertical.step"
            (offset
                (xyz 0.75 0 0)
            )
            (scale
                (xyz 1 1 1)
            )
            (rotate
                (xyz -0 -0 -0)
            )
        )
    )
    """

    file = f"Castellated_1x{rows:02d}_P{pitch:.2f}mm_Vertical.kicad_mod"
    with open(file, "w") as f:
        f.write(header)

        for num in range(rows):
            pad = \
            f"""	(pad "{num+1}" thru_hole circle
                    (at -{pitch*0.75/2:.3f} {pitch*num})
                    (size 1.35 1.35)
                    (drill 0.95)
                    (layers "*.Cu" "*.Mask")
                    (remove_unused_layers no)
                    (zone_connect 1)
                    (thermal_bridge_width 0.4)
                    (thermal_bridge_angle 0)
                    (thermal_gap 0.3)
                    (uuid "{uuid()}")
                )
                (pad "{num+1}" thru_hole circle
                    (at {pitch*0.75/2:.3f} {pitch*num})
                    (size 1.35 1.35)
                    (drill 0.95)
                    (layers "*.Cu" "*.Mask")
                    (remove_unused_layers no)
                    (zone_connect 1)
                    (thermal_bridge_width 0.4)
                    (thermal_bridge_angle 0)
                    (thermal_gap 0.3)
                    (uuid "{uuid()}")
                )
                (pad "{num+1}" smd rect
                    (at 0 {pitch*num})
                    (size 3 1.5)
                    (layers "F.Cu" "F.Mask")
                    (zone_connect 1)
                    (thermal_bridge_width 0.4)
                    (thermal_bridge_angle 0)
                    (thermal_gap 0.3)
                    (uuid "{uuid()}")
                )
                (pad "{num+1}" smd rect
                    (at 0 {pitch*num})
                    (size 3 1.5)
                    (layers "B.Cu" "B.Mask")
                    (zone_connect 1)
                    (thermal_bridge_width 0.4)
                    (thermal_bridge_angle 0)
                    (thermal_gap 0.3)
                    (uuid "{uuid()}")
                )
            """
            f.write(pad)

        f.write(footer)

