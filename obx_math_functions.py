import obx_web_scraping as obx_web

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

def get_temperature_list(pref_temp, obx_list):
    o_list = [(obx_list[i].name, obx_list[i].temperature, obx_list[i].wave_height) for i in range(len(obx_list))]
    t_list = sorted(o_list, key=lambda obx_list_obj: abs(obx_list_obj[1] - pref_temp))
    return t_list

def get_wave_list(obx_list):
    o_list = [(obx_list[i].name, obx_list[i].temperature, obx_list[i].wave_height) for i in range(len(obx_list))]
    w_list = sorted(o_list, key=lambda obx_list_obj: obx_list_obj[2])
    r_list = w_list[::-1]
    return r_list

def get_obx_list(obx_list):
    return [(obx_web.locations[i], obx_list[i][1], obx_list[i][0]) for i in range(len(obx_list))]

def rank(list1, list2, m): # list 1 sorted by temp, list2 sorted by wave heigth TODO wave heights are not sorting correctly
    multi = m/100
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

    sorted_list = sorted(scores, key=lambda s: s[1])  # Lowest score wins
    t_list = []
    for l_object in sorted_list:
        for obx_list_obj in list1:
            if l_object[0] == obx_list_obj[0]:
                t_list.append(obx_list_obj)
                continue
    return t_list