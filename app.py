import time
import datetime
from lib.upbit import Upbit

UNIT = 200

if __name__ == "__main__":
	upbit = Upbit()

	markets = upbit.getKrwMarket()

	datetime_format = "%Y-%m-%dT%H:%M:%S+09:00"

	# 20년 12월 1일 ~ 21년 1월 17일 거래 진행
	_from = datetime.datetime(2020, 12, 1, 0, 0, 0)
	_from += datetime.timedelta(minutes=UNIT) # 2020년 12월 1일 ~
	_to = datetime.datetime(2021, 1, 17, 0, 0, 0)
	targetTime = _from

	diff = _to - _from
	diff_mins = (diff.days * 24 * 60) + (diff.seconds // 60)

	for i in range(diff_mins // UNIT):
		targetTime += datetime.timedelta(minutes=UNIT)
		print("to :",targetTime.strftime(datetime_format))

		minCharts = upbit.getMinCharts("KRW-BTC", 1, UNIT, targetTime.strftime(datetime_format))

		# 오류가 발생 한 경우
		if minCharts == False:
			break

		for chart in minCharts:
			print(chart)
			time.sleep(1) # 너무 빠른 처리를 막기 위함