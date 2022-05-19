import pyupbit
import numpy as np
# OHLCV: (open, high, low, close, volume)
df = pyupbit.get_ohlcv("KRW-BTC", count=100)
print(df)
df['range'] = (df['high'] - df['low']) * 0.8
df['target'] = df['open'] + df['range'].shift(1)
print(df['range'])
print(df['target'])
fee = 0.0005
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] + fee,
                     1)

print(df['ror'])
df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print(df['hpr'])
print(df['dd'])
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")