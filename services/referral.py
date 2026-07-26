# services/referral.py

"""
Работа с реферальной ссылкой.

Вся ссылка хранится только в .env
через переменную:

REFERRAL_URL=https://...

Никаких ссылок в коде нет.
"""


from config import REFERRAL_URL



def get_referral_link() -> str:
    """
    Возвращает реферальную ссылку магазина.
    """

    return REFERRAL_URL