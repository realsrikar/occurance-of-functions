from occurance import main


if __name__ == "__main__":
    file = int(input(
        "\nWhich data do you want to Process?\n\t1. Negatively Correlated with VVIQ\n\t2. Postitively Correlated with VVIQ\n\n> "))

    if file == 1:
        filename = "negatively.tsv"
    if file == 2:
        filename = "frequency.tsv"
    if file == 3:
        filename = "positively.tsv"

    main("Data/brodmann.tsv", "Data/Table/")
