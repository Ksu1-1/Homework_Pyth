from smartphone import Smartphone

catalog = [
    Smartphone('Samsung', 'Galaxy', '+79878981851'),
    Smartphone('Apple', 'Iphone 16', '+79554455882'),
    Smartphone('Honor', '600 Pro', '+79652854196'),
    Smartphone('Fly', 'Stratus', '+79854789632'),
    Smartphone('Xiaomi', 'HyperOS 3', '+79557711996')
]
for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')
