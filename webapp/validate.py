from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def note_validate(note):
    errors = {}

    if not note.name:
        errors["name"] = "Name is mandatory"

    if not note.email:
        errors["email"] = "Email is mandatory"
    else:
        try:
            validate_email(note.email)
        except ValidationError:
            errors["email"] = "Invalid email format"

    if note.guest_note and len(note.guest_note) > 50:
        errors["guest_note"] = "The length of this field should be less than 50"

    return errors