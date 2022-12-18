import serial

PORT = "/dev/cu.usbserial-14310"
BAUD_RATE = 9600

with serial.Serial(PORT,BAUD_RATE) as ser :

		while True:
			line = ser.readline().decode('utf-8')
			#print(line)
			valx = line.split()[1]  
			#valy = line.split("##")[1]
				

			print(valx)
			#print(valy)
		
			
