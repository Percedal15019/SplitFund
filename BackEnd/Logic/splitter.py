def calculate_split(total_amount, participants):
    count = len(participants)
    individual = round(total_amount / count, 2)

    return {user_id: individual for user_id in participants}
