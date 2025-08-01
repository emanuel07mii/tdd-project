from pydantic import BaseModel


class BaseSchemaMixin(BaseModel):
    class ConfigDict:
        from_attributes = True
