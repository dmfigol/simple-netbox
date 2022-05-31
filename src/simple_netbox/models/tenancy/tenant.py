from datetime import datetime, date
from typing import Optional, Dict, Any

from pydantic import Field, AnyUrl, constr

from simple_netbox.models.base import Model, CRUDModel


class BaseTenant(CRUDModel):
    name: constr(min_length=1, max_length=100) = Field(..., title="Name")
    slug: constr(regex=r"^[-a-zA-Z0-9_]+$", min_length=1, max_length=100) = Field(
        ..., title="Slug"
    )


class TenantRetrieve(BaseTenant):
    id: Optional[int] = Field(None, title="Id")
    url: Optional[AnyUrl] = Field(None, title="Url")
    display: Optional[str] = Field(None, title="Display")
    # name: constr(min_length=1, max_length=100) = Field(..., title='Name')
    # slug: constr(regex=r'^[-a-zA-Z0-9_]+$', min_length=1, max_length=100) = Field(
    #     ..., title='Slug'
    # )
    # group: Optional[NestedTenantGroup] = None
    description: Optional[constr(max_length=200)] = Field(None, title="Description")
    comments: Optional[str] = Field(None, title="Comments")
    # tags: Optional[List[NestedTag]] = None
    custom_fields: Optional[Dict[str, Any]] = Field({}, title="Custom fields")
    created: Optional[date] = Field(None, title="Created")
    last_updated: Optional[datetime] = Field(None, title="Last updated")
    circuit_count: Optional[int] = Field(None, title="Circuit count")
    device_count: Optional[int] = Field(None, title="Device count")
    ipaddress_count: Optional[int] = Field(None, title="Ipaddress count")
    prefix_count: Optional[int] = Field(None, title="Prefix count")
    rack_count: Optional[int] = Field(None, title="Rack count")
    site_count: Optional[int] = Field(None, title="Site count")
    virtualmachine_count: Optional[int] = Field(None, title="Virtualmachine count")
    vlan_count: Optional[int] = Field(None, title="Vlan count")
    vrf_count: Optional[int] = Field(None, title="Vrf count")
    cluster_count: Optional[int] = Field(None, title="Cluster count")


class TenantCreate(BaseTenant):
    pass


class TenantUpdate(BaseTenant):
    id: int


Tenant = TenantCreate
