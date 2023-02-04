from os import path
from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

output_dir = path.join(path.sep, "home", "imurnane", "code")
temperature_file = open(path.join(output_dir, "temp.txt"), "w")
humidity_file = open(path.join(output_dir, "humid.txt"), "w")
pressure_file = open(path.join(output_dir, "pressure.txt"), "w")

for i in range(300):
    temperature_file.write(str(sense.temperature) + "\n")
    humidity_file.write(str(sense.humidity) + "\n")
    pressure_file.write(str(sense.pressure) + "\n")
    
    temperature_file.flush()
    humidity_file.flush()
    pressure_file.flush()
    
    sense.show_message(str(i))
    sleep(1)
    
temperature_file.close()
humidity_file.close()
pressure_file.close()
