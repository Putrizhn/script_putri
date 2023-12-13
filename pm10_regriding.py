#mengimport modul yang diperlukan
#script ini digunakan untuk melakukan regriding menjadi mikrogram/meter kubik
import pandas as pd  
import xarray as xr
from netCDF4 import Dataset
import numpy as np

ds = xr.open_dataset(r"PM_10/pm10.nc") # membuka file nc
ds
# latii = [2.8,2.4,2,1.6,1.2,0.8,0.4,0.0,-0.2,-0.4,-0.8,-1.2,-1.6,-2,-2.4,-2.8,-3.2,-3.6-4 ]
# lonii = [98,98.4,98.8,99.2,99.6,100,100.32,100.4,100.8,101.2,101.6,102,102.4,102.8,103.2,103.6,104]
latii = [-6.1556594]
lonii = [106.8388152]
# 100.32, -0.2 GAWbkt
# -6.1556594,106.8388152 stamet kemayoran

#menentukan longitude baru
new_lon = np.arange(ds.longitude[0], ds.longitude[-1], 0.05)  # 0.4 to 0.05
#menentukan latitude baru
new_lat = np.arange(ds.latitude[-1], ds.latitude[0], 0.05)
#melakukan regriding menggunakan interpolation
ds = ds.interp(latitude=new_lat, longitude=new_lon)  # Interpolation
# ds = ds.sel(latitude=latii,longitude=lonii,method="nearest")
# ds
df = ds.to_dataframe() # mengubah data menjadi tipe data frame 
#mengonversi kg/mikrogram kubik menjadi mikrogram/meter kubik
df ["pm10"] = df["pm10"] * 1000000000 #di kali
df.to_csv("/Users/Jia/Downloads/data_skripsi/PM_10/pm10_arrange.csv")