from typing import TYPE_CHECKING, TypeVar, Generic, Type, cast, Optional, List, Any

from pydantic import parse_obj_as

if TYPE_CHECKING:
    from simple_netbox.models.base import CRUDModel
    from simple_netbox.netbox import NetBox, AsyncNetBox

TCreate = TypeVar("TCreate", bound="CRUDModel")
TUpdate = TypeVar("TUpdate", bound="CRUDModel")
TRetrieve = TypeVar("TRetrieve", bound="CRUDModel")


class CRUDAttrs(Generic[TCreate, TUpdate, TRetrieve]):
    endpoint: str
    create_model: Type[TCreate] = cast(Type[TCreate], "CRUDModel")
    update_model: Type[TUpdate] = cast(Type[TUpdate], "CRUDModel")
    retrieve_model: Type[TRetrieve] = cast(Type[TRetrieve], "CRUDModel")
    delete_endpoint = "{endpoint}/{id}/"
    create_endpoint = "{endpoint}/"
    update_endpoint = "{endpoint}/{id}/"
    get_endpoint = "{endpoint}/{id}/"
    get_all_endpoint = "{endpoint}/"


class BaseCRUD(CRUDAttrs[TCreate, TUpdate, TRetrieve]):
    pass


class CRUD(BaseCRUD[TCreate, TUpdate, TRetrieve]):
    attrs = CRUDAttrs

    def __init__(self, netbox: "NetBox") -> None:
        self.netbox = netbox

    # def create(self, obj: T) -> T:
    #     pass

    # def update(self, obj: T) -> T:
    #     pass

    # def get(self, id: Optional[int] = None, name: Optional[str] = None) -> T:
    #     pass

    # def list(self) -> List[TRetrieve]:
    #     url = self.attrs.get_all_endpoint.format(endpoint=self.attrs.endpoint)
    #     response = self.netbox.http_client.get(url)
    #     pass

    def delete(self, id: int) -> None:
        url = self.attrs.delete_endpoint.format(endpoint=self.attrs.endpoint, id=id)
        response = self.netbox.http_client.delete(url)
        response.raise_for_status()
        return None


class AsyncCRUD(BaseCRUD[TCreate, TUpdate, TRetrieve]):
    attrs = CRUDAttrs

    def __init__(self, netbox: "AsyncNetBox") -> None:
        self.netbox = netbox

    async def create(self, obj: TCreate) -> TRetrieve:
        url = self.attrs.create_endpoint.format(endpoint=self.attrs.endpoint)
        response = await self.netbox.http_client.post(url, json=obj.dict())
        response.raise_for_status()
        result = self.attrs.retrieve_model(**response.json())
        return result

    async def update(self, obj: Any) -> TRetrieve:
        _obj = self.attrs.update_model.from_orm(obj)
        url = self.attrs.update_endpoint.format(endpoint=self.attrs.endpoint, id=obj.id)
        response = await self.netbox.http_client.put(url, json=_obj.dict())
        response.raise_for_status()
        result = self.attrs.retrieve_model(**response.json())
        return result

    async def list(self) -> List[TRetrieve]:
        url = self.attrs.get_all_endpoint.format(endpoint=self.attrs.endpoint)
        response = await self.netbox.http_client.get(url)
        response.raise_for_status()
        data = response.json().get("results", [])
        result = parse_obj_as(List[self.attrs.retrieve_model], data)
        return result

    async def delete(
        self, id: Optional[int] = None, name: Optional[str] = None
    ) -> None:
        url = self.attrs.delete_endpoint.format(endpoint=self.attrs.endpoint, id=id)
        response = await self.netbox.http_client.delete(url)
        response.raise_for_status()
        return None
