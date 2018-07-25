import requests
import time

def main():
	while True:
		forecast()
		time.sleep(20)

def forecast():
	response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=3448439&APPID=765901de0eabfedfe64d68292d7c4d08")
	data = eval(response.content)

	temperaturas = []
	for forecast in data['list'][:8]:
		temperaturas.append(forecast['main']['temp'] - 273.15)

	response_atual = requests.get("http://api.openweathermap.org/data/2.5/weather?id=3448439&APPID=765901de0eabfedfe64d68292d7c4d08")
	data_atual = eval(response_atual.content)

	t_atual = data_atual["main"]["temp"] - 273.15
	t_min = min(temperaturas)
	t_max = max(temperaturas)

	print("Temperatura atual: {:.2f}".format(t_atual))
	print("Temperatura minima: {:.2f}".format(t_min))
	print("Temperatura maxima: {:.2f}".format(t_max))

if __name__ == "__main__":
	main()