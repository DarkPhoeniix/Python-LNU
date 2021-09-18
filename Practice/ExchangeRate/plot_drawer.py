
from struct_exchange_rate import ExchangeRateForDay
from data_parser import parse_data
import point_forecasting
import matplotlib.pyplot as plt


def draw_plot(exchange_rates: [ExchangeRateForDay]):
    data = parse_data(exchange_rates)
    dates = [i.today[0:5] for i in exchange_rates]
    fig, axs = plt.subplots(1, 3, figsize=(9, 3))

    need_data = [i + 1 for i in range(len(dates))]
    forecast = [[None] * 2, [None] * 2, [None] * 2]
    for i in range(3):
        k, b = point_forecasting.line_by_least_squares_method([need_data, data[i][0]])
        forecast[i][0] = list((x*k+b) for x in range(len(dates)))
        k, b = point_forecasting.line_by_least_squares_method([need_data, data[i][1]])
        forecast[i][1] = list((x*k+b) for x in range(len(dates)))
    axs[0].set_title('PrivatBank')
    axs[1].set_title('Oschadbank')
    axs[2].set_title('Raiffeisen Bank')

    for i in range(3):
        axs[i].scatter(dates, data[i][0], color='#006561')
        axs[i].plot(dates, data[i][0], color='#006561')
        axs[i].plot(dates, forecast[i][0], color='#5CCDC9')
        axs[i].scatter(dates, data[i][1], color='#A64A00')
        axs[i].plot(dates, data[i][1], color='#A64A00')
        axs[i].plot(dates, forecast[i][1], color='#FFB173')

    min_lim = min(min(data[0][0]) - 0.2, min(data[1][0]) - 0.2, min(data[2][0]) - 0.2)
    max_lim = max(max(data[0][1]) + 0.2, max(data[1][1]) + 0.2, max(data[2][1]) + 0.2)
    axs[0].set_ylim(min_lim, max_lim)
    axs[1].set_ylim(min_lim, max_lim)
    axs[2].set_ylim(min_lim, max_lim)

    axs[0].tick_params(labelsize=8)
    axs[1].tick_params(labelsize=8)
    axs[2].tick_params(labelsize=8)

    fig.autofmt_xdate()

    plt.show()
