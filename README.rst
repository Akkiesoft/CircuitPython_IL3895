Introduction
============

CircuitPython `displayio` drivers for IL3895-based ePaper displays.
This is a repository forked from `Adafruit_CircuitPython_SSD1675 <https://github.com/adafruit/Adafruit_CircuitPython_SSD1675>`_.

I adjusted the module parameters to ensure that the "WaveShare 250x122, 2.13inch E-Ink display HAT for Raspberry Pi(V1)` worked properly.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Installing
=====================

Please copy it manually to a suitable directory.

Usage Example
=============

.. code-block:: python

    """Simple test script for 2.13" 250x122 WaveShare E-Ink display HAT.

    Supported products:
      * WaveShare 250x122, 2.13inch E-Ink display HAT for Raspberry Pi
          * Only V1 (HINK-E0213-G01 labeled)
          * https://www.waveshare.com/2.13inch-e-paper-hat.htm
    """

    import time

    import board
    import busio
    import displayio
    from fourwire import FourWire

    import il3895

    displayio.release_displays()

    epd_cs = board.GP22
    epd_dc = board.GP10
    epd_reset = board.GP2
    epd_busy = board.GP6

    spi = busio.SPI(clock=board.GP18, MOSI=board.GP19)
    display_bus = FourWire(spi, command=epd_dc, chip_select=epd_cs, reset=epd_reset, baudrate=1000000)
    time.sleep(1)

    display = il3895.IL3895(display_bus, width=250, height=122, rotation=90, busy_pin=epd_busy)

    g = displayio.Group()

    pic = displayio.OnDiskBitmap("/display-ruler.bmp")
    t = displayio.TileGrid(pic, pixel_shader=pic.pixel_shader)
    g.append(t)

    display.root_group = g

    display.refresh()

    print("refreshed")

    time.sleep(120)

