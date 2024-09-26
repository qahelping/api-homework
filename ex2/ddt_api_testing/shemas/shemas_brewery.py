from voluptuous import PREVENT_EXTRA, Schema

get_single_brewery = Schema(
    {
        "id": str,
        "name": str,
        "brewery_type": str,
        "address_1": str,
        "address_2": None,
        "address_3": None,
        "city": str,
        "state_province": str,
        "postal_code": str,
        "country": str,
        "longitude": str,
        "latitude": str,
        "phone": str,
        "website_url": str,
        "state": str,
        "street": str,
    },
    extra=PREVENT_EXTRA,
    required=True,
)
