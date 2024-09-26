brewery_schema = {
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "brewery_type": {
      "type": "string"
    },
    "address_1": {
      "type": "string"
    },
    "address_2": {
      "type": ["string", "null"]
    },
    "address_3": {
      "type": ["string", "null"]
    },
    "city": {
      "type": "string"
    },
    "state_province": {
      "type": "string"
    },
    "postal_code": {
      "type": "string"
    },
    "country": {
      "type": "string"
    },
    "longitude": {
      "type": "string"
    },
    "latitude": {
      "type": "string"
    },
    "phone": {
      "type": "string"
    },
    "website_url": {
      "type": "string"
    },
    "state": {
      "type": "string"
    },
    "street": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name",
    "brewery_type",
    "address_1",
    "city",
    "state_province",
    "postal_code",
    "country",
    "phone",
    "website_url",
    "state",
    "street"
  ]
}