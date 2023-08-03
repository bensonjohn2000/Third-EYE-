import RPi.GPIO as IO         #we are calling header file which helps us to use GPIO’s of PI
IO.setwarnings(False)          #do not show any warnings

IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN39 as ‘GPIO19’)

IO.setup(26,IO.IN)
IO.setwarnings(False)          # do not show any warnings
while True:
    if(IO.input(26) == False):       #if GPIO26 goes low execute the below statements
             print("Button Pressed")
# import serial
# import time
# # receiverNum = "+919746349717"
# # sim800l = serial.Serial(
# # port='/dev/ttyS0' ,
# # baudrate = 115200,
# # parity=serial.PARITY_NONE,
# # stopbits=serial.STOPBITS_ONE,
# # bytesize=serial.EIGHTBITS,
# # timeout=1
# # )
# # sms ="http://maps.google.com/?q="+str(500)+','+str(500);
# # time.sleep(1)
# # sim800l.write(str.encode('AT+CMGF=1\n'))
# # print (sim800l.read(24))
# # time.sleep(1)
# # cmd1 = "AT+CMGS=\""+str(receiverNum)+"\"\n"
# # sim800l.write(str.encode(cmd1))
# # print (sim800l.read(24))
# # time.sleep(1)
# # sim800l.write(str.encode(str(sms)))
# # sim800l.write(str.encode(chr(26)))
# # print (sim800l.read(24))
# # time.sleep(1)
# 
# def GPS_Info():
#     global NMEA_buff
#     global lat_in_degrees
#     global long_in_degrees
#     nmea_time = []
#     nmea_latitude = []
#     nmea_longitude = []
#     nmea_time = NMEA_buff[0]                    #extract time from GPGGA string
#     nmea_latitude = NMEA_buff[1]                #extract latitude from GPGGA string
#     nmea_longitude = NMEA_buff[3]               #extract longitude from GPGGA string
#     
#     #print("NMEA Time: ", nmea_time,'\n')
#     #print ("NMEA Latitude:", nmea_latitude,"NMEA Longitude:", nmea_longitude,'\n')
#     try:
#     
#         lat = float(nmea_latitude)                  #convert string into float for calculation
#         longi = float(nmea_longitude)               #convertr string into float for calculation
#         
#         lat_in_degrees = convert_to_degrees(lat)    #get latitude in degree decimal format
#         long_in_degrees = convert_to_degrees(longi) #get longitude in degree decimal format
#         
#     except:
#         lat_in_degrees = 0   #get latitude in degree decimal format
#         long_in_degrees = 0
#     
# #convert raw NMEA string into degree decimal format   
# def convert_to_degrees(raw_value):
#     decimal_value = raw_value/100.00
#     degrees = int(decimal_value)
#     mm_mmmm = (decimal_value - int(decimal_value))/0.6
#     position = degrees + mm_mmmm
#     position = "%.4f" %(position)
#     return position
#     
# 
# if __name__ == '__main__':
#     ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#     print(ser)
#     ser.reset_input_buffer()
#     while True:
# #          print("Start")
# #          if(IO.input(26) == False):       #if GPIO26 goes low execute the below statements
# #              print("Button Pressed")
#          #if ser.in_waiting > 0:
#                 line = ser.readline() #.decode('utf-8').rstrip()
#                 print(line)
#                 #print(line)
#                 gpgga_info = "$GPGGA,"      #Open port with baud rate
#                 GPGGA_buffer = 0
#                 NMEA_buff = 0
#                 lat_in_degrees = 0
#                 long_in_degrees = 0
#                 received_data = (str)(ser.readline())                   #read NMEA string received
#                 GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string                 
#                 if (GPGGA_data_available>0):
#                     GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  #store data coming after "$GPGGA," string 
#                     NMEA_buff = (GPGGA_buffer.split(','))               #store comma separated data in buffer
#                     GPS_Info()                                          #get time, latitude, longitude
#          
#                     print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\n')
#                     sms ="http://maps.google.com/?q="+lat_in_degrees+','+long_in_degrees;
#                     time.sleep(1)
#                     sim800l.write(str.encode('AT+CMGF=1\n'))
#                     print (sim800l.read(24))
#                     time.sleep(1)
#                     cmd1 = "AT+CMGS=\""+str(receiverNum)+"\"\n"
#                     sim800l.write(str.encode(cmd1))
#                     print (sim800l.read(24))
#                     time.sleep(1)
#                     sim800l.write(str.encode(str(sms)))
#                     sim800l.write(str.encode(chr(26)))
#                     print (sim800l.read(24))
#                     time.sleep(1)
# GPIO.cleanup()
# 