from app.calc import add, BankAccount, InsufficientFunds
import pytest


@pytest.fixture
def zero_bank_acct():
    return BankAccount()


@pytest.fixture
def bank_acct():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8)
])
def test_add(num1, num2, expected):
    print("testing")
    assert add(num1, num2) == expected


def test_bank_set_init_amount(bank_acct):
    assert bank_acct.balance == 50


def test_bank_def_amount(zero_bank_acct):
    assert zero_bank_acct.balance == 0


def test_withdraw(bank_acct):
    bank_acct.withdraw(20)
    assert bank_acct.balance == 30


def test_depo(bank_acct):
    bank_acct.deposit(30)
    assert bank_acct.balance == 80


def test_coll_int(bank_acct):
    bank_acct.collect_interest()
    assert round(bank_acct.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    # (10, 50, -40)
])
def test_bank_txn(zero_bank_acct, deposited, withdrew, expected):
    zero_bank_acct.deposit(deposited)
    zero_bank_acct.withdraw(withdrew)
    assert zero_bank_acct.balance == expected


def test_insufficient_funds(bank_acct):
    with pytest.raises(InsufficientFunds):
        bank_acct.withdraw(200)
