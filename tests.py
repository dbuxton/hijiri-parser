# coding: utf-8

import unittest
from parser import parse, convert_to_gregorian


class ParserTest(unittest.TestCase):

  solar_hijiri_persian = (
    {
      'page': 'http://www.jamejamonline.ir/NewsPreview/1085298620231286444',
      'raw_date': u'تاریخ : دوشنبه 27 خرداد 1392 13:59',
      'hijiri_parsed': (1392, 3, 27),
      'gregorian_parsed': (2013, 6, 17),
    },
    {
      'page': 'http://resalat-news.com/Fa/?code=143723',
      'raw_date': u'1392/03/27',
      'hijiri_parsed': (1392, 3, 27),
      'gregorian_parsed': (2013, 6, 17),
    },
    {
      'page': 'http://www.jamejamonline.ir/NewsPreview/1084193085615226012',
      'raw_date': u'تاریخ : یکشنبه 26 خرداد 1392 15:35',
      'hijiri_parsed': (1392, 3, 26),
      'gregorian_parsed': (2013, 6, 16),
    },
  )

  arabic_numerals_solar_hijiri_persian = (
    {
      'page': 'http://siasatrooz.ir/vdcbf8bw.rhb89piuur.html',
      'raw_date': u'تاریخ انتشار : چهارشنبه ۱۸ ارديبهشت ۱۳۹۲ ساعت ۲۲:۵۱',
      'hijiri_parsed': (1392, 2, 18),
      'gregorian_parsed': (2013, 5, 8),
    },
    {
      'page': 'http://siasatrooz.ir/vdchmvn6.23nzkdftt2.html',
      'raw_date': u'تاریخ انتشار : چهارشنبه ۱۱ ارديبهشت ۱۳۹۲ ساعت ۲۰:۵۲',
      'hijiri_parsed': (1392, 2, 11),
      'gregorian_parsed': (2013, 5, 1),
    },
    {
      'page': 'http://siasatrooz.ir/vdchq-nq.23n-idftt2.html',
      'raw_date': u'تاریخ انتشار : چهارشنبه ۱۵ شهريور ۱۳۹۱ ساعت ۲۱:۵۰',
      'hijiri_parsed': (1391, 6, 15),
      'gregorian_parsed': (2012, 9, 5),
    },
    {
      'page': 'http://www.esfahanemrooz.ir/fa/news/34031/%D8%AF%D8%B1%D8%A8%D8%A7%D8%B1%D9%87-%D8%A7%D8%AB%D8%B1%D8%A7%D8%AA-%D8%AF%D8%B1%D9%85%D8%A7%D9%86%DB%8C-%DB%8C%D8%AE-%DA%86%D9%87-%D9%85%DB%8C-%D8%AF%D8%A7%D9%86%DB%8C%D8%AF.html',
      'raw_date': u'۱۳۹۲/۰۲/۳۰ - ۱۲:۴۹',
      'hijiri_parsed': (1392, 2, 30),
      'gregorian_parsed': (2013, 5, 20),
    },
    {
      'page': 'http://www.esfahanemrooz.ir/fa/news/33845/%D8%AA%D8%A7%DA%A9%D8%B3%DB%8C-%D9%87%D8%A7%DB%8C-%D8%A8%DB%8C-%D8%AE%DB%8C%D8%A7%D9%84%D8%8C-%D9%85%D8%B3%D8%A7%D9%81%D8%B1%D9%87%D8%A7%DB%8C-%D8%B3%D8%B1%DA%AF%D8%B1%D8%AF%D8%A7%D9%86.html',
      'raw_date': u'۱۳۹۲/۰۲/۲۵ - ۱۳:۱۹',
      'hijiri_parsed': (1392, 2, 25),
      'gregorian_parsed': (2013, 5, 15),
    },
  )

  def test_hijiri_persian_parse(self):
    for case in self.solar_hijiri_persian:
      hijiri = parse(case['raw_date'])
      self.assertEqual(case['hijiri_parsed'], hijiri, 'Expected %s for string "%s": got %s' % (case['hijiri_parsed'], case['raw_date'], hijiri))

  def test_arabic_numerals_parse(self):
    for case in self.arabic_numerals_solar_hijiri_persian:
      hijiri = parse(case['raw_date'])
      self.assertEqual(case['hijiri_parsed'], hijiri, 'Expected %s for string "%s": got %s' % (case['hijiri_parsed'], case['raw_date'], hijiri))

  def test_gregorian_conversian(self):
    for case in list(self.solar_hijiri_persian) + list(self.arabic_numerals_solar_hijiri_persian):
      gregorian = convert_to_gregorian(case['hijiri_parsed'])
      self.assertEqual(gregorian, case['gregorian_parsed'])

  def test_integration(self):
    for case in list(self.solar_hijiri_persian) + list(self.arabic_numerals_solar_hijiri_persian):
      gregorian = convert_to_gregorian(parse(case['raw_date']))
      self.assertEqual(gregorian, case['gregorian'], 'Got incorrect Gregorian date %s for raw input %s - should be %s' % (gregorian, case['raw_date'], case['gregorian']))

if __name__ == '__main__':
  unittest.main()