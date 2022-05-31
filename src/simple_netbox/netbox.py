from types import TracebackType
from typing import Optional, Type, TYPE_CHECKING, Any, Dict

from httpx import Client, AsyncClient

from simple_netbox.crud.dcim import DCIM, AsyncDCIM
from simple_netbox.crud.tenancy import Tenancy, AsyncTenancy

if TYPE_CHECKING:
    from httpx._types import VerifyTypes


class Base:
    def __init__(self, host: str, token: str) -> None:
        self.host = host
        self.token = token

    @property
    def headers(self) -> Dict[str, Any]:
        headers = {
            "Authorization": f"Token {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        return headers

    @property
    def api_base_url(self) -> str:
        return f"{self.host}/api"


class NetBox(Base):
    def __init__(self, host: str, token: str, verify: "VerifyTypes" = True) -> None:
        super().__init__(host=host, token=token)
        self.http_client = Client(
            headers=self.headers,
            base_url=self.api_base_url,
            verify=verify,
        )
        self.tenancy = Tenancy(netbox=self)
        self.dcim = DCIM(netbox=self)

    def __enter__(self) -> "NetBox":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        self.http_client.__exit__(exc_type, exc_value, traceback)
        return None


class AsyncNetBox(Base):
    def __init__(self, host: str, token: str, verify: "VerifyTypes" = True) -> None:
        super().__init__(host=host, token=token)
        self.http_client = AsyncClient(
            headers=self.headers,
            base_url=self.api_base_url,
            verify=verify,
        )
        self.tenancy = AsyncTenancy(netbox=self)
        self.dcim = AsyncDCIM(netbox=self)

    async def __aenter__(self) -> "AsyncNetBox":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        await self.http_client.__aexit__(exc_type, exc_value, traceback)
        return None
