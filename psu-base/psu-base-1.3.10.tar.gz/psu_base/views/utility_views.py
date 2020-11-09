# utility_views.py
#
#   These are views that are used for common tasks
#

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from psu_base.classes.Log import Log
from psu_base.classes.ConvenientDate import ConvenientDate
from psu_base.classes.DynamicRole import DynamicRole
from datetime import date
from psu_base.services import error_service

log = Log()
allowable_role_list = DynamicRole().super_user()


def validate_date_format(request):
    """
    Given a date input, validate the date format and return in standard format, or Forbidden if invalid

    Params:
        date_string:    The date entered by the user

        Optional:
            response_type:  { date, datetime } (defaults to 'date')
            min_years:      Minimum acceptable age of given date in years
            max_years:      Maximum acceptable age of given date in years
            min_days:      Minimum acceptable age of given date in days
            max_days:      Maximum acceptable age of given date in days
    """
    date_string = request.GET.get('date_string')
    log.trace([date_string])

    data = {
        'given': date_string,
        'converted_date': None,
        'converted_datetime': None,
        'age_days': None,
        'age_years': None,
        'error_message': None
    }

    try:
        if not date_string:
            data['error_message'] = "No date was given"
            response = JsonResponse(data)
            response.status_code = 403
            return response

        else:
            date_cd = ConvenientDate(date_string)

            if date_cd.conversion_error:
                data['error_message'] = date_cd.conversion_error
                response = JsonResponse(data)
                response.status_code = 403
                return response

            elif not date_cd.datetime_instance:
                data['error_message'] = "Could not recognize the given date format"
                response = JsonResponse(data)
                response.status_code = 403
                return response

            # Convert to standard date and datetime strings
            data['converted_date'] = date_cd.date_field()
            data['converted_datetime'] = date_cd.timestamp()

            # Prepare to calculate age
            given_datetime = date_cd.datetime_instance
            given_date = date(given_datetime.year, given_datetime.month, given_datetime.day)
            today = date.today()

            # Get age in years (negative age indicates future date)
            age = today.year - given_date.year - ((today.month, today.day) < (given_date.month, given_date.day))
            data['age_years'] = age

            # Get age in days (negative age indicates future date)
            delta = today - given_date
            data['age_days'] = delta.days

            return JsonResponse(data)

    except Exception as ee:
        data['error_message'] = f"Invalid date: {date_string}"
        response = JsonResponse(data)
        response.status_code = 403
        return response
