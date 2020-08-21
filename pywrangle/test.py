import pandas as pd
from decorator_df_change import record_size_change



df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
print(df.shape)

