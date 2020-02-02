from datacleaner import DataCleaner

data_cleaner = DataCleaner('../files/mushrooms.csv')

encoded_df = data_cleaner.onehot_encode()
print(encoded_df)