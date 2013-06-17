# coding: utf-8


# Dict of month names in Persian, supplied as a convenience
# Key is month number, value is tuple of possible spellings
# TODO: add more spelling variations (if appropriate)
persian_months = {
  1: (u'فروردین',),
  2: (u'اردیبهشت',),
  3: (u'خرداد',),
  4: (u'تیر',),
  5: (u'مرداد',),
  6: (u'شهریور',),
  7: (u'مهر',),
  8: (u'آبان',),
  9: (u'آذر',),
  10: (u'دی',),
  11: (u'بهمن',),
  12: (u'اسفند',),
}

def parse(datestring):
  """
  Parse a short string as a hijiri date. We have no guarantees on whether there
  will be redundant information in there (extra punctuation etc) but we should
  cover the most obvious cases first.

  See http://en.wikipedia.org/wiki/Solar_Hijri_calendar for a description of the
  Hijiri solar calendar.

  This does not yet handle the Hijiri lunar calendar.

  Args:
    `datestring`: string that we think represents a valid date
  Returns:
    3-tuple of date in valid hijiri format `(year, month, day)`
    where year, month and day are all integers.
  """
  raise NotImplementedError()

def convert_to_gregorian(datetuple, calendar='solar'):
  """
  Converts a hijiri date in the format `(year, month, day)` to
  Gregorian format.
  Args:
    `datetuple` - 3-tuple hijiri date
    `calendar` - `solar` or `lunar` depending on whether we are using the Persian solar
    or Arab (?) lunar calendar to calculate date
  Returns:
    3-tuple of date in Gregorian format
  """
  if calendar == 'solar':
    return convert_solar_to_gregorian(datetuple)
  elif calendar == 'lunar':
    return convert_lunar_to_gregorian(datetuple)
  else:
    raise ValueError('Invalid calendar specified')

def convert_solar_to_gregorian(datetuple):
  raise NotImplementedError()

def convert_lunar_to_gregorian(datetuple):
  raise NotImplementedError()
