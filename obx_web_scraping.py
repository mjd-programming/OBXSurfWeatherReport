import bs4
import requests
import re

locations = ["nags-head-pier", "Avon", "Kitty hawk", "Corolla", "Rodanthe", "Ocrecok", "duck", "Cape Hatteras"]


def get_soup(site):
    res = requests.get(site)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, features="html.parser")


def averages(surfline_data, temps):
    new_list = []
    for i in range(len(surfline_data)):
        av_temp = (surfline_data[i][1] + temps[i][1]) / 2
        new_list.append((surfline_data[i][0], av_temp))
    return new_list


def surfline_reports():
    sites = ["https://www.surfline.com/surf-report/nags-head-pier/5842041f4e65fad6a7708a40",
             "https://www.surfline.com/surf-report/avon-pier/5842041f4e65fad6a7708a3d",
             "https://www.surfline.com/surf-report/kitty-hawk-pier/5842041f4e65fad6a7708a44",
             "https://www.surfline.com/surf-report/corolla/5842041f4e65fad6a7708a46",
             "https://www.surfline.com/surf-report/rodanthe-pier/584204214e65fad6a7709d1b",
             "https://www.surfline.com/surf-report/ocracoke/5842041f4e65fad6a7708a3c",
             "https://www.surfline.com/surf-report/duck-pier/5842041f4e65fad6a7708a45",
             "https://www.surfline.com/surf-report/cape-hatteras-lighthouse/5842041f4e65fad6a7708a38"
             ]
    heights = []
    for site in sites:
        soup = get_soup(site)
        # Wave Height
        wave_height = soup.find_all(class_="quiver-surf-height")[-1].getText()
        if wave_height == 'Flat':
            wave_height = 0
        else:
            wave_tuple = re.findall(r'(\d)*-(\d)*', wave_height)[0]
            wave_height = sum([int(i) for i in wave_tuple])/2
        # Temperature
        temp = soup.find(class_="sl-wetsuit-recommender__conditions__weather").getText()
        temp = int(re.findall(r'\d+', temp)[0])

        heights.append((wave_height, temp))
    return heights


def gov_weather():
    sites = ["https://forecast.weather.gov/MapClick.php?lat=35.97843000000006&lon=-75.63601999999997#.XVL9zi2ZNZo",
             "https://forecast.weather.gov/MapClick.php?lat=35.2533&lon=-75.5232#.XVMF3i2ZNZo",
             "https://forecast.weather.gov/MapClick.php?lat=36.0973&lon=-75.7124#.XVMFBy2ZNZo",
             "https://forecast.weather.gov/MapClick.php?lat=36.3795&lon=-75.8303#.XVMFNS2ZNZo",
             "https://forecast.weather.gov/MapClick.php?lat=35.5958&lon=-75.4675#.XVMFay2ZNZo",
             "https://forecast.weather.gov/MapClick.php?lat=35.1109&lon=-75.98",
             "https://forecast.weather.gov/MapClick.php?lat=36.1707&lon=-75.7561#.XVMFui2ZNZo",
             "https://forecast.weather.gov/MapClick.php?lat=35.2533&lon=-75.5232#.XVMF3i2ZNZo"
             ]
    temps = []
    for site in sites:
        soup = get_soup(site)
        temp = soup.find_all(class_="myforecast-current-lrg")[-1].getText()
        temp = int(re.findall(r'\d*', temp)[0])
        temps.append((None, temp))
    return temps

def get_height_surf():
    print('starting...')
    surf = surfline_reports()
    print('processing...')
    gov = gov_weather()
    print('complete.')
    return averages(surf, gov)
