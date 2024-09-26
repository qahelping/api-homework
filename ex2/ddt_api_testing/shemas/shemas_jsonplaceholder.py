from voluptuous import PREVENT_EXTRA, Schema

create_user = Schema(
    {"userId": int, "id": int, "title": str, "body": str},
    extra=PREVENT_EXTRA,
    required=True,
)

update_user = Schema(
    {"userId": int, "id": int, "title": str, "body": str},
    extra=PREVENT_EXTRA,
    required=True,
)
