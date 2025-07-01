

import pandas as pd
import requests

df = pd.read_excel("image_sources.xlsx")
half_url = "https:"

for index, row in df.iterrows():
    src = row['Image Source']
    full_url = half_url + src

    try:
        response = requests.get(full_url)
        response.raise_for_status()

        filename = f"image{index + 1}.jpg"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(filename)

    except requests.RequestException as e:
        print(f"Failed to download image at index {index}: {e}")
