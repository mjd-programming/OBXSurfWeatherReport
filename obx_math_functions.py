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