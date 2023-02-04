from sense_emu import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

mn = [10, 11, 14, 17, 21, 23, 25, 26, 31, 33, 35, 38, 42, 45, 46, 47]

pixels = [white if i in mn else black for i in range(64)]

sense.set_pixels(pixels)
