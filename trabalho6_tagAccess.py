from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.LOW)

leitor = SimpleMFRC522()
print("Aproxime a tag do leitor para leitura.")

id = int(leitor.read_id())

id_cadastrada = 82510128764

if id == id_cadastrada:
	print("acesso liberado")
	GPIO.output(16, GPIO.HIGH)
else:
	print("acesso negado")
	GPIO.output(20, GPIO.HIGH)
try:
	while(True):
		pass
except KeyobardInterrupt:
	GPIO.cleanup()
