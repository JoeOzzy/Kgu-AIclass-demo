import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
import numpy as np
import os

fig, ax = plt.subplots(figsize=(14,12))
ax.set_facecolor('#cfe8f3')

# Simplified landmass outlines (approximate, hand-digitized for visual reference only)
china_coast = [
    (105,32),(112,32),(115,30),(117,28.5),(119.5,26.2),(120.5,24.5),(117.5,23.6),
    (114.5,22.8),(113.7,22.2),(112.4,21.7),(110.5,21.3),(108.6,21.6),(106.6,21.5),
    (105,22),(105,32)
]
hainan = [(108.6,20.2),(109.6,19.9),(110.8,19.3),(110.5,18.3),(109.4,18.4),(108.6,19.6),(108.6,20.2)]
taiwan = [(121.9,25.3),(122.0,24.5),(121.5,23.0),(120.8,21.9),(120.2,22.9),(120.0,24.2),(121.0,25.1),(121.9,25.3)]
luzon = [(120.3,18.6),(122.2,18.5),(122.3,17.0),(123.9,13.9),(122.7,13.0),(121.0,14.0),(120.0,15.5),(119.8,17.0),(120.3,18.6)]
vietnam = [(105,23.3),(104,22.5),(103.8,21.0),(105.9,20.7),(107.0,21.0),(107.9,20.5),(106.9,19.0),
           (106.0,17.5),(107.3,16.0),(109.2,13.0),(109.0,11.0),(107.0,9.0),(104.7,10.4),(104.7,14.0),
           (104.0,18.0),(103.0,20.5),(105,23.3)]

for poly in [china_coast, hainan, taiwan, luzon, vietnam]:
    p = Polygon(poly, closed=True, facecolor='#f0ead6', edgecolor='#8a8060', linewidth=0.8, zorder=1)
    ax.add_patch(p)

ax.set_xlim(104, 135)
ax.set_ylim(8, 32)
ax.set_aspect(1.05)
ax.grid(True, linewidth=0.3, linestyle='--', color='gray', alpha=0.6)
ax.set_xticks(range(105,136,5))
ax.set_yticks(range(8,33,4))
ax.set_xlabel('Longitude (deg E)', fontsize=9)
ax.set_ylabel('Latitude (deg N)', fontsize=9)

tracks = {
    "Hato (2017)*": {"color":"#9edae5", "pts":[(128,15.5),(122,17.5),(118,20.2),(114.6,21.6),(113.1,21.9)]},
    "Mangkhut (2018)*": {"color":"#7f7f7f", "pts":[(150,13),(140,13.8),(130,14.5),(122.5,15.3),(117,18.5),(113.9,21.9),(112.2,21.9)]},
    "Higos (2020)": {"color":"#1f77b4", "pts":[(133,15.5),(129,16.5),(124,18.5),(118,20.5),(114.5,21.7),(113.4,21.9)]},
    "Nesat (2022)": {"color":"#8c564b", "pts":[(126,17.0),(122,18.5),(119.5,20.0),(117,20.7),(114.5,21.0),(111.5,21.1)]},
    "Doksuri (2023)": {"color":"#ff7f0e", "pts":[(137,14.5),(130,15.8),(124.5,17.5),(121.5,19.6),(121.0,20.7),(120.3,22.0),(118.5,23.9),(118.58,24.7)]},
    "Saola (2023)": {"color":"#d62728", "pts":[(125.5,19.1),(122,19.8),(119.5,20.5),(117.8,21.0),(116.0,21.6),(114.3,22.0),(112.2,21.9)]},
    "Koinu (2023)": {"color":"#e377c2", "pts":[(129,16.5),(124,18.5),(121.0,21.5),(120.5,22.3),(120.7,23.3),(118.0,23.6)]},
    "Yagi (2024)": {"color":"#2ca02c", "pts":[(131,15.0),(126,14.7),(121.9,15.9),(117,17.0),(112.0,18.6),(110.6,19.6),(108.5,20.0),(106.0,20.9)]},
    "Ragasa (2025)": {"color":"#9467bd", "pts":[(136,13.0),(129,14.5),(123,17.5),(121.0,20.4),(118.0,21.3),(115.0,21.5),(112.2,21.85),(109.5,21.9)]},
}

