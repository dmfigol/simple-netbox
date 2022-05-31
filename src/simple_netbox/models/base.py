import pydantic


class Model(pydantic.BaseModel):
    class Config:
        orm_mode = True


class CRUDModel(Model):
    pass

    @property
    def _id(self) -> int:
        return getattr(self, "id")
