from datetime import datetime
from yr.libyr import Yr

from watcher.watcher import Watcher
from watcher.services.argument_parser import get_forecast_params
from watcher.services.date_searcher import get_next_date_from_weekday


class LocationForecast(Watcher):

    def __init__(self):
        self.__params = get_forecast_params()

    def run(self):
        arguments = dict()

        if self.__params.location_xyz is not None:
            arguments['location_xyz'] = self.__params.location_name
        elif self.__params.location_name is not None:
            arguments['location_name'] = self.__params.location_name
        else:
            raise Exception('Location must be defined')

        weather = Yr(**arguments)
        search_day = self.get_searched_days()

        for forecast in weather.forecast():
            if datetime.fromisoformat(forecast['@from']).date() in search_day:
                # todo: report expected weather
                print(forecast)

    def get_searched_days(self):
        searched_days = list()
        for day_abbr in self.__params.days:
            searched_days.append(get_next_date_from_weekday(day_abbr))

        return searched_days


if __name__ == "__main__":
    watcher = LocationForecast()
    watcher.run()
