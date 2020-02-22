from enum import IntEnum

class AppointmentStatuses(IntEnum):
    PENDING = 1
    COMPLETED = 2
    CANCELLED = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
