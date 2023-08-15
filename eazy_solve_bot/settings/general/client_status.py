from enum import Enum
class ClientStatusEnum(Enum):
    NONE = "NONE" # Не является пользователем
    BAN = "BAN"  # Заказчик забанен
    BAD = "BAD"  # Проблемный заказчик ()
    NEW = "NEW"  # Новый заказчик (1-2 заказа или общая сумма не > 2x)
    SILVER = "SILVER"  # Статус серебро (2-5 заказов или общая сумма не > 5x)
    GOLD = "GOLD"  # Статус золото (5-10 заказов или общая сумма не >10x)
    PLATINUM = "PLATINUM"  # Статус платина (10+ заказов или общая сумма >10x)
    VIP = "VIP"  # Статус vip для заказчика


CLIENT_STATUS = {"NONE": ClientStatusEnum.NONE,
                "BAN": ClientStatusEnum.BAN,
                "BAD": ClientStatusEnum.BAD,
                "NEW": ClientStatusEnum.NEW,
                "SILVER": ClientStatusEnum.SILVER,
                "GOLD": ClientStatusEnum.GOLD,
                "PLATINUM": ClientStatusEnum.PLATINUM,
                "VIP": ClientStatusEnum.VIP}