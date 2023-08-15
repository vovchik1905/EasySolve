from enum import IntEnum


class SolverStatusEnum(IntEnum):
    NONE = 0 # Не является исполнителем
    BAN = 1 # Решатель забанен
    BAD = 2 # Проблемнырешатель
    NEW = 3 # Новый решатель
    SILVER = 4  # Статус серебро (2-5 заказов или общая сумма не > 5x)
    GOLD = 5  # Статус золото (5-10 заказов или общая сумма не >10x)
    PLATINUM = 6  # Статус платина (10+ заказов или общая сумма >10x)
    VIP = 7  # Статус vip для решателя


SOLVER_STATUS = {"NONE": SolverStatusEnum.NONE,
                "BAN": SolverStatusEnum.BAN,
                "BAD": SolverStatusEnum.BAD,
                "NEW": SolverStatusEnum.NEW,
                "SILVER": SolverStatusEnum.SILVER,
                "GOLD": SolverStatusEnum.GOLD,
                "PLATINUM": SolverStatusEnum.PLATINUM,
                "VIP": SolverStatusEnum.VIP}