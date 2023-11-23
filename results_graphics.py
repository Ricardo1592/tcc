from matplotlib import pyplot as plt

def plot_graphics(waypoints: list, planning_times: list):
    x_axis = range(1, len(waypoints)+1)
    plt.figure(figsize=(10, 5))
    waypoints_max = max(waypoints)
    attempt_max_waypoint = waypoints.index(waypoints_max)
    waypoints_min = min(waypoints)
    attempt_min_waypoint = waypoints.index(waypoints_min)

    plt.subplot(1, 2, 1)
    plt.plot(x_axis, waypoints, label='Motion Plans', color='c')
    plt.annotate(f"max({waypoints_max}, {attempt_max_waypoint+1}, {planning_times[attempt_max_waypoint]})", [attempt_max_waypoint, waypoints_max], ha='center')
    plt.annotate(f"min({waypoints_min}, {attempt_min_waypoint+1}, {planning_times[attempt_min_waypoint]})", [attempt_min_waypoint, waypoints_min], ha='center')
    plt.title('Waypoints Planned for each attempt')
    plt.xlabel('Attempts')
    plt.ylabel('waypoints')
    plt.yscale('linear')
    # plt.ylim(min(waypoints), max(waypoints))

    # plt.grid(True)

    planning_times_max = max(planning_times)
    max_index = planning_times.index(planning_times_max)
    planning_times_min = min(planning_times)
    min_index = planning_times.index(planning_times_min)
    # Gerando gráfico para a variação de Posição
    plt.subplot(1, 2, 2)
    plt.plot(planning_times, color='c')
    plt.annotate(f"max({planning_times_max}, {max_index+1}, {waypoints[max_index]})", [max_index, planning_times_max], ha='center')
    plt.annotate(f"min({planning_times_min}, {min_index+1}, {waypoints[min_index]})", [min_index, planning_times_min], ha='center')
    plt.title('Planning time for each attempt')
    plt.xlabel('Attempts')
    plt.ylabel('planning_times(s)')

    # plt.grid(True)

    # Exibindo os gráficos
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    #JOINTS
    #RRT
    # waypoints25 = [82, 78, 76, 81, 78, 77, 78, 75, 87, 79, 89, 75, 79, 80, 79, 78, 78, 89, 78, 78, 99, 75, 90, 94, 85]
    # planning_times25 = [0.0356, 0.0396, 0.062, 0.0469, 0.0499, 0.0655, 0.049, 0.0476, 0.0798, 0.0597, 0.0339, 0.0503, 0.0651, 0.0426, 0.0395, 0.0501, 0.0455, 0.0494, 0.0373, 0.0441, 0.0492, 0.0411, 0.0772, 0.0322, 0.0448]
    # plot_graphics(waypoints25, planning_times25)
    # waypoints50 = [82, 78, 76, 81, 78, 77, 78, 75, 87, 79, 89, 75, 79, 80, 79, 78, 78, 89, 78, 78, 99, 75, 90, 94, 85, 77, 85, 82, 84, 75, 84, 87, 81, 76, 85, 76, 78, 89, 92, 77, 76, 76, 85, 75, 81, 77, 89, 85, 77, 79]
    # planning_times50 = [0.0356, 0.0396, 0.062, 0.0469, 0.0499, 0.0655, 0.049, 0.0476, 0.0798, 0.0597, 0.0339, 0.0503, 0.0651, 0.0426, 0.0395, 0.0501, 0.0455, 0.0494, 0.0373, 0.0441, 0.0492, 0.0411, 0.0772, 0.0322, 0.0448, 0.0461, 0.0501, 0.0643, 0.0502, 0.0902, 0.0503, 0.0542, 0.0405, 0.057, 0.0354, 0.0743, 0.0901, 0.0598, 0.0259, 0.0491, 0.0455, 0.0505, 0.0607, 0.058, 0.0465, 0.0395, 0.0873, 0.0338, 0.0364, 0.0348]
    # plot_graphics(waypoints50, planning_times50)
    # waypoints100 = [83, 79, 76, 76, 87, 93, 85, 81, 74, 83, 91, 86, 76, 86, 75, 76, 82, 89, 81, 82, 80, 78, 86, 76, 81, 82, 85, 87, 75, 87, 80, 84, 102, 81, 76, 90, 74, 79, 78, 75, 85, 80, 78, 77, 74, 74, 78, 95, 83, 74, 79, 87, 78, 77, 85, 85, 89, 76, 80, 79, 81, 76, 76, 84, 78, 76, 80, 100, 77, 80, 77, 82, 83, 91, 90, 176, 82, 88, 81, 77, 78, 79, 84, 80, 80, 91, 102, 77, 97, 78, 76, 81, 78, 86, 76, 84, 74, 74, 82, 84]
    # planning_times100 = [0.0621, 0.0389, 0.0646, 0.086, 0.073, 0.0705, 0.0433, 0.0444, 0.0373, 0.0557, 0.0469, 0.0589, 0.0527, 0.0481, 0.05, 0.0441, 0.0973, 0.0677, 0.0458, 0.0738, 0.0802, 0.0483, 0.0526, 0.0615, 0.0575, 0.0427, 0.0339, 0.0789, 0.0458, 0.0386, 0.0682, 0.0858, 0.0577, 0.0477, 0.0531, 0.0458, 0.088, 0.0489, 0.0419, 0.0357, 0.0462, 0.0334, 0.0272, 0.0492, 0.0394, 0.0404, 0.0444, 0.0827, 0.0688, 0.0404, 0.0627, 0.0464, 0.0478, 0.068, 0.096, 0.0754, 0.0871, 0.0753, 0.0506, 0.05, 0.0368, 0.0342, 0.0449, 0.0877, 0.059, 0.0523, 0.0926, 0.098, 0.0559, 0.0432, 0.0461, 0.0698, 0.048, 0.0475, 0.0883, 0.0653, 0.0737, 0.0518, 0.053, 0.038, 0.0562, 0.085, 0.0661, 0.0644, 0.0375, 0.0436, 0.0594, 0.0619, 0.0496, 0.0993, 0.053, 0.0714, 0.0551, 0.0424, 0.0552, 0.0447, 0.0493, 0.0823, 0.0581, 0.0446]
    # plot_graphics(waypoints100, planning_times100)

    #RRTStar
    # waypoints25 = [74, 78, 85, 91, 83, 76, 86, 81, 79, 77, 82, 80, 80, 75, 100, 78, 79, 78, 83, 76, 76, 81, 77, 94, 80]
    # planning_times25 = [0.0359, 0.0456, 0.0387, 0.0268, 0.0541, 0.0608, 0.0449, 0.0347, 0.0587, 0.0716, 0.0844, 0.0473, 0.0449, 0.054, 0.0441, 0.1203, 0.0488, 0.0433, 0.0435, 0.0576, 0.059, 0.0383, 0.0699, 0.0337, 0.0471]
    # plot_graphics(waypoints25, planning_times25)
    # waypoints50 = [79, 78, 83, 79, 77, 79, 74, 83, 77, 83, 85, 85, 85, 82, 76, 94, 78, 80, 78, 84, 78, 82, 78, 86, 78, 89, 88, 82, 78, 74, 81, 85, 90, 81, 82, 77, 81, 79, 89, 77, 82, 81, 82, 78, 80, 75, 78, 81, 96, 79, 78, 77, 80, 80, 86, 75, 78, 82, 77, 77, 78, 82, 86, 93, 76, 80, 76, 79, 80, 80, 83, 85, 78, 78, 75]
    # waypoints50 = waypoints50[25:]
    # planning_times50 = [0.0426, 0.0582, 0.0834, 0.0916, 0.0755, 0.046, 0.0518, 0.0391, 0.0464, 0.0426, 0.0542, 0.0421, 0.0509, 0.0416, 0.054, 0.0569, 0.0535, 0.0476, 0.0492, 0.0464, 0.0349, 0.0559, 0.0485, 0.0427, 0.0713, 0.0336, 0.0741, 0.0683, 0.0771, 0.0362, 0.0361, 0.0511, 0.0547, 0.0477, 0.0585, 0.0641, 0.0378, 0.0389, 0.0463, 0.0682, 0.0634, 0.0513, 0.0528, 0.0831, 0.0587, 0.0348, 0.0375, 0.0422, 0.0461, 0.0636, 0.0579, 0.0373, 0.0434, 0.1157, 0.0513, 0.0532, 0.0534, 0.0352, 0.0435, 0.0486, 0.0558, 0.0332, 0.0682, 0.1057, 0.045, 0.0368, 0.0436, 0.0401, 0.0461, 0.0527, 0.0523, 0.06, 0.0382, 0.0456, 0.0605]
    # planning_times50 = planning_times50[25:]
    # plot_graphics(waypoints50, planning_times50)
    # waypoints100 = [79, 78, 83, 79, 77, 79, 74, 83, 77, 83, 85, 85, 85, 82, 76, 94, 78, 80, 78, 84, 78, 82, 78, 86, 78, 89, 88, 82, 78, 74, 81, 85, 90, 81, 82, 77, 81, 79, 89, 77, 82, 81, 82, 78, 80, 75, 78, 81, 96, 79, 78, 77, 80, 80, 86, 75, 78, 82, 77, 77, 78, 82, 86, 93, 76, 80, 76, 79, 80, 80, 83, 85, 78, 78, 75, 83, 77, 82, 76, 83, 80, 81, 84, 93, 80, 77, 83, 76, 85, 81, 80, 101, 73, 79, 80, 76, 88, 83, 76, 78, 78, 88, 82, 79, 85, 84, 97, 86, 80, 83, 80, 85, 78, 107, 77, 136, 76, 75, 82, 76, 77, 85, 80, 190, 79, 79, 82, 81, 80, 98, 88, 78, 98, 75, 81, 76, 76, 97, 81, 79, 88, 81, 87, 80, 85, 96, 76, 91, 92, 79, 79, 75, 82, 74, 81, 78, 90, 79, 81, 80, 82, 88, 78, 87, 80, 82, 78, 79, 84, 79, 82, 74, 75, 79, 79]
    # waypoints100 = waypoints100[75:]
    # planning_times100 = [0.0426, 0.0582, 0.0834, 0.0916, 0.0755, 0.046, 0.0518, 0.0391, 0.0464, 0.0426, 0.0542, 0.0421, 0.0509, 0.0416, 0.054, 0.0569, 0.0535, 0.0476, 0.0492, 0.0464, 0.0349, 0.0559, 0.0485, 0.0427, 0.0713, 0.0336, 0.0741, 0.0683, 0.0771, 0.0362, 0.0361, 0.0511, 0.0547, 0.0477, 0.0585, 0.0641, 0.0378, 0.0389, 0.0463, 0.0682, 0.0634, 0.0513, 0.0528, 0.0831, 0.0587, 0.0348, 0.0375, 0.0422, 0.0461, 0.0636, 0.0579, 0.0373, 0.0434, 0.1157, 0.0513, 0.0532, 0.0534, 0.0352, 0.0435, 0.0486, 0.0558, 0.0332, 0.0682, 0.1057, 0.045, 0.0368, 0.0436, 0.0401, 0.0461, 0.0527, 0.0523, 0.06, 0.0382, 0.0456, 0.0605, 0.062, 0.0601, 0.0562, 0.0475, 0.0464, 0.0394, 0.0504, 0.0367, 0.0563, 0.04, 0.0581, 0.0566, 0.043, 0.0384, 0.0463, 0.0378, 0.154, 0.0585, 0.0549, 0.0715, 0.048, 0.0369, 0.04, 0.1158, 0.0489, 0.0346, 0.0506, 0.0578, 0.0863, 0.0428, 0.0361, 0.0444, 0.0539, 0.0558, 0.0334, 0.0487, 0.0505, 0.0591, 0.062, 0.0417, 0.0714, 0.0527, 0.083, 0.0381, 0.047, 0.0451, 0.0646, 0.0316, 0.0635, 0.0444, 0.0543, 0.0585, 0.0415, 0.0359, 0.0539, 0.0545, 0.0473, 0.0319, 0.0357, 0.118, 0.0529, 0.0799, 0.0638, 0.0488, 0.0619, 0.0417, 0.0574, 0.0285, 0.0367, 0.043, 0.0296, 0.0599, 0.0404, 0.0415, 0.035, 0.0759, 0.0595, 0.0484, 0.0512, 0.0836, 0.0413, 0.0483, 0.0812, 0.0433, 0.0335, 0.045, 0.0441, 0.0851, 0.0419, 0.0552, 0.0438, 0.0593, 0.0487, 0.0483, 0.0393, 0.0419, 0.0502, 0.0524, 0.0634, 0.0396]
    # planning_times100 = planning_times100[:-75]
    # plot_graphics(waypoints100, planning_times100)

    # #LazyPRMStar
    # waypoints25 = [82, 87, 82, 84, 81, 75, 80, 78, 80, 80, 77, 84, 80, 79, 81, 76, 81, 79, 82, 78, 85, 78, 80, 76, 82]
    # planning_times25 = [0.0573, 0.0879, 0.0378, 0.0528, 0.0492, 0.0454, 0.0559, 0.0421, 0.0437, 0.0347, 0.1096, 0.0459, 0.0362, 0.0515, 0.0715, 0.0435, 0.0435, 0.0374, 0.0465, 0.0404, 0.0387, 0.032, 0.0435, 0.0551, 0.0391]
    # plot_graphics(waypoints25, planning_times25)
    # waypoints50 = [82, 87, 82, 84, 81, 75, 80, 78, 80, 80, 77, 84, 80, 79, 81, 76, 81, 79, 82, 78, 85, 78, 80, 76, 82, 96, 100, 77, 78, 96, 79, 75, 81, 79, 79, 79, 81, 80, 76, 79, 75, 76, 80, 75, 81, 75, 86, 80, 89, 82, 78, 82, 77, 75, 81, 78, 82, 91, 91, 82, 78, 83, 76, 78, 84, 87, 79, 86, 78, 76, 76, 78, 76, 89, 82]
    # waypoints50 = waypoints50[25:]
    # planning_times50 = [0.0573, 0.0879, 0.0378, 0.0528, 0.0492, 0.0454, 0.0559, 0.0421, 0.0437, 0.0347, 0.1096, 0.0459, 0.0362, 0.0515, 0.0715, 0.0435, 0.0435, 0.0374, 0.0465, 0.0404, 0.0387, 0.032, 0.0435, 0.0551, 0.0391, 0.0448, 0.0454, 0.0511, 0.1264, 0.0563, 0.0487, 0.0494, 0.1181, 0.0576, 0.0375, 0.0505, 0.0776, 0.0456, 0.0517, 0.0903, 0.0394, 0.0494, 0.0686, 0.0569, 0.0314, 0.0378, 0.0644, 0.0516, 0.0273, 0.0856, 0.0727, 0.0852, 0.0756, 0.0885, 0.04, 0.0837, 0.0633, 0.0389, 0.0708, 0.0506, 0.048, 0.038, 0.0595, 0.0445, 0.0325, 0.0503, 0.0588, 0.0571, 0.0501, 0.0515, 0.0836, 0.0436, 0.0392, 0.0542, 0.0399]
    # planning_times50 = planning_times50[25:]
    # plot_graphics(waypoints50, planning_times50)
    # waypoints100 = [82, 87, 82, 84, 81, 75, 80, 78, 80, 80, 77, 84, 80, 79, 81, 76, 81, 79, 82, 78, 85, 78, 80, 76, 82, 96, 100, 77, 78, 96, 79, 75, 81, 79, 79, 79, 81, 80, 76, 79, 75, 76, 80, 75, 81, 75, 86, 80, 89, 82, 78, 82, 77, 75, 81, 78, 82, 91, 91, 82, 78, 83, 76, 78, 84, 87, 79, 86, 78, 76, 76, 78, 76, 89, 82, 77, 75, 74, 77, 86, 74, 82, 79, 78, 86, 80, 74, 98, 75, 85, 78, 74, 77, 80, 93, 81, 81, 79, 78, 78, 79, 77, 79, 81, 77, 78, 79, 86, 80, 74, 82, 82, 79, 80, 75, 77, 85, 93, 79, 75, 85, 77, 79, 76, 77, 83, 75, 84, 82, 78, 77, 79, 76, 90, 142, 79, 86, 81, 80, 96, 90, 79, 78, 76, 77, 81, 97, 82, 85, 79, 82, 79, 91, 83, 77, 76, 93, 83, 78, 83, 76, 83, 89, 77, 74, 90, 89, 81, 86, 78, 76, 77, 78, 85, 79]
    # waypoints100 = waypoints100[75:]
    # planning_times100 = [0.0573, 0.0879, 0.0378, 0.0528, 0.0492, 0.0454, 0.0559, 0.0421, 0.0437, 0.0347, 0.1096, 0.0459, 0.0362, 0.0515, 0.0715, 0.0435, 0.0435, 0.0374, 0.0465, 0.0404, 0.0387, 0.032, 0.0435, 0.0551, 0.0391, 0.0448, 0.0454, 0.0511, 0.1264, 0.0563, 0.0487, 0.0494, 0.1181, 0.0576, 0.0375, 0.0505, 0.0776, 0.0456, 0.0517, 0.0903, 0.0394, 0.0494, 0.0686, 0.0569, 0.0314, 0.0378, 0.0644, 0.0516, 0.0273, 0.0856, 0.0727, 0.0852, 0.0756, 0.0885, 0.04, 0.0837, 0.0633, 0.0389, 0.0708, 0.0506, 0.048, 0.038, 0.0595, 0.0445, 0.0325, 0.0503, 0.0588, 0.0571, 0.0501, 0.0515, 0.0836, 0.0436, 0.0392, 0.0542, 0.0399, 0.0623, 0.0598, 0.0505, 0.0749, 0.0476, 0.0405, 0.0377, 0.0332, 0.0609, 0.0353, 0.0294, 0.0755, 0.0365, 0.0577, 0.0702, 0.0799, 0.0551, 0.0499, 0.0406, 0.0292, 0.0496, 0.0449, 0.0365, 0.0723, 0.0366, 0.0399, 0.0635, 0.0549, 0.0495, 0.0527, 0.0491, 0.0397, 0.041, 0.0475, 0.0443, 0.0373, 0.0461, 0.0634, 0.0345, 0.0492, 0.0368, 0.0641, 0.0409, 0.0543, 0.1375, 0.042, 0.0526, 0.0445, 0.0411, 0.0311, 0.0524, 0.0341, 0.0447, 0.0391, 0.0435, 0.0468, 0.0721, 0.0978, 0.0451, 0.0877, 0.0606, 0.0487, 0.0364, 0.0683, 0.046, 0.039, 0.0462, 0.0493, 0.0716, 0.0454, 0.0371, 0.0527, 0.036, 0.0583, 0.043, 0.0522, 0.0746, 0.0421, 0.0535, 0.0634, 0.0509, 0.0629, 0.072, 0.0553, 0.0697, 0.06, 0.0714, 0.0428, 0.059, 0.0431, 0.0354, 0.0436, 0.0867, 0.0456, 0.0562, 0.0563, 0.0555, 0.0585, 0.0291, 0.0443]
    # planning_times100 = planning_times100[:-75]
    # plot_graphics(waypoints100, planning_times100)

    #POSE
    # # RRT
    # waypoints25 = [50, 85, 50, 50, 85, 85, 58, 58, 76, 85, 58, 62, 84, 50, 80, 50, 50, 74, 50, 81, 58, 58, 58, 58, 82]
    # planning_times25 = [0.0725, 0.0686, 0.0275, 0.0435, 0.1263, 0.0623, 0.0306, 0.0289, 0.0532, 0.0926, 0.0694, 0.0824, 0.106, 0.0317, 0.0631, 0.0427, 0.0521, 0.0688, 0.0404, 0.0775, 0.0395, 0.0317, 0.0313, 0.0292, 0.1132]
    # plot_graphics(waypoints25, planning_times25)
    # waypoints50 = [50, 85, 50, 50, 85, 85, 58, 58, 76, 85, 58, 62, 84, 50, 80, 50, 50, 74, 50, 81, 58, 58, 58, 58, 82, 84, 58, 60, 81, 75, 58, 58, 50, 86, 58, 50, 84, 58, 58, 58, 83, 75, 58, 83, 58, 50, 58, 50, 50, 50, 83, 58, 87, 50, 58, 58, 50, 83, 90, 95, 86, 73, 50, 89, 86, 84, 61, 50, 50, 50, 85, 73, 50, 58, 86]
    # waypoints50 = waypoints50[25:]
    # planning_times50 = [0.0725, 0.0686, 0.0275, 0.0435, 0.1263, 0.0623, 0.0306, 0.0289, 0.0532, 0.0926, 0.0694, 0.0824, 0.106, 0.0317, 0.0631, 0.0427, 0.0521, 0.0688, 0.0404, 0.0775, 0.0395, 0.0317, 0.0313, 0.0292, 0.1132, 0.0526, 0.0501, 0.0695, 0.0626, 0.068, 0.0304, 0.0986, 0.1351, 0.0664, 0.0538, 0.0415, 0.0964, 0.0311, 0.1672, 0.0378, 0.0635, 0.0679, 0.0362, 0.0671, 0.0555, 0.0894, 0.027, 0.0498, 0.0208, 0.0421, 0.2527, 0.0927, 0.1216, 0.0362, 0.0407, 0.0389, 0.0391, 0.0659, 0.0956, 0.074, 0.0967, 0.0923, 0.0314, 0.0898, 0.052, 0.0909, 0.0961, 0.0262, 0.1058, 0.04, 0.0726, 0.1104, 0.0293, 0.051, 0.0861]
    # planning_times50 = planning_times50[25:]
    # plot_graphics(waypoints50, planning_times50)

    # RRTStar
    waypoints25 = [74, 78, 85, 91, 83, 76, 86, 81, 79, 77, 82, 80, 80, 75, 100, 78, 79, 78, 83, 76, 76, 81, 77, 94, 80]
    planning_times25 = [0.0359, 0.0456, 0.0387, 0.0268, 0.0541, 0.0608, 0.0449, 0.0347, 0.0587, 0.0716, 0.0844, 0.0473, 0.0449, 0.054, 0.0441, 0.1203, 0.0488, 0.0433, 0.0435, 0.0576, 0.059, 0.0383, 0.0699, 0.0337, 0.0471]
    plot_graphics(waypoints25, planning_times25)
    waypoints50 = [79, 78, 83, 79, 77, 79, 74, 83, 77, 83, 85, 85, 85, 82, 76, 94, 78, 80, 78, 84, 78, 82, 78, 86, 78, 89, 88, 82, 78, 74, 81, 85, 90, 81, 82, 77, 81, 79, 89, 77, 82, 81, 82, 78, 80, 75, 78, 81, 96, 79, 78, 77, 80, 80, 86, 75, 78, 82, 77, 77, 78, 82, 86, 93, 76, 80, 76, 79, 80, 80, 83, 85, 78, 78, 75]
    waypoints50 = waypoints50[25:]
    planning_times50 = [0.0426, 0.0582, 0.0834, 0.0916, 0.0755, 0.046, 0.0518, 0.0391, 0.0464, 0.0426, 0.0542, 0.0421, 0.0509, 0.0416, 0.054, 0.0569, 0.0535, 0.0476, 0.0492, 0.0464, 0.0349, 0.0559, 0.0485, 0.0427, 0.0713, 0.0336, 0.0741, 0.0683, 0.0771, 0.0362, 0.0361, 0.0511, 0.0547, 0.0477, 0.0585, 0.0641, 0.0378, 0.0389, 0.0463, 0.0682, 0.0634, 0.0513, 0.0528, 0.0831, 0.0587, 0.0348, 0.0375, 0.0422, 0.0461, 0.0636, 0.0579, 0.0373, 0.0434, 0.1157, 0.0513, 0.0532, 0.0534, 0.0352, 0.0435, 0.0486, 0.0558, 0.0332, 0.0682, 0.1057, 0.045, 0.0368, 0.0436, 0.0401, 0.0461, 0.0527, 0.0523, 0.06, 0.0382, 0.0456, 0.0605]
    planning_times50 = planning_times50[25:]
    plot_graphics(waypoints50, planning_times50)
    waypoints100 = [79, 78, 83, 79, 77, 79, 74, 83, 77, 83, 85, 85, 85, 82, 76, 94, 78, 80, 78, 84, 78, 82, 78, 86, 78, 89, 88, 82, 78, 74, 81, 85, 90, 81, 82, 77, 81, 79, 89, 77, 82, 81, 82, 78, 80, 75, 78, 81, 96, 79, 78, 77, 80, 80, 86, 75, 78, 82, 77, 77, 78, 82, 86, 93, 76, 80, 76, 79, 80, 80, 83, 85, 78, 78, 75, 83, 77, 82, 76, 83, 80, 81, 84, 93, 80, 77, 83, 76, 85, 81, 80, 101, 73, 79, 80, 76, 88, 83, 76, 78, 78, 88, 82, 79, 85, 84, 97, 86, 80, 83, 80, 85, 78, 107, 77, 136, 76, 75, 82, 76, 77, 85, 80, 190, 79, 79, 82, 81, 80, 98, 88, 78, 98, 75, 81, 76, 76, 97, 81, 79, 88, 81, 87, 80, 85, 96, 76, 91, 92, 79, 79, 75, 82, 74, 81, 78, 90, 79, 81, 80, 82, 88, 78, 87, 80, 82, 78, 79, 84, 79, 82, 74, 75, 79, 79]
    waypoints100 = waypoints100[75:]
    planning_times100 = [0.0426, 0.0582, 0.0834, 0.0916, 0.0755, 0.046, 0.0518, 0.0391, 0.0464, 0.0426, 0.0542, 0.0421, 0.0509, 0.0416, 0.054, 0.0569, 0.0535, 0.0476, 0.0492, 0.0464, 0.0349, 0.0559, 0.0485, 0.0427, 0.0713, 0.0336, 0.0741, 0.0683, 0.0771, 0.0362, 0.0361, 0.0511, 0.0547, 0.0477, 0.0585, 0.0641, 0.0378, 0.0389, 0.0463, 0.0682, 0.0634, 0.0513, 0.0528, 0.0831, 0.0587, 0.0348, 0.0375, 0.0422, 0.0461, 0.0636, 0.0579, 0.0373, 0.0434, 0.1157, 0.0513, 0.0532, 0.0534, 0.0352, 0.0435, 0.0486, 0.0558, 0.0332, 0.0682, 0.1057, 0.045, 0.0368, 0.0436, 0.0401, 0.0461, 0.0527, 0.0523, 0.06, 0.0382, 0.0456, 0.0605, 0.062, 0.0601, 0.0562, 0.0475, 0.0464, 0.0394, 0.0504, 0.0367, 0.0563, 0.04, 0.0581, 0.0566, 0.043, 0.0384, 0.0463, 0.0378, 0.154, 0.0585, 0.0549, 0.0715, 0.048, 0.0369, 0.04, 0.1158, 0.0489, 0.0346, 0.0506, 0.0578, 0.0863, 0.0428, 0.0361, 0.0444, 0.0539, 0.0558, 0.0334, 0.0487, 0.0505, 0.0591, 0.062, 0.0417, 0.0714, 0.0527, 0.083, 0.0381, 0.047, 0.0451, 0.0646, 0.0316, 0.0635, 0.0444, 0.0543, 0.0585, 0.0415, 0.0359, 0.0539, 0.0545, 0.0473, 0.0319, 0.0357, 0.118, 0.0529, 0.0799, 0.0638, 0.0488, 0.0619, 0.0417, 0.0574, 0.0285, 0.0367, 0.043, 0.0296, 0.0599, 0.0404, 0.0415, 0.035, 0.0759, 0.0595, 0.0484, 0.0512, 0.0836, 0.0413, 0.0483, 0.0812, 0.0433, 0.0335, 0.045, 0.0441, 0.0851, 0.0419, 0.0552, 0.0438, 0.0593, 0.0487, 0.0483, 0.0393, 0.0419, 0.0502, 0.0524, 0.0634, 0.0396]
    planning_times100 = planning_times100[75:]
    plot_graphics(waypoints100, planning_times100)

