def score_grade(score):
    if score < 40:
        return "F"
    elif score <= 44:
        return "E"
    elif score <= 49:
        return 'D'
    elif score <= 59:
        return 'C'
    elif score <= 69:
        return 'B'
    else:
        return 'A'

