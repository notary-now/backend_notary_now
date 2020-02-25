def format_notary(notary):
    return {
        "id": notary.related_user.id,
        "first_name": notary.related_user.first_name,
        "last_name": notary.related_user.last_name,
        "email": notary.related_user.email,
        "profile_photo": notary.related_user.profile_photo,
        "zip_code": notary.related_user.zip_code,
        "notary_values": {
            "state_notary_number": notary.state_notary_number,
            "commission_date": notary.commission_date,
            "expiration_date": notary.expiration_date,
            "verified": notary.verified,
            "active": notary.active,
            "radius": notary.radius,
            "bio": notary.bio
        }
    }
