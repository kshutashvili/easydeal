from config.models import SiteConfiguration

config = SiteConfiguration.get_solo()


def get_price_currency(price, currency):
    if currency == 'USD':
        result_price = price * config.usd_rate
    elif currency == 'EUR':
        result_price = price * config.euro_rate
    elif currency == 'RUB':
        result_price = price * config.rub_rate
    else:
        result_price = price
    return result_price


def get_price_thb(price, currency):
    if currency == 'USD':
        result_price = float(price) / float(config.usd_rate)
    elif currency == 'EUR':
        result_price = float(price) / float(config.euro_rate)
    elif currency == 'RUB':
        result_price = float(price) / float(config.rub_rate)
    else:
        result_price = price
    return result_price
