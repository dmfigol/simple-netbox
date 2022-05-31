from typing import TYPE_CHECKING
from simple_netbox.crud.base import BaseCRUD, CRUD, AsyncCRUD, CRUDAttrs
from simple_netbox.models.tenancy.tenant import (
    TenantCreate,
    TenantRetrieve,
    TenantUpdate,
)

if TYPE_CHECKING:
    from simple_netbox.netbox import NetBox, AsyncNetBox


class TenantCRUDAttrs(CRUDAttrs[TenantCreate, TenantUpdate, TenantRetrieve]):
    endpoint = "/tenancy/tenants"
    create_model = TenantCreate
    update_model = TenantUpdate
    retrieve_model = TenantRetrieve


class TenantCRUD(CRUD[TenantCreate, TenantUpdate, TenantRetrieve]):
    attrs = TenantCRUDAttrs


class AsyncTenantCRUD(AsyncCRUD[TenantCreate, TenantUpdate, TenantRetrieve]):
    attrs = TenantCRUDAttrs


class Tenancy:
    def __init__(self, netbox: "NetBox") -> None:
        self.tenants = TenantCRUD(netbox=netbox)


class AsyncTenancy:
    def __init__(self, netbox: "AsyncNetBox") -> None:
        self.tenants = AsyncTenantCRUD(netbox=netbox)
