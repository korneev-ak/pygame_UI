def lambdaWrap(func,args):
    """
    instead of lambdas in loops that don't copy values
    :return: lambda: func(*args)
    """
    return lambda:func(*args)