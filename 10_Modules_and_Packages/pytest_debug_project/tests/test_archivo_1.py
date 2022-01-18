from common import archivo_1
import pandas._testing as pd_testing
import pytest


@pytest.mark.test_rapido
@pytest.mark.parametrize('input_1, input_2',
						[(2,3), (4,5), (3,2)])
def test_mi_funcion_suma(input_1, input_2):
	assert isinstance(2, int)
	assert isinstance(archivo_1.mi_funcion_suma(input_1, input_2), int)

@pytest.mark.test_lento
def test_get_month_from_date(get_test_df):
	df_transformed = archivo_1.get_month_from_date(get_test_df)
	expected_dtypes = {'user_id': 'int64',
						'book_id': 'object',
						'rating': 'int64',
						'timestamp': 'object',
						'date': 'datetime64[ns]',
						'month':'int64'
						}
	assert df_transformed.dtypes.to_dict() == expected_dtypes
	assert df_transformed.shape[0] > 0
	pd_testing.assert_frame_equal(df_transformed.drop_duplicates(), df_transformed)

if __name__ == '__main__':
	test_mi_funcion_suma()