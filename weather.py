import requests
import time
from datetime import date
import matplotlib.pyplot as plt

record = {}

def main():
	plt.ion()
	plt.show()

	while True:
		temperatura_atual()
		forecast()
		info_dia()
		time.sleep(3600)

def info_dia():
	hoje = date.today()
	dados = record[hoje]
	horas = list(dados.keys())
	temps = list(dados.values())

	t_max = max(temps)
	t_min = min(temps)

	print("Temperatura minima: {:.2f}".format(t_min))
	print("Temperatura maxima: {:.2f}".format(t_max))

	if (0 in horas):
		horas[horas.index(0)] = 24

	plt.clf()
	plt.plot(horas, temps)
	plt.draw()
	plt.pause(0.001)

def forecast():
	response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=3448439&APPID=765901de0eabfedfe64d68292d7c4d08")
	data = eval(response.content)

	for forecast in data['list'][:8]:
		temp = forecast['main']['temp'] - 273.15
		t = time.gmtime(forecast['dt'])
		d = date.fromtimestamp(forecast['dt'])
		h = t.tm_hour
		adicionaTemp(d, h, temp)

def temperatura_atual():
	response_atual = requests.get("http://api.openweathermap.org/data/2.5/weather?id=3448439&APPID=765901de0eabfedfe64d68292d7c4d08")
	data_atual = eval(response_atual.content)

	t_atual = data_atual["main"]["temp"] - 273.15

	print("Temperatura atual: {:.2f}".format(t_atual))

def adicionaTemp(d, h, temp):
	if (d in record):
		record[d].update({h: temp})
	else:
		record[d] = {h: temp}

if __name__ == "__main__":
	main()