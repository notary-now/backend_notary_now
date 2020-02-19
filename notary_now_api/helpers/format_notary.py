def format_notary(notary):
    return {
        "id": notary.user.id,
        "first_name": notary.user.first_name,
        "last_name": notary.user.last_name,
        "email": notary.user.email,
        "profile_photo": notary.user.profile_photo,
        "zip_code": notary.user.zip_code,
        "notary_values": {
            "commission_date": notary.commission_date,
            "expiration_date": notary.expiration_date,
            "verified": notary.verified,
            "active": notary.active,
            "radius": notary.radius,
            "bio": notary.bio
        }
    }
