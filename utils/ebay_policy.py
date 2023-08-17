DISPATCHTIMEMAX = {
    '00.0 ~ 00.5kg【EU含む】': '10',
    '00.5 ~ 01.0kg【EU含む】': '10',
    '01.0 ~ 01.5kg【EU含む】': '10',
    '01.5 ~ 02.0kg【EU含む】': '10',
    '02.0 ~ 02.5kg【EU含む】': '10',
    '02.5 ~ 03.0kg【EU含む】': '10',
    '03.0 ~ 03.5kg【EU含む】': '10',
    '03.5 ~ 04.0kg【EU含む】': '10',
    '04.0 ~ 04.5kg【EU含む】': '10',
    '【FedEx - DHL】00.0 ~ 00.5kg 【30days】【EU含む】': '5',
    '【FedEx - DHL】00.5 ~ 01.0kg 【5days】【EU含む】': '5',
    '【US・EU・Mx・Ca・Asia 送料無料】': '5',
    '【エコSAL】 5day': '5',
}

RETURN_POLICY = {
    'ReturnsAccepted, MoneyBack, Days_60, Seller': {
        'ReturnsAcceptedOption': 'ReturnsAccepted',
        'RefundOption': 'MoneyBack',
        'ReturnsWithinOption': 'Days_60',
        'ShippingCostPaidByOption': 'Seller',
        'InternationalReturnsAcceptedOption': 'ReturnsAccepted',
        'InternationalRefundOption': 'MoneyBack',
        'InternationalReturnsWithinOption': 'Days_60',
        'InternationalShippingCostPaidByOption': 'Seller'
    }
}

