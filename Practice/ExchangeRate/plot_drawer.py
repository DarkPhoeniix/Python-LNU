
from copy import copy
from datetime import date, datetime, timedelta
from struct_exchange_rate import ExchangeRateForDay
from data_parser import parse_data
import point_forecasting
import matplotlib.pyplot as plt


def draw_plot(start_day: date, end_day: date, exchange_rates: [ExchangeRateForDay]):
    # checking dates boundaries
    if (datetime.strptime(exchange_rates[0].today, "%d/%m/%Y").date() > start_day) or \
       (datetime.strptime(exchange_rates[-1].today, "%d/%m/%Y").date() < end_day):
        print("No such data in files")

    # read available dates from files
    specified_data = [i for i in exchange_rates if datetime.strptime(i.today, "%d/%m/%Y").date() >= start_day and \
                                                   datetime.strptime(i.today, "%d/%m/%Y").date() <= end_day]
    data = parse_data(specified_data)
    dates = [i.today[0:5] for i in specified_data]  # get off year in dates

    # create plot with 3 subplots for different banks
    fig, axs = plt.subplots(1, 3, figsize=(9, 3))

    # replace dates with natural numbers for easier forecasting
    numbers = [i + 1 for i in range(len(dates))]
    forecast = [[None] * 2, [None] * 2, [None] * 2]
    forecast_dates = copy(dates)

    # add next day for forecasting
    forecast_dates.append((datetime.strptime(dates[-1], '%d/%m') + timedelta(days=1)).strftime('%d/%m'))
    for i in range(3):  # forecast by least squares method
        k, b = point_forecasting.line_by_least_squares_method([numbers, data[i][0]])
        forecast[i][0] = list((x*k+b) for x in range(len(forecast_dates)))
        k, b = point_forecasting.line_by_least_squares_method([numbers, data[i][1]])
        forecast[i][1] = list((x*k+b) for x in range(len(forecast_dates)))

    # print("Forecast for 'PrivatBank': \t" + forecast[0][0] + ' ' + forecast[0][1])
    # print("Forecast for 'Oschadbank': \t" + forecast[1][0] + ' ' + forecast[1][1])
    # print("Forecast for 'Raiffeisen Bank': \t" + forecast[2][0] + ' ' + forecast[2][1])

    # set titles
    axs[0].set_title('PrivatBank')
    axs[1].set_title('Oschadbank')
    axs[2].set_title('Raiffeisen Bank')
    # cycle for plot drawing
    for i in range(3):
        axs[i].plot(dates, data[i][0], 'o', ls='-', ms=4, color='#006561', label='purchase rate')
        axs[i].plot(forecast_dates, forecast[i][0], color='#5CCDC9')
        axs[i].plot(forecast_dates[-1], forecast[i][0][-1], 'o', ls='-', ms=4, color='#5CCDC9', label='purchase forecast')
        axs[i].annotate(str(round(forecast[i][1][-1], 2)), (forecast_dates[-1], forecast[i][1][-1]),
                        textcoords="offset points", xytext=(0, 10), ha='center', fontsize=7)
        axs[i].plot(dates, data[i][1], 'o', ls='-', ms=4, color='#A64A00', label='sale rate')
        axs[i].plot(forecast_dates, forecast[i][1], color='#FFB173')
        axs[i].plot(forecast_dates[-1], forecast[i][1][-1], 'o', ls='-', ms=4, color='#FFB173', label='sale forecast')
        axs[i].annotate(str(round(forecast[i][0][-1], 2)), (forecast_dates[-1], forecast[i][0][-1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=7)

    # calculate size of each plot
    min_lim = min(min(data[0][0]) - 0.2, min(data[1][0]) - 0.2, min(data[2][0]) - 0.2)
    max_lim = max(max(data[0][1]) + 0.2, max(data[1][1]) + 0.2, max(data[2][1]) + 0.2)
    axs[0].set_ylim(min_lim, max_lim)
    axs[1].set_ylim(min_lim, max_lim)
    axs[2].set_ylim(min_lim, max_lim)

    # set font sizes for axes
    x_font_size = 6
    y_font_size = 7
    x_font_rotation = 60
    for i in range(3):
        axs[i].tick_params(axis='x', labelsize=x_font_size, rotation=x_font_rotation)
        axs[i].tick_params(axis='y', labelsize=y_font_size)

    # set subplots positions
    plt.subplots_adjust(left=0.08, bottom=0.15, right=0.8, top=0.85)
    plt.legend(bbox_to_anchor=(1.8, 0.5), loc='center right', borderaxespad=0., fontsize=10)

    plt.show()
