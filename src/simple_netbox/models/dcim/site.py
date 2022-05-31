from datetime import datetime, date
from decimal import Decimal
from enum import Enum
from typing import Optional, Dict, Any


from pydantic import AnyUrl, BaseModel, EmailStr, Field, condecimal, conint, constr

from simple_netbox.models.base import Model, CRUDModel


class Label40(Enum):
    Planned = "Planned"
    Staging = "Staging"
    Active = "Active"
    Decommissioning = "Decommissioning"
    Retired = "Retired"


class Value40(Enum):
    planned = "planned"
    staging = "staging"
    active = "active"
    decommissioning = "decommissioning"
    retired = "retired"


class Status11(Model):
    label: Label40
    value: Value40


class SiteBase(CRUDModel):
    name: constr(min_length=1, max_length=100) = Field(..., title="Name")
    slug: constr(regex=r"^[-a-zA-Z0-9_]+$", min_length=1, max_length=100) = Field(
        ..., title="Slug"
    )
    status: Optional[Status11] = Field(None, title="Status")


class SiteRetrieve(SiteBase):
    id: Optional[int] = Field(None, title="Id")
    url: Optional[AnyUrl] = Field(None, title="Url")
    display: Optional[str] = Field(None, title="Display")
    # region: Optional[NestedRegion] = None
    # group: Optional[NestedSiteGroup] = None
    # tenant: Optional[NestedTenant] = None
    facility: Optional[constr(max_length=50)] = Field(
        None, description="Local facility ID or description", title="Facility"
    )
    asn: Optional[conint(ge=1, le=4294967295)] = Field(
        None, description="32-bit autonomous system number", title="ASN"
    )
    # asns: Optional[List[NestedASN]] = None
    time_zone: Optional[str] = Field(None, title="Time zone")
    description: Optional[constr(max_length=200)] = Field(None, title="Description")
    physical_address: Optional[constr(max_length=200)] = Field(
        None, title="Physical address"
    )
    shipping_address: Optional[constr(max_length=200)] = Field(
        None, title="Shipping address"
    )
    latitude: Optional[Decimal] = Field(
        None, description="GPS coordinate (latitude)", title="Latitude"
    )
    longitude: Optional[Decimal] = Field(
        None, description="GPS coordinate (longitude)", title="Longitude"
    )
    contact_name: Optional[constr(max_length=50)] = Field(None, title="Contact name")
    contact_phone: Optional[constr(max_length=20)] = Field(None, title="Contact phone")
    contact_email: Optional[str] = Field(None, title="Contact E-mail")
    comments: Optional[str] = Field(None, title="Comments")
    # tags: Optional[List[NestedTag]] = None
    custom_fields: Optional[Dict[str, Any]] = Field({}, title="Custom fields")
    created: Optional[date] = Field(None, title="Created")
    last_updated: Optional[datetime] = Field(None, title="Last updated")
    circuit_count: Optional[int] = Field(None, title="Circuit count")
    device_count: Optional[int] = Field(None, title="Device count")
    prefix_count: Optional[int] = Field(None, title="Prefix count")
    rack_count: Optional[int] = Field(None, title="Rack count")
    virtualmachine_count: Optional[int] = Field(None, title="Virtualmachine count")
    vlan_count: Optional[int] = Field(None, title="Vlan count")


class SiteCreate(SiteBase):
    pass


class SiteUpdate(SiteBase):
    id: int


Site = SiteCreate
