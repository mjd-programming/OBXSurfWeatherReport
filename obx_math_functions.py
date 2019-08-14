import obx_web_scraping as obx_web

multiply_percents = [(100-(i*25), i*25) for i in range(5)]

def get_average_wave_height(wave_heights):
    temp_waves = []
    for wave in wave_heights:
        temp_waves.append(sum(wave))
    return sum(temp_waves)/len(temp_waves)

def get_average_temperature(temps):
    temp_temps = []
    for temp in temps:
        temp_temps.append(temp)
    return sum(temp_temps)/len(temp_temps)

def get_ordered_list(obx_list):
    o_list = [(obx_web.locations[i], obx_list[i][1], obx_list[i][0]) for i in range(len(obx_list))]
    return o_list

def rank(list1, list2, multi): # list 1 sorted by temp, list2 sorted by wave heigth
    rankings = []
    length = len(list1)
    # get positions by temp
    for i in range(length):
        rankings.append([list1[i][0], i])  # (NAME, TEMP RANK)
    # get positions by wave height
    for i in range(length):
        for n in range(length):
            if list2[n][0] == rankings[i][0]:
                rankings[i].append(n)  # (NAME, TEMP RANK, WAVE RANK)

    # score = position in list1 * multipler + position in list2 * 1 - multipler
    scores = []
    for item in rankings:
        scores.append((item[0], (item[1] * (1 - multi) + (item[2] *  multi)))) # 0 = Best Temp, 1 = Best Waves

    return scores  # Lowest score wins


list1 = [('Nags Head', 81.0, 1.5), ('Avon', 83.5, 1.5), ('Kitty Hawk', 81.0, 0), ('Corolla', 77.0, 0), ('Rodanthe', 81.5, 1.5), ('Ocracoke', 83.5, 1.5), ('Duck', 81.0, 0), ('Cape Hatteras', 83.5, 1.5)]
list2 = [('Avon', 83.5, 1.5), ('Kitty Hawk', 81.0, 0), ('Corolla', 77.0, 0), ('Rodanthe', 81.5, 1.5), ('Ocracoke', 83.5, 1.5), ('Duck', 81.0, 0), ('Cape Hatteras', 83.5, 1.5), ('Nags Head', 81.0, 1.5)]

print(rank(list1, list2, .75))



