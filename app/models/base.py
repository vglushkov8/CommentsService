from pydantic import BaseModel


class BaseOrmModel(BaseModel):

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, obj):
        if hasattr(obj, 'id'):
            obj.id = str(obj.id)
        return super().from_orm(obj)