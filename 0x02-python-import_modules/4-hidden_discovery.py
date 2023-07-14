#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4

    hidden_4_name = dir(hidden_4)
    for names in hidden_4_name:
        if names[0:2] != '__':
            print(names)
