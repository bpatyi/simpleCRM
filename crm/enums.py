from enum import (
    Enum,
    unique
)


@unique
class EntityType(Enum):
    # ev
    sole_trade = 'Sole Trade'
    # ec
    sole_venture = 'Sole Venture'
    # bt
    limited_partnership = 'Limited Partnership'
    # kkt
    general_partnership = 'General Partnership'
    # kht
    limited_liability_company = 'Limited Liabiltity Company'
    # kv
    community_interest_company = 'Community Interest Company'
    # rt
    joint_venture = 'Joint Venture'
    # nyrt
    joint_stock_company = 'Joint Stock Company'
    # zrt
    public_limited_company = 'Public Limited Company'


@unique
class CompanyType(Enum):
    user = 1
    contact = 2