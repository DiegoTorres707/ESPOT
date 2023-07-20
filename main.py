import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyexcel_ods


def ods_to_dataframe(file_path):
    # Lee el archivo .ods 
    data = pyexcel_ods.get_data(file_path)

    #Convertir datos al dataframe
    df = pd.DataFrame(data[next(iter(data))])
    return df


file_path = "registers.ods"

# archivo .ods y convertirlo en un DataFrame
df = ods_to_dataframe(file_path)


print(df)