SHIPPING_POLICY = {
    '00.0 ~ 00.5kg【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'ExpeditedShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GN', 'GW', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'YT', 'NE', 'NG', 'SH', 'SN', 'SC', 'SL', 'SO', 'SZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW', 'AI', 'AG', 'AW', 'BS', 'BZ', 'VG', 'KY', 'DM', 'GD', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MS', 'AN', 'NI', 'PA', 'KN', 'LC', 'VC', 'TT', 'TC', 'VI', 'LA', 'MO', 'VN', 'RU', 'AD', 'BY', 'GG', 'JE', 'LI', 'MK', 'MC', 'SM', 'SJ', 'UA', 'VA', 'AF', 'BD', 'BT', 'JP', 'MN', 'NP', 'PK', 'TJ', 'TM', 'IQ', 'JO', 'YE', 'BM', 'GL', 'PM', 'AS', 'CK', 'FJ', 'GU', 'KI', 'MH', 'FM', 'NR', 'NU', 'PW', 'SB', 'TO', 'TV', 'VU', 'WF', 'WS', 'FK', 'GF', 'GY', 'SR', 'VE', 'PO Box'],
        'RateTableDetails': {
            'InternationalRateTableId': '5190864010'
        },
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['CA', 'MX'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'GB', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '2.0',
                'ShippingServicePriority': '2',
            },
            {
                'ShipToLocation': ['Asia', 'CN'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '2.0',
                'ShippingServicePriority': '3',
            },
            {
                'ShipToLocation': ['Americas', 'BR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '19.0',
                'ShippingServicePriority': '4',
            },
            {
                'ShipToLocation': 'Worldwide',
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '12.0',
                'ShippingServicePriority': '5',
            }
        ],
    },

    '00.5 ~ 01.0kg【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'ExpeditedShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GN', 'GW', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'YT', 'NE', 'NG', 'SH', 'SN', 'SC', 'SL', 'SO', 'SZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW', 'AI', 'AG', 'AW', 'BS', 'BZ', 'VG', 'KY', 'DM', 'GD', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MS', 'AN', 'NI', 'PA', 'KN', 'LC', 'VC', 'TT', 'TC', 'VI', 'LA', 'MO', 'VN', 'RU', 'AD', 'BY', 'GG', 'JE', 'LI', 'MK', 'MC', 'SM', 'SJ', 'UA', 'VA', 'AF', 'BD', 'BT', 'JP', 'MN', 'NP', 'PK', 'TJ', 'TM', 'IQ', 'JO', 'YE', 'BM', 'GL', 'PM', 'AS', 'CK', 'FJ', 'GU', 'KI', 'MH', 'FM', 'NR', 'NU', 'PW', 'SB', 'TO', 'TV', 'VU', 'WF', 'WS', 'FK', 'GF', 'GY', 'SR', 'VE', 'PO Box'],
        'RateTableDetails': {
            'InternationalRateTableId': '5190864010'
        },
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['CA', 'MX'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'GB', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '2.0',
                'ShippingServicePriority': '2',
            },
            {
                'ShipToLocation': ['Asia', 'CN'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '2.0',
                'ShippingServicePriority': '3',
            },
            {
                'ShipToLocation': ['Americas', 'BR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '23.0',
                'ShippingServicePriority': '4',
            },
            {
                'ShipToLocation': 'Worldwide',
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '13.0',
                'ShippingServicePriority': '5',
            }
        ],
    },

    '01.0 ~ 01.5kg【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'ExpeditedShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GN', 'GW', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'YT', 'NE', 'NG', 'SH', 'SN', 'SC', 'SL', 'SO', 'SZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW', 'AI', 'AG', 'AW', 'BS', 'BZ', 'VG', 'KY', 'DM', 'GD', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MS', 'AN', 'NI', 'PA', 'KN', 'LC', 'VC', 'TT', 'TC', 'VI', 'LA', 'MO', 'VN', 'RU', 'AD', 'BY', 'GG', 'JE', 'LI', 'MK', 'MC', 'SM', 'SJ', 'UA', 'VA', 'AF', 'BD', 'BT', 'JP', 'MN', 'NP', 'PK', 'TJ', 'TM', 'IQ', 'JO', 'YE', 'BM', 'GL', 'PM', 'AS', 'CK', 'FJ', 'GU', 'KI', 'MH', 'FM', 'NR', 'NU', 'PW', 'SB', 'TO', 'TV', 'VU', 'WF', 'WS', 'FK', 'GF', 'GY', 'SR', 'VE', 'PO Box'],
        'RateTableDetails': {
            'InternationalRateTableId': '5190864010'
        },
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['CA', 'MX'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'GB', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '4.0',
                'ShippingServicePriority': '2',
            },
            {
                'ShipToLocation': ['Asia', 'CN'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '2.0',
                'ShippingServicePriority': '3',
            },
            {
                'ShipToLocation': ['Americas', 'BR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '33.0',
                'ShippingServicePriority': '4',
            },
            {
                'ShipToLocation': 'Worldwide',
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '20.0',
                'ShippingServicePriority': '5',
            }
        ],
    },
    
    '01.5 ~ 02.0kg【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'ExpeditedShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GN', 'GW', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'YT', 'NE', 'NG', 'SH', 'SN', 'SC', 'SL', 'SO', 'SZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW', 'AI', 'AG', 'AW', 'BS', 'BZ', 'VG', 'KY', 'DM', 'GD', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MS', 'AN', 'NI', 'PA', 'KN', 'LC', 'VC', 'TT', 'TC', 'VI', 'LA', 'MO', 'VN', 'RU', 'AD', 'BY', 'GG', 'JE', 'LI', 'MK', 'MC', 'SM', 'SJ', 'UA', 'VA', 'AF', 'BD', 'BT', 'JP', 'MN', 'NP', 'PK', 'TJ', 'TM', 'IQ', 'JO', 'YE', 'BM', 'GL', 'PM', 'AS', 'CK', 'FJ', 'GU', 'KI', 'MH', 'FM', 'NR', 'NU', 'PW', 'SB', 'TO', 'TV', 'VU', 'WF', 'WS', 'FK', 'GF', 'GY', 'SR', 'VE', 'PO Box'],
        'RateTableDetails': {
            'InternationalRateTableId': '5190864010'
        },
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['CA', 'MX'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'GB', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '6.0',
                'ShippingServicePriority': '2',
            },
            {
                'ShipToLocation': ['Asia', 'CN'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '6.0',
                'ShippingServicePriority': '3',
            },
            {
                'ShipToLocation': ['Americas', 'BR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '44.0',
                'ShippingServicePriority': '4',
            },
            {
                'ShipToLocation': 'Worldwide',
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '27.0',
                'ShippingServicePriority': '5',
            }
        ],
    },
    
    '02.0 ~ 02.5kg【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'ExpeditedShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GN', 'GW', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'YT', 'NE', 'NG', 'SH', 'SN', 'SC', 'SL', 'SO', 'SZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW', 'AI', 'AG', 'AW', 'BS', 'BZ', 'VG', 'KY', 'DM', 'GD', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MS', 'AN', 'NI', 'PA', 'KN', 'LC', 'VC', 'TT', 'TC', 'VI', 'LA', 'MO', 'VN', 'RU', 'AD', 'BY', 'GG', 'JE', 'LI', 'MK', 'MC', 'SM', 'SJ', 'UA', 'VA', 'AF', 'BD', 'BT', 'JP', 'MN', 'NP', 'PK', 'TJ', 'TM', 'IQ', 'JO', 'YE', 'BM', 'GL', 'PM', 'AS', 'CK', 'FJ', 'GU', 'KI', 'MH', 'FM', 'NR', 'NU', 'PW', 'SB', 'TO', 'TV', 'VU', 'WF', 'WS', 'FK', 'GF', 'GY', 'SR', 'VE', 'PO Box'],
        'RateTableDetails': {
            'InternationalRateTableId': '5190864010'
        },
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['CA', 'MX'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'GB', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '8.0',
                'ShippingServicePriority': '2',
            },
            {
                'ShipToLocation': ['Asia', 'CN'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '6.0',
                'ShippingServicePriority': '3',
            },
            {
                'ShipToLocation': ['Americas', 'BR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '52.0',
                'ShippingServicePriority': '4',
            },
            {
                'ShipToLocation': 'Worldwide',
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '33.0',
                'ShippingServicePriority': '5',
            }
        ],
    },
    
    '02.5 ~ 03.0kg【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'ExpeditedShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GN', 'GW', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'YT', 'NE', 'NG', 'SH', 'SN', 'SC', 'SL', 'SO', 'SZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW', 'AI', 'AG', 'AW', 'BS', 'BZ', 'VG', 'KY', 'DM', 'GD', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MS', 'AN', 'NI', 'PA', 'KN', 'LC', 'VC', 'TT', 'TC', 'VI', 'LA', 'MO', 'VN', 'RU', 'AD', 'BY', 'GG', 'JE', 'LI', 'MK', 'MC', 'SM', 'SJ', 'UA', 'VA', 'AF', 'BD', 'BT', 'JP', 'MN', 'NP', 'PK', 'TJ', 'TM', 'IQ', 'JO', 'YE', 'BM', 'GL', 'PM', 'AS', 'CK', 'FJ', 'GU', 'KI', 'MH', 'FM', 'NR', 'NU', 'PW', 'SB', 'TO', 'TV', 'VU', 'WF', 'WS', 'FK', 'GF', 'GY', 'SR', 'VE', 'PO Box'],
        'RateTableDetails': {
            'InternationalRateTableId': '5190864010'
        },
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['CA', 'MX'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'GB', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '8.0',
                'ShippingServicePriority': '2',
            },
            {
                'ShipToLocation': ['Asia', 'CN'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '6.0',
                'ShippingServicePriority': '3',
            },
            {
                'ShipToLocation': ['Americas', 'BR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '58.0',
                'ShippingServicePriority': '4',
            },
            {
                'ShipToLocation': 'Worldwide',
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '36.0',
                'ShippingServicePriority': '5',
            }
        ],
    },

    '03.0 ~ 03.5kg【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'ExpeditedShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GN', 'GW', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'YT', 'NE', 'NG', 'SH', 'SN', 'SC', 'SL', 'SO', 'SZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW', 'AI', 'AG', 'AW', 'BS', 'BZ', 'VG', 'KY', 'DM', 'GD', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MS', 'AN', 'NI', 'PA', 'KN', 'LC', 'VC', 'TT', 'TC', 'VI', 'LA', 'MO', 'VN', 'RU', 'AD', 'BY', 'GG', 'JE', 'LI', 'MK', 'MC', 'SM', 'SJ', 'UA', 'VA', 'AF', 'BD', 'BT', 'JP', 'MN', 'NP', 'PK', 'TJ', 'TM', 'IQ', 'JO', 'YE', 'BM', 'GL', 'PM', 'AS', 'CK', 'FJ', 'GU', 'KI', 'MH', 'FM', 'NR', 'NU', 'PW', 'SB', 'TO', 'TV', 'VU', 'WF', 'WS', 'FK', 'GF', 'GY', 'SR', 'VE', 'PO Box'],
        'RateTableDetails': {
            'InternationalRateTableId': '5190864010'
        },
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['CA', 'MX'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'GB', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '9.0',
                'ShippingServicePriority': '2',
            },
            {
                'ShipToLocation': ['Asia', 'CN'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '8.0',
                'ShippingServicePriority': '3',
            },
            {
                'ShipToLocation': ['Americas', 'BR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '66.0',
                'ShippingServicePriority': '4',
            },
            {
                'ShipToLocation': 'Worldwide',
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '45.0',
                'ShippingServicePriority': '5',
            }
        ],
    },

    '03.5 ~ 04.0kg【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'ExpeditedShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GN', 'GW', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'YT', 'NE', 'NG', 'SH', 'SN', 'SC', 'SL', 'SO', 'SZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW', 'AI', 'AG', 'AW', 'BS', 'BZ', 'VG', 'KY', 'DM', 'GD', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MS', 'AN', 'NI', 'PA', 'KN', 'LC', 'VC', 'TT', 'TC', 'VI', 'LA', 'MO', 'VN', 'RU', 'AD', 'BY', 'GG', 'JE', 'LI', 'MK', 'MC', 'SM', 'SJ', 'UA', 'VA', 'AF', 'BD', 'BT', 'JP', 'MN', 'NP', 'PK', 'TJ', 'TM', 'IQ', 'JO', 'YE', 'BM', 'GL', 'PM', 'AS', 'CK', 'FJ', 'GU', 'KI', 'MH', 'FM', 'NR', 'NU', 'PW', 'SB', 'TO', 'TV', 'VU', 'WF', 'WS', 'FK', 'GF', 'GY', 'SR', 'VE', 'PO Box'],
        'RateTableDetails': {
            'InternationalRateTableId': '5190864010'
        },
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['CA', 'MX'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'GB', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '9.0',
                'ShippingServicePriority': '2',
            },
            {
                'ShipToLocation': ['Asia', 'CN'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '6.0',
                'ShippingServicePriority': '3',
            },
            {
                'ShipToLocation': ['Americas', 'BR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '72.0',
                'ShippingServicePriority': '4',
            },
            {
                'ShipToLocation': 'Worldwide',
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '49.0',
                'ShippingServicePriority': '5',
            }
        ],
    },

    '04.0 ~ 04.5kg【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'ExpeditedShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GN', 'GW', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'YT', 'NE', 'NG', 'SH', 'SN', 'SC', 'SL', 'SO', 'SZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW', 'AI', 'AG', 'AW', 'BS', 'BZ', 'VG', 'KY', 'DM', 'GD', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MS', 'AN', 'NI', 'PA', 'KN', 'LC', 'VC', 'TT', 'TC', 'VI', 'LA', 'MO', 'VN', 'RU', 'AD', 'BY', 'GG', 'JE', 'LI', 'MK', 'MC', 'SM', 'SJ', 'UA', 'VA', 'AF', 'BD', 'BT', 'JP', 'MN', 'NP', 'PK', 'TJ', 'TM', 'IQ', 'JO', 'YE', 'BM', 'GL', 'PM', 'AS', 'CK', 'FJ', 'GU', 'KI', 'MH', 'FM', 'NR', 'NU', 'PW', 'SB', 'TO', 'TV', 'VU', 'WF', 'WS', 'FK', 'GF', 'GY', 'SR', 'VE', 'PO Box'],
        'RateTableDetails': {
            'InternationalRateTableId': '5190864010'
        },
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['CA', 'MX'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'GB', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '9.0',
                'ShippingServicePriority': '2',
            },
            {
                'ShipToLocation': ['Asia', 'CN'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '4.0',
                'ShippingServicePriority': '3',
            },
            {
                'ShipToLocation': ['Americas', 'BR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '78.0',
                'ShippingServicePriority': '4',
            },
            {
                'ShipToLocation': 'Worldwide',
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '53.0',
                'ShippingServicePriority': '5',
            }
        ],
    },

    '【FedEx - DHL】00.0 ~ 00.5kg 【30days】【EU含む】': {
        'ShippingType': 'Flat',
        'ShippingServiceOptions': {
            'FreeShipping': 'False',
            'ShippingService': 'StandardShippingFromOutsideUS',
            'ShippingServiceCost': '20.5',
            'ShippingServiceAdditionalCost': '0.0',
        },
    },

    '【FedEx - DHL】00.5 ~ 01.0kg 【5days】【EU含む】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'ExpeditedService': 'False',
            'ShippingService': 'StandardShippingFromOutsideUS',
            'ShippingServiceCost': '1.0',
            'ShippingServiceAdditionalCost': '1.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['US Protectorates', 'GU', 'JP'],
        'InternationalShippingServiceOption': {
            'ShipToLocation': ['Europe', 'Asia', 'CA', 'GB', 'CN', 'MX', 'DE', 'FR'],
            'ShippingService': 'StandardInternational',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        }
    },

    '【US・EU・Mx・Ca・Asia 送料無料】': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': [
            {
                'FreeShipping': 'True',
                'ExpeditedService': 'False',
                'ShippingService': 'StandardShippingFromOutsideUS',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ExpeditedService': 'False',
                'ShippingService': 'ExpeditedShippingFromOutsideUS',
                'ShippingServiceCost': '12.0',
                'ShippingServiceAdditionalCost': '6.0',
                'ShippingServicePriority': '2',
            },
        ],
        'ExcludeShipToLocation': ['JP', 'GU'],
        'InternationalShippingServiceOption': [
            {
                'ShipToLocation': ['Europe', 'Asia', 'CA', 'GB', 'CN', 'MX', 'DE', 'FR'],
                'ShippingService': 'StandardInternational',
                'ShippingServiceCost': '0.0',
                'ShippingServicePriority': '1',
            },
            {
                'ShipToLocation': ['Europe', 'Asia', 'CA', 'GB', 'CN', 'MX', 'DE', 'FR'],
                'ShippingService': 'ExpeditedInternational',
                'ShippingServiceCost': '12.0',
                'ShippingServiceAdditionalCost': '6.0',
                'ShippingServicePriority': '2',
            },
        ],
    },

    '【エコSAL】 5day': {
        'ShippingType': 'Flat',
        'GlobalShipping': 'True',
        'ShippingServiceOptions': {
            'FreeShipping': 'True',
            'ShippingService': 'EconomyShippingFromOutsideUS',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        },
        'ExcludeShipToLocation': ['APO/FPO', 'Africa', 'South America', 'IT', 'JP', 'ID'],
        'InternationalShippingServiceOption': {
            'ShipToLocation': 'Worldwide',
            'ShippingService': 'OtherInternational',
            'ShippingServiceCost': '0.0',
            'ShippingServicePriority': '1',
        }
    },
}
