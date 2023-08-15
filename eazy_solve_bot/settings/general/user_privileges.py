from enum import IntEnum


class UserPrivileges(IntEnum):
    CLIENT = 1
    CLIENT_AND_SOLVER = 2
    PARTNER = 3
    ADMIN = 4
    ACCOUNTANT = 5
    CREATOR = 6


USER_PRIVILEGES = {"CLIENT": UserPrivileges.CLIENT,
                    "CLIENT_AND_SOLVER": UserPrivileges.CLIENT_AND_SOLVER,
                    "PARTNER": UserPrivileges.PARTNER,
                    "ADMIN": UserPrivileges.ADMIN,
                    "ACCOUNTANT": UserPrivileges.ACCOUNTANT,
                    "CREATOR": UserPrivileges.CREATOR}


INT_TO_USER_PRIVILEGES = {1: UserPrivileges.CLIENT,
                            2: UserPrivileges.CLIENT_AND_SOLVER,
                            3: UserPrivileges.PARTNER,
                            4: UserPrivileges.ADMIN,
                            5: UserPrivileges.ACCOUNTANT,
                            6: UserPrivileges.CREATOR}