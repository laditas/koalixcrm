# -*- coding: utf-8 -*-

import pytz
from selenium.common.exceptions import NoSuchElementException


def assert_when_element_does_not_exist(testcase, xpath):
    try:
        testcase.selenium.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print(xpath+" does not exist")


def assert_when_element_exists(testcase, xpath):
    try:
        testcase.selenium.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return
    print(xpath+" does exist")


def make_date_utc(input_date):
    output_date = pytz.timezone("UTC").localize(input_date, is_dst=None)
    return output_date
