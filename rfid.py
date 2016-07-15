import serial


class SerialDevice:

    def __init__(self, port, baudrate, parity, stopbits, bytesize):
        self.port = port
        self.baudrate = baudrate
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize

    def openDevice(self):
        try:
            ser = serial.Serial()
            ser.port = self.port
            ser.baudrate = self.baudrate
            ser.bytesize = self.bytesize
            ser.parity = self.parity
            try:
                ser.open()
            except Exception, e:
                print("Device Open Error: "+str(e))

            data = ser.read(12)
            return data

        except Exception, e:
            print ("Unable to Initialize device: "+str(e))

        ser.close()


if __name__ == "__main__":
    device = SerialDevice("/dev/ttyUSB3", 9600, serial.PARITY_NONE,
                          serial.STOPBITS_ONE, serial.EIGHTBITS)
    print device.openDevice()
