'''
	Raspberry Pi GPIO Status and Control
'''
# DEFINE FLASK APP LIBRARIES
from flask import Flask, render_template, request, jsonify

# DEFINE SERIAL LIBRARIES
import serial
import io

# DEFINE VAR
ser = serial.Serial()
ser.baudrate = 19200
ser.port = '/dev/ttyUSB0'
ser.timeout=1

# OPEN SERIAL
ser.open()
print(ser.is_open)
sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser), newline = '\r\n', line_buffering = True)


# DEFINE FUNCTIONS
def sendCommand(command):
        sio.write(str(command))
        sio.flush()
        print("Written: ", command)

def getResponse():
	print("In Get Response")
	counter = 0
	response = ''
	res = ''
	while True:
		sio.flush()
		response = sio.readline()
		res = res + response
		counter = counter + 1
#               print(counter)
		print(response) 
		if response == "":
			print("End Read")
			break
	return res

def powerStatus(device):

	command = ""

	if device == 'furman1':
		command = "?STATUS 0\r\n"
	if device == 'furman2':
		command = "?STATUS 0\r\n"
	if device == 'furman3':
		command = "?STATUS 0\r\n"

	sendCommand(command)

	while True:
		response = sio.readline()
		offString = "BANK1=OFF"
		print("test")
		print(response)
		onString = "BANK1=ON"
		if onString in response:
			print("It's ON")
			return True
			break
		elif offString in response:
			print("It's OFF")
			return False
			break

#DEFINE FLASK APP
app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(Hello='world')
	# Read Sensors Status

@app.route("/<deviceName>/status")
def statusHandler(deviceName):
	if deviceName == 'furman1':
		device = deviceName
	if deviceName == 'furman2':
		device = deviceName
	if deviceName == 'furman3':
		device = deviceName

	powerStatusVar = powerStatus(device)
#	print(powerStatusVar)

	return jsonify(powerStatus=powerStatusVar)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):

	if deviceName == 'furman1':
		device = '0'
	if deviceName == 'furman2':
		device = '1'
	if deviceName == 'furman3':
		device = '2'
	
	if action == "on":
		actionVar = "ON"
	if action == "off":
		actionVar = "OFF"

	commandString = "!SEQ_" + actionVar + " " + device + "\r\n"

#	print("TEST")
	print(commandString)
	#sendCommand("!SEQ_ON 0\r\n")
	#commandString = commandString + device + "\r\n"

	sendCommand(commandString)
	response = getResponse()

	deviceObj = {'deviceName':device,'status':actionVar,'command':commandString,'response':response}

	
	return jsonify(deviceObj)


if __name__ == "__main__":
   app.run(host='10.0.10.220', port=80, debug=True)