for name, d in tracks.items():
    pts = d["pts"]
    lons = [p[0] for p in pts]
    lats = [p[1] for p in pts]
    ax.plot(lons, lats, color=d["color"], linewidth=2.4, marker='o', markersize=4.5,
            zorder=5, path_effects=[pe.Stroke(linewidth=3.8, foreground='white'), pe.Normal()])
    ax.plot(lons[0], lats[0], marker='*', markersize=13, color=d["color"],
            markeredgecolor='black', markeredgewidth=0.6, zorder=6)
    ax.annotate('', xy=(lons[-1],lats[-1]), xytext=(lons[-2],lats[-2]),
                arrowprops=dict(arrowstyle='-|>', color=d["color"], lw=1.8), zorder=6)

city_labels = {
    "Hong Kong": (114.17, 22.32), "Taipei": (121.56, 25.03), "Guangzhou": (113.26, 23.13),
    "Shenzhen": (114.06, 22.54), "Manila": (120.98, 14.60), "Hanoi": (105.85, 21.03),
    "Haikou": (110.35, 20.03), "Fuzhou": (119.30, 26.08), "Kaohsiung": (120.31, 22.62),
    "Macau": (113.55, 22.20),
}
for name, (lon, lat) in city_labels.items():
    ax.plot(lon, lat, marker='s', color='black', markersize=4.5, zorder=7)
    ax.text(lon+0.4, lat+0.15, name, fontsize=8.5, fontweight='bold', zorder=7,
            path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

ax.text(112,26.5,"CHINA", fontsize=11, fontweight='bold', color='#5c5230', alpha=0.8)
ax.text(120.9,23.7,"TAIWAN", fontsize=9, fontweight='bold', color='#5c5230', alpha=0.8, rotation=90)
ax.text(122.5,12.5,"PHILIPPINES", fontsize=9, fontweight='bold', color='#5c5230', alpha=0.8)
ax.text(106,15,"VIETNAM", fontsize=9, fontweight='bold', color='#5c5230', alpha=0.8, rotation=75)
ax.text(125,25,"WEST PACIFIC\nOCEAN", fontsize=9, color='#2a5674', alpha=0.6, ha='center')
ax.text(112.5,18,"SOUTH CHINA\nSEA", fontsize=9, color='#2a5674', alpha=0.6, ha='center')

legend_elements = [Line2D([0],[0], color=d["color"], lw=2.4, marker='o', markersize=5, label=name)
                    for name, d in tracks.items()]
legend_elements.append(Line2D([0],[0], marker='*', color='gray', linestyle='None', markersize=12,
                               markeredgecolor='black', label='Formation point'))
leg = ax.legend(handles=legend_elements, loc='lower left', fontsize=9, framealpha=0.95, title="Typhoon (year)")
leg.get_title().set_fontweight('bold')

plt.title("Major Typhoon Tracks Affecting Hong Kong, Taiwan & Southern China (2020s)",
          fontsize=14.5, fontweight='bold', pad=14)
plt.figtext(0.5, 0.005,
            "Simplified reference paths (formation to landfall/dissipation), based on Hong Kong Observatory & JTWC post-storm reports.\nHato (2017) & Mangkhut (2018) shown in grey as pre-2020 reference storms for scale comparison. Coastlines are simplified for illustration, not navigational use.",
            ha='center', fontsize=8, style='italic')

plt.tight_layout()
os.makedirs('output', exist_ok=True)
plt.savefig('output/typhoon_tracks_hk_taiwan_china_2020s.png', dpi=200, bbox_inches='tight')
print("saved")
