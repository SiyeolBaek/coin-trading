import json
import requests
from os.path import dirname, abspath

config = json.loads(open(dirname(abspath(__file__)) + "/config.json").read())

class Upbit(object):
	def __init__(self):
		pass

	# 전체 거래 종목 가져오기
	def getMarket(self):
		url = "https://api.upbit.com/v1/market/all"

		querystring = {"isDetails":"false"}

		response = requests.request("GET", url, params=querystring)

		datas = json.loads(response.text)

		return datas

	# KRW 거래 종목 가져오기
	def getKrwMarket(self):
		markets = self.getMarket()
		datas = []

		for market in markets:
			if "KRW" in market['market']:
				datas.append(market)

		return datas

	# 분 차트 가져오기
	def getMinCharts(self, market_id, unit=1, count=1, to=''):
		url = "https://api.upbit.com/v1/candles/minutes/"+str(unit)

		querystring = {"market":market_id,"count":count}

		# 마지막 캔들 시간이 존재하는 경우
		if to != '':
			querystring['to'] = to

		response = requests.request("GET", url, params=querystring)

		try:
			datas = json.loads(response.text)
		except:
			# API 요청 과다로 인한 오류
			return False

		return datas