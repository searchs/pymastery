def do_stuff(num):
    """Adds 5 to passed int"""
    try:
        return int(num) + 5
    except ValueError as err:
        return err
