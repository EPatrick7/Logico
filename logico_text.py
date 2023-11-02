import logico


def run():
    while True:
        print(logico.crunch(logico.input_statement(input("Calculate: ")),False))
if __name__ == "__main__":
    run()