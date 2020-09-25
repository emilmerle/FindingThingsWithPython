"""
A dictionary of country specific regular expressions for finding
phone numbers.
"""

countryDict = {
    'germany': r'''(
    (\d{3}|\(\d{3}\))? # area code (optional)
    (\s|-|\.|/)? # separator (optional)
    (\d{7,9}) # 7 to 9 digits
    )'''
}
