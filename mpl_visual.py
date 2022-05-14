import matplotlib.pyplot as plt
import test

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(test.dates, test.highs, c='red', alpha=0.5)
ax.plot(test.dates, test.lows, c='blue', alpha=0.5)
ax.fill_between(test.dates, test.highs, test.lows, facecolor='blue', alpha=0.1)

"""方式1"""
ax.axes.xaxis.set_ticks(range(0, 365, 60))
ax.axes.xaxis.set_ticklabels(['2018-01', '2018-03', '2018-05', '2018-07', '2018-09', '2018-11', '2019-01'])

"""方式2"""
# ax.axes.xaxis.set_ticks(
#     range(0, 365, 60),
#     ['2018-01', '2018-03', '2018-05', '2018-07', '2018-09', '2018-11', '2019-01']
# )

"""方式3"""
# plt.xticks(range(0, 365, 60), ['2018-01', '2018-03', '2018-05', '2018-07', '2018-09', '2018-11', '2019-01'])

fig.autofmt_xdate()

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
ax.set_title('2018年每日温度', fontsize=18)
ax.set_xlabel('日期', fontsize=14)
ax.set_ylabel('温度(F)', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
