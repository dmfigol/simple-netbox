import asyncio
import os

from simple_netbox import AsyncNetBox
from simple_netbox.models.tenancy.tenant import Tenant
import rich

NETBOX_HOST = os.environ["NETBOX_HOST"]
NETBOX_TOKEN = os.environ["NETBOX_TOKEN"]


async def main() -> None:
    async with AsyncNetBox(host=NETBOX_HOST, token=NETBOX_TOKEN, verify=False) as nb:
        # tenants = await nb.tenancy.tenants.list()
        # for tenant in tenants:
        #     if tenant.name.startswith("Test"):
        #         tenant.name += "TO DELETE"
        #         await nb.tenancy.tenants.update(tenant)

        # # tenant = Tenant(name="created from python sdk")
        # # await nb.tenancy.tenants.create(tenant)

        # tenants = await nb.tenancy.tenants.list()
        # print("tenants:")
        # for tenant in tenants:
        #     print(tenant.name)
        sites = await nb.dcim.sites.list()
        for site in sites:
            print(site.status)


if __name__ == "__main__":
    asyncio.run(main())
