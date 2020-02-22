def format_appointment(appointment):
    return {
        "id": appointment.id,
        "notary": {
                "name": appointment.related_notary.first_name + " " + appointment.related_notary.last_name,
                "id": appointment.notary_id,
            },
        "appointee": {
                "name": appointment.related_appointee.first_name + " " + appointment.related_appointee.last_name,
                "id": appointment.appointee_id,
            },
        "status": appointment.get_appointment_result,
        "time": appointment.time,
        "date": appointment.date,
        "location": appointment.location,
    }
