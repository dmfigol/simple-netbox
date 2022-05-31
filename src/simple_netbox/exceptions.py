class NetBoxError(Exception):
    pass


class NetBoxHTTPError(NetBoxError):
    pass


class NetBoxHTTPClientError(NetBoxHTTPError):
    pass


class NetBoxHTTPServerError(NetBoxHTTPError):
    pass
