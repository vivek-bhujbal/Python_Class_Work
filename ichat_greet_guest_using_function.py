def greet_guest(name, arrival_time, preference):
    # Determine the time of day
    if 5 <= arrival_time < 12:
        time_of_day = 'morning'
    elif 12 <= arrival_time < 18:
        time_of_day = 'afternoon'
    else:
        time_of_day = 'evening'

    # Generate greeting based on preference
    if preference == 'formal':
        greeting = f"Good {time_of_day}, Mr. {name}."
    elif preference == 'informal':
        greeting = f"Hey {name}, good {time_of_day}!"
    else:
        greeting = f"Hello {name}, good {time_of_day}."

    return greeting


def greet_all_guests(guests):
    for guest in guests:
        name, arrival_time, preference = guest
        print(greet_guest(name, arrival_time, preference))


# List of guests with their names, arrival times, and preferences
guests = [
    ('James', 11, 'formal'),
    ('Jacob', 11, 'formal'),
    ('Benjamin', 14, 'informal'),
    ('William', 19, 'formal'),
    ('Alexander', 20, 'informal')
]

# Greet all guests
greet_all_guests(guests)


