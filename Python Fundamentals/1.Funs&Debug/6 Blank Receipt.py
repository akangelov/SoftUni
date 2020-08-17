#Blank_Receipt


def print_header():
    print("CASH RECEIPT \n------------------------------")


def print_body():
    print("Charged to____________________ \nReceived by___________________")


def print_footer():
    print("------------------------------\n© SoftUni")


def print_receipt():
    print_header()
    print_body()
    print_footer()

if __name__ == "__main__":
    print_receipt()