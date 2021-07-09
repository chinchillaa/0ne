import pandas as pd
import numpy as np
#import tensorflow as tf
print("--------------------------------test--------------------------------")

print(np.random.randint(0, 2))
sample_array = np.array([2, 4, 5, 6])
sample_df = pd.DataFrame({
    "col1": sample_array,
    "col2": sample_array*2,
    "col3": ["a", "b", "c", "d"]
})

print(sample_df)
