from twilio.rest import Client
import serial
import time
sense = serial.Serial('COM4', 9600)

account_sid = 'AC4f3df2af353b7ac24970b0f2ae76eb96'  
auth_token = 'aa918568495f1dd5e9d2a56f6f64c8ea'
client = Client(account_sid, auth_token)

suara_tinggi = 400 #desibel
suara_bicara = 350 #desibel
suara_lingkungan = 340 #desibel

while True:
	while sense.inWaiting():
		sound=int(sense.readline().decode())
		if sound > suara_tinggi:
			messageTosend="Suara Tinggi Terdeteksi. Desibel terdeteksi: "+str(sound)+" Mungkin ada Kegaduhan, Segera Cek!"
		elif (sound > suara_bicara and sound < suara_tinggi):
			messageTosend="Suara Normal. Desibel terdeteksi : "+str(sound)+" Aman Bos!"
		elif (sound > suara_lingkungan and sound < suara_bicara):
			messageTosend="Suara Lingkungan. Desibel terdeteksi : "+str(sound)+" Mungkin ada maling atau aktivitas mencurigakan lainnya. Ayo Cepat ke Lokasi!" 

		message=client.messages.create(
			body=messageTosend,
			from_='whatsapp:+14155238886',
			to='whatsapp:+6281246105091'
        	)
		time.sleep(10)

print(message.sid)	