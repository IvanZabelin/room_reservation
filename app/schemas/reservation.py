from datetime import datetime
from pydantic import BaseModel, root_validator, validator


class ReservationBase(BaseModel):
    from_reserve: datetime
    to_reserve: datetime

    @root_validator
    def check_from_reserve_before_to_reserve(cls, values):
        from_reserve = values.get('from_reserve')
        to_reserve = values.get('to_reserve')
        if from_reserve and to_reserve and from_reserve >= to_reserve:
            raise ValueError(
                'Время начала бронирования должно быть меньше времени окончания.'
            )
        return values


class ReservationCreate(ReservationBase):
    meetingroom_id: int

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                'Время начала бронирования должно быть больше текущего времени.'
            )
        return value


class ReservationUpdate(BaseModel):
    from_reserve: datetime
    to_reserve: datetime


class ReservationDB(BaseModel):
    id: int
    meetingroom_id: int
    from_reserve: datetime
    to_reserve: datetime

    class Config:
        orm_mode = True

