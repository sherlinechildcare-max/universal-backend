def match_caregiver(client_profile, all_caregivers):
    """
    Match logic: match by conditions, religion, language, care style.
    Later this will use ML model.
    """
    matched = []
    for caregiver in all_caregivers:
        if caregiver.language == client_profile.user.language:
            matched.append(caregiver)
    return matched