def my_function(first_name, mood_today):
    '''
    parameters
    ----------
    first_name: as STR
    mood_today: as STR
    '''
    return "Hello, my name is {}, and I'm feeling {}.".format(first_name, mood_today)

if __name__ == '__main__':
    print my_function("Dan", "happy")
