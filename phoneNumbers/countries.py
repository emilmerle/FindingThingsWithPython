"""
A dictionary of country specific regular expressions for finding
phone numbers.
"""

countryDict = {
    'canada': r'''
    ((\+?1)?) # country code
    (\s|-|\.)? # separator
    (\([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]\))? # area code
    ([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])? # area code w/o  parens
    (\s|-|\.)? # separator
    ([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2}) # first three
    (\s|-|\.)? # separator
    (\d{4}) # last four (required)
    ''',
    'germany': r'''(
    (\d{3}|\(\d{3}\))? # area code (optional)
    (\s|-|\.|/)? # separator (optional)
    (\d{7,9}) # 7 to 9 digits
    )'''
}

countryDict['usa'] = countryDict.get('canada')
