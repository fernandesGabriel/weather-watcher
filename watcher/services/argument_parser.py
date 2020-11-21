import argparse

allowed_days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']


def get_forecast_params():
    parser = argparse.ArgumentParser()

    location = parser.add_mutually_exclusive_group(required=True)
    location.add_argument('--location-name', type=str, dest='location_name', help='Watch by location name')
    location.add_argument('--location-xyz', type=dict, dest='location_xyz', help='Watch by location coordinates')

    parser.add_argument('--day', '-d', type=str, dest='days', choices=allowed_days, action='append', help='Watch day')

    return parser.parse_args()