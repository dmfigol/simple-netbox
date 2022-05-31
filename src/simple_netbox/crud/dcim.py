from typing import TYPE_CHECKING
from simple_netbox.crud.base import BaseCRUD, CRUD, AsyncCRUD, CRUDAttrs
from simple_netbox.models.dcim.site import (
    SiteCreate,
    SiteRetrieve,
    SiteUpdate,
)

if TYPE_CHECKING:
    from simple_netbox.netbox import NetBox, AsyncNetBox


class SitesCRUDAttrs(CRUDAttrs[SiteCreate, SiteUpdate, SiteRetrieve]):
    endpoint = "/dcim/sites"
    create_model = SiteCreate
    update_model = SiteUpdate
    retrieve_model = SiteRetrieve


class SitesCRUD(CRUD[SiteCreate, SiteUpdate, SiteRetrieve]):
    attrs = SitesCRUDAttrs


class AsyncSitesCRUD(AsyncCRUD[SiteCreate, SiteUpdate, SiteRetrieve]):
    attrs = SitesCRUDAttrs


class DCIM:
    def __init__(self, netbox: "NetBox") -> None:
        self.sites = SitesCRUD(netbox=netbox)


class AsyncDCIM:
    def __init__(self, netbox: "AsyncNetBox") -> None:
        self.sites = AsyncSitesCRUD(netbox=netbox)
