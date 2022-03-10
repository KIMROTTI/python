import pyupbit

access = "ZFYw3r9uHEUxSWPbdM3WAsKTjBn09su8OELshxmX"          # 본인 값으로 변경
secret = "VHu6XLoWoLo3w6U7ml7oKhmQBiJrd9Pk7nMgjDdE"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print(upbit.get_balance("KRW"))
