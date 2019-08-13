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

def get_ordered_list(obx_list):
    o_list = [(obx_web.locations[i], obx_list[i][1], obx_list[i][0]) for i in range(len(obx_list))]
    return o_list