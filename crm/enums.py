from base.enums import Enum


class EntityType(Enum):
    # ev
    SOLE_TRADE = 'ST'
    # ec
    SOLE_VENTURE = 'SV'
    # bt
    LIMITED_PARTNERSHIP = 'LP'
    # kkt
    GENERAL_PARTNERSHIP = 'GP'
    # kht
    LIMITED_LIABILITY_COMPANY = 'LLC'
    # kv
    COMMUNITY_INTEREST_COMPANY = 'CIC'
    # rt
    JOINT_VENTURE = 'JV'
    # nyrt
    JOINT_STOCK_COMPANY = 'JSC'
    # zrt
    PUBLIC_LIMITED_COMPANY = 'PLC'

    _CHOICES = (
        (SOLE_TRADE, 'Sole trade'),
        (SOLE_VENTURE, 'Sole venture'),
        (LIMITED_PARTNERSHIP, 'Limited partnership'),
        (GENERAL_PARTNERSHIP, 'General partnership'),
        (LIMITED_LIABILITY_COMPANY, 'Limited liability company'),
        (COMMUNITY_INTEREST_COMPANY, 'Community interest company'),
        (JOINT_VENTURE, 'Joint venture'),
        (JOINT_STOCK_COMPANY, 'Joint stock company'),
        (PUBLIC_LIMITED_COMPANY, 'Public limited company')
    )


class Gender(Enum):
    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'
    OTHER = 'O'

    _CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNKNOWN, 'Unknown'),
        (OTHER, 'Other')
    )


class FamilyStatus(Enum):
    MARREID = 'M'
    SINGLE = 'S'
    WIDOW = 'W'
    PARTNER = 'P'
    DIVORCED = 'D'

    _CHOICES = (
        (MARREID, 'Married'),
        (SINGLE, 'Single'),
        (WIDOW, 'Widow'),
        (PARTNER, 'Partner'),
        (DIVORCED, 'Divorced')
    )


class EducationLevel(Enum):
    ELEMENTERY = 'E'
    VOCATIONAL = 'V'
    HIGH = 'H'
    DEGREE = 'D'
    MASTER_DEGREE = 'MD'
    DOCTORAL_DEGREE = 'DD'
    PROFESSIONAL_DEGREE = 'PD'


    _CHOICES = (
        (ELEMENTERY, 'Elementery'),
        (VOCATIONAL, 'Vocational'),
        (HIGH, 'High'),
        (DEGREE, 'Degree'),
        (MASTER_DEGREE, 'Master degree'),
        (DOCTORAL_DEGREE, 'Doctoral degree'),
        (PROFESSIONAL_DEGREE, 'Professional degree')
    )
