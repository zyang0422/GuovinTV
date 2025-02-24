from typing import TypedDict, Literal, Union

OriginType = Literal["local", "whitelist", "subscribe", "hotel", "multicast", "online_search"]
IPvType = Literal["ipv4", "ipv6", None]


class ChannelData(TypedDict):
    """
    Channel data types, including url, date, resolution, origin and ipv_type
    """
    url: str
    date: str | None
    resolution: str | None
    origin: OriginType
    ipv_type: IPvType


CategoryChannelData = dict[str, dict[str, list[ChannelData]]]


class TestResult(TypedDict):
    """
    Test result types, including speed, delay, resolution
    """
    speed: int | float | None
    delay: int | float | None
    resolution: str | None


TestResultCacheData = dict[str, list[TestResult]]

ChannelTestResult = Union[ChannelData, TestResult]
