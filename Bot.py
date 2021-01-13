from twilio.rest import Client
import serial
import time
ser = serial.Serial('COM5', 9600)


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC30e4b22a9af2c2d7ae472d014864480f'
auth_token = 'b161362257e39c4280735424d1d07a98'
client = Client(account_sid, auth_token)


while True:
    while ser.inWaiting():
        vib = ser.readline().decode()
        messageTosend="Alert!!! Suara Mencurigakan Terdeteksi, dengan besaran: "+str(vib)
        message = client.messages.create(
                              body=messageTosend,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+62895361708830'
                          )
        time.sleep(1)

print(message.sid)