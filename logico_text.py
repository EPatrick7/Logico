import logico


def run():
    """Endlessly asks for logical equations to crunch."""
    while True:
        print(logico.crunch(logico.input_statement(input("Calculate: ")),False))
if __name__ == "__main__":
    run()