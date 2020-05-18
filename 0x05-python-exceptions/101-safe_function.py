#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as v:
        print("Exception: {}".format(v), file=sys.stderr)
        return None
    
