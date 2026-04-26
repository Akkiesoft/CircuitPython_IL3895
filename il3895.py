# SPDX-FileCopyrightText: 2026 Akkiesoft
# SPDX-FileCopyrightText: 2019 Scott Shawcroft for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
`il3895`
================================================================================

CircuitPython `displayio` drivers for IL3895-based ePaper displays


* Author(s): Akkiesoft, Scott Shawcroft (Original)

Implementation Notes
--------------------

**Hardware:**

* `WaveShare 250x122, 2.13inch E-Ink display HAT for Raspberry Pi (V1; HINK-E0213-G01 labeled) <https://www.waveshare.com/2.13inch-e-paper-hat.htm>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware (version 5+) for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

from epaperdisplay import EPaperDisplay

try:
    import typing

    from fourwire import FourWire
except ImportError:
    pass


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/Akkiesoft/CircuitPython_IL3895.git"

_START_SEQUENCE = (
    b"\x12\x80\x02"  # Software reset, 2ms delay
    b"\x01\x03\xf9\x00\x00"  # driver output control
    b"\x0c\x03\xd7\xd6\x9d"  # BOOSTER_SOFT_START_CONTROL
    b"\x11\x01\x03"  # Data entry sequence
    b"\x3c\x01\x03"  # Border color
    b"\x2c\x01\xA8"  # Vcom Voltage
    b"\x03\x01\x10"  # Set gate voltage
    b"\x04\x01\x19"  # Set source voltage
    b"\x3a\x01\x1a"  # Set dummy line period
    b"\x3b\x01\x08"  # Set gate line width
    b"\x32\x1e\x22\x55\xaa\x55\xaa\x55\xaa\x11\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x01\x00\x00\x00\x00\x00"  # LUT
    b"\x22\x01\xC4"  # DISPLAY_UPDATE_CONTROL_2
)

_STOP_SEQUENCE = b"\x10\x01\x01"  # Enter deep sleep


# pylint: disable=too-few-public-methods
class IL3895(EPaperDisplay):
    """IL3895 driver"""

    def __init__(self, bus: FourWire, **kwargs) -> None:
        stop_sequence = _STOP_SEQUENCE
        try:
            bus.reset()
        except RuntimeError:
            stop_sequence = b""
        super().__init__(
            bus,
            _START_SEQUENCE,
            stop_sequence,
            **kwargs,
            ram_width=122,
            ram_height=250,
            set_column_window_command=0x44,
            set_row_window_command=0x45,
            set_current_column_command=0x4E,
            set_current_row_command=0x4F,
            write_black_ram_command=0x24,
            refresh_display_command=0x20,
            refresh_time=2.2,
            address_little_endian=True,
        )
