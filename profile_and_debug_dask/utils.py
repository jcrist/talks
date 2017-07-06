import bokeh.plotting as bp


def plot_by_month(by_month):
    bp.output_file('by_month.html')

    fig = bp.figure(title='Flights Per Month', x_axis_label='Time',
                    y_axis_label='Flights', x_axis_type='datetime')
    fig.line(by_month.index, by_month.EWR, legend='EWR', color='red')
    fig.line(by_month.index, by_month.JFK, legend='JFK', color='blue')
    fig.line(by_month.index, by_month.LGA, legend='LGA', color='green')

    bp.show(fig)
