#materi 4 : Introduction to Machine Learning

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Contoh koordinat sintetis, bukan lokasi sebenarnya
data = {
    "nama": [
        "Fasilitas A",
        "Fasilitas B",
        "Fasilitas C",
        "Fasilitas D"
    ],
    "longitude": [
        102.250, 102.260, 102.275, 102.285
    ],
    "latitude": [
        -3.800, -3.810, -3.795, -3.820
    ]
}

# Membuat data geografis
gdf = gpd.GeoDataFrame(
    data,
    geometry=[
        Point(lon, lat)
        for lon, lat in zip(
            data["longitude"], data["latitude"]
        )
    ],
    crs="EPSG:4326"
)

# Mengubah koordinat ke proyeksi metrik
# agar perhitungan jarak menggunakan meter
gdf = gdf.to_crs("EPSG:32748")

# Menghitung jarak setiap fasilitas
# terhadap fasilitas pertama
referensi = gdf.geometry.iloc[0]
gdf["jarak_dari_A_meter"] = (
    gdf.geometry.distance(referensi).round(2)
)

print(
    gdf[["nama", "jarak_dari_A_meter"]]
)

# Visualisasi persebaran fasilitas
gdf.plot(
    color="blue",
    markersize=50,
    figsize=(8, 6)
)

for _, row in gdf.iterrows():
    plt.annotate(
        row["nama"],
        (row.geometry.x, row.geometry.y)
    )

plt.title("Persebaran Fasilitas Publik")
plt.axis("off")
plt.tight_layout()
plt.savefig("peta_fasilitas.png", dpi=200)
plt.show()

# Menyimpan hasil analisis
gdf.to_file(
    "hasil_fasilitas.geojson",
    driver="GeoJSON"
)
