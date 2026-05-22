def read_input(filename):

    parameters = {}

    with open(filename, 'r') as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            if line.startswith('#'):
                continue

            key, value = line.split('=')

            parameters[key.strip()] = value.strip()

    return parameters
