from datacleaner import DataCleaner, segment_data

data_cleaner = DataCleaner('../files/mushrooms.csv')

encoded_df = data_cleaner.onehot_encode()
sets = segment_data(encoded_df)
print("training set: ", len(sets[0]))
print("test set length: ", len(sets[1]))
