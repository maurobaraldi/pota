import numpy as np
import matplotlib.pyplot as plt

algorithms = ["bubble", "selection", "insertion", "heap", "merge", "quick", "counting", "radix", "bucket"]
items = [500, 1000, 5000, 10000, 100000, 500000, 1000000]
results = {
    500: [16.604900, 8.62336, 0.79679, 2.07352, 3.30233, 1.63769, 0.52547, 1.77717, 0.79894],
    1000: [73.88114, 33.23245, 1.28841, 4.60839, 7.21716, 4.16755, 1.06859, 3.13401, 1.60336],
    5000: [1863.92402, 801.87225, 6.09517, 31.33440, 50.33111, 15.12646, 4.83965, 19.09208, 7.67183],
    10000: [7405.8659, 3343.93358, 10.48088, 65.58656, 99.00283, 35.84098, 11.22283, 36.25130, 15.54703],
    100000: [1005060.68038, 596893.49651, 108.17790, 829.51569, 1247.49302, 389.73093, 133.78453, 430.89866, 180.97448],
    500000: [0, 0, 618.35098, 5051.09500, 7371.846675872803, 2529.72531, 741.96052, 2741.41526, 1091.30454],
    1000000: [0, 0 ,1310.01019, 10977.40268, 15401.09872, 4776.71122, 1520.69568, 5104.99143, 2198.02904],
}

temp = results[1000000]
ind = np.arange(len(temp))  # the x locations for the groups
width = 0.30  # the width of the bars

fig, ax = plt.subplots()
plt.xticks(rotation=75)

bar = ax.bar(ind - width/2, temp, width, color='SkyBlue', label='1000000 itens')

ax.set_ylabel('Eficiencia em Milisegundos')
ax.set_title('Eficieciencia dos algoritimos.')
ax.set_xticks(ind)
ax.set_xticklabels(algorithms)
ax.legend()

def autolabel(rects, xpos='center'):
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height, '{}'.format(height), ha=ha[xpos], va='bottom', rotation="vertical")

autolabel(bar, "right")

plt.show()

