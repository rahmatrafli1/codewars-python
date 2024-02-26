def swap_values(args):
    if len(args) == 2:
        args[0], args[1] = args[1], args[0]
        return args
    else:
        return "Input should contain exactly two elements."