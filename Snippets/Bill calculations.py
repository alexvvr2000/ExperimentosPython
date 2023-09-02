"""Calculate the bills that a person must when going to the ATM."""


def calculate_bills(money, amount_bills):
    """Substract the necesary bills for a bill to be payed.

    First introduce the amount to be breaken down. Afterwards,
    Introduce a paired values of bills and its respective
    amount and eventually you will get a dictionary with the
    necessary bills.

    Args:
        money (float): Total money to break into bills
        bills_amount int:int: Dictionary of bills given descendingly
            that are going to be used for the calculation´s amount:
            {
                bill (int): base_amount (int)
                ...
            }

    Returns:
        A dictionary of bills and its necesary amount for the ATM
        to be taken:
            {
                bill (int): necesarry_bills (int),
                ...
                left (str): remaining (float)
            }
        None if a the given bills can´t cover the given amount

    Example:
        >> avaible_bills = {20:5}
        >> calculate_bills(50, avaible_bills)
        >> {20:2, 'left':10}
    """
    given_bills = {}
    remaining = money

    # to check if all the bills were used
    all_used = {}

    for bill, amount in amount_bills.items():
        given_bills[bill] = 0
        all_used[bill] = False

        # Sucks dry the bill until expends it all
        while remaining >= bill:

            # if all the bills were used
            if given_bills[bill] == amount:
                all_used[bill] = True
                break
            else:
                remaining -= bill
                given_bills[bill] += 1

        if given_bills[bill] == 0:
            del given_bills[bill]

    # if all the bills were used and there is still be money to withdraw
    if all(all_used.values()) and remaining > 0:
        return None
    else:
        # Only two decimals matters
        given_bills['left'] = float('%.2f' % remaining)
        return given_bills


if __name__ == '__main__':

    allowed_bills = {
        500: 4,
        200: 10,
        100: 40,
        50: 10,
        20: 2
    }

    total_ATM = sum(
        bill * amount for bill, amount
        in allowed_bills.items()
    )

    print(
        "Total in ATM: " + str(total_ATM) + "\n" +
        "Avaible bills: " + str(allowed_bills) + "\n"
    )

    money = 7000
    print("Money to withdraw: " + str(money))

    total_bills = calculate_bills(money, allowed_bills)

    if total_bills is None:
        print("Insufficient money in the ATM")
    else:
        print("Bills to give: " + str(total_bills))
