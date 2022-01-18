from functools import reduce
import pandas as pd
from ..common2 import archivo_3

def mi_funcion_suma(*args) -> int:
	return reduce(lambda a, b: a+b, args)

def load_csv(path: str) -> pd.DataFrame:
	return pd.read_csv(path, sep = ',', decimal = '.')

def get_month_from_date(input_df: pd.DataFrame) -> pd.DataFrame:
	input_df['date'] = pd.to_datetime(input_df['timestamp'])
	input_df['month'] = input_df['date'].dt.month
	return input_df

if __name__ == '__main__':
	print(mi_funcion_suma(1,2,3,4,5))
	archivo_3.funcion_3()
