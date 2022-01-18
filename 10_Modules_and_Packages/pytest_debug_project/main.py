from common.archivo_1 import mi_funcion_suma, load_csv, get_month_from_date
import os

if __name__ == '__main__':
	print(os.path.abspath(os.path.dirname(__file__)))
	mi_funcion_suma(2,43)
	df = load_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'ratings.csv'))
	df = get_month_from_date(df)
	print(df)
