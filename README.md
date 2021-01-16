# Coin Trading

업비트를 이용한 암호화폐 자동 매매 프로그램입니다.



## Backtesting

실제 매매를 진행하기 전 과거 데이터를 기반으로 백테스팅을 진행합니다.

백테스팅은 SQLite DB에 기록 될 예정이며, 테이블 정보는 아래와 같습니다.

### SQLite Table

```sql
CREATE TABLE "trades" (
	"no"	INTEGER,			/* 거래 고유번호 */
	"type"	TEXT,  			/* 거래 방식(매수, 매도) */
	"price"	INTEGER,		/* 거래 금액 */
	"amount"	INTEGER,	/* 거래 수량 */
	"balance"	INTEGER,	/* 잔고 */
	"timestamp"	TEXT,		/* 거래 시각(해당 분봉 시간) */
	PRIMARY KEY("no" AUTOINCREMENT)
);
```



## Requirements

- Python 3

- 업비트에서 발급 된 API 키 필요
- lib 폴더 내 API 정보를 담은 config.json 파일 구성 (아래 형태와 같음)

```json
{
  "access_key" : "access_key",
  "secret_key" : "secret_key"
}
```



## Usage

```
python app.py
```

