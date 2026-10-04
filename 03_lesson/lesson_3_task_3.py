from address import Address
from mailing import Mailing

to_address = Address('460000', 'г.Оренбург', 'ул.Кирова', 'д.54', 'кв.8')
from_address = Address('462630', 'г.Гай', 'ул.Декабристов', 'д.13', 'кв.10')

mailing = Mailing(to_address, from_address, 545.50, 'N562277A55')

print(f'Отправление {mailing.track} из: '
      f'{mailing.from_address.index}, {mailing.from_address.city}, '
      f'{mailing.from_address.street}, '
      f'{mailing.from_address.house} - {mailing.from_address.apartment}'
      f' в: {mailing.to_address.index}, {mailing.to_address.city}, '
      f'{mailing.to_address.street}, '
      f'{mailing.to_address.house} - {mailing.to_address.apartment}.'
      f' Стоимость {mailing.cost} рублей.')
