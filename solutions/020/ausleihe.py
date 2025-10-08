#! /usr/bin/env python3
"""
This script allows a user to keep track of their lent and returned books.

The following interaction is possible:

```bash
$ ./ausleihe.py
Kontostand: 0
Wie viele Medien wollen Sie ausleihen/zurückgeben? (q zum Beenden)
> 4

Kontostand: 4
Wie viele Medien wollen Sie ausleihen/zurückgeben? (q zum Beenden)
> 20
Sie dürfen maximal 15 Medien ausleihen. Sie können noch 11 Medien ausleihen.

Kontostand: 4
Wie viele Medien wollen Sie ausleihen/zurückgeben? (q zum Beenden)
> -5
Sie können nur Medien zurückgeben, die Sie auch ausgeliehen haben.
Rückgabe wird abgebrochen.

Kontostand: 4
Wie viele Medien wollen Sie ausleihen/zurückgeben? (q zum Beenden)
> q
Programm wird beendet.
$
```
"""

def transact_if_allowed(account_balance, number_of_media):
    """Lend or return media, if within allowed number of media on account.

    Parameters:
    ```````````
    account_balance (int): The current balance before the transaction is attempted.
            Valid values: 0 <= x <= 15
            
    number_of_media (int): The number of the media to be lent or returned.
            A positive number signifies lending and a negative Number signifies returning.

    Returns:
    ````````
    int: The current account balance.
    """
    new_balance = account_balance + number_of_media
    if 0 <= new_balance and new_balance <= 15:
        return new_balance
    elif new_balance > 15:
        print(f"Sie dürfen maximal 15 Medien ausleihen. Sie können noch {15 - account_balance} Medien ausleihen.")
        return account_balance
    elif new_balance < 0:
        print("Sie können nur Medien zurückgeben, die Sie auch ausgeliehen haben.")
        print("Rückgabe wird abgebrochen.")
        return account_balance
    else:
        print("ERROR: Unreachable.")
        print("Account wird zurückgesetzt.")
        return 0

if __name__ == "__main__":
    account_balance = 0 # This variable stores the account balance for the user

    stop_iteration = False

    while not stop_iteration:
        print("Kontostand:", account_balance)
        print("Wie viele Medien wollen Sie ausleihen/zurückgeben? (q zum Beenden)")
        text = input("> ")
        if text == "q":
            print("Programm wird beendet.")
            stop_iteration = True
        else:
            account_balance = transact_if_allowed(account_balance, int(text))
            print()