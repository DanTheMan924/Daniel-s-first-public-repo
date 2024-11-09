import pytest
from bank import Account

def test_initial_balance():
    '''test balance and owner of created Account are as expected'''
    acc1 = Account('me')
    assert acc1.balance == 0
    assert acc1.owner == 'me'
    acc2 = Account('mine', 20)
    assert acc2.balance == 20
    assert acc2.owner == 'mine'
    assert acc2.owner != 'yours'

def test_deposit():
    '''test depositing amount updates Account balance'''
    acc = Account('me')
    acc.deposit(40)
    assert acc.balance == 40
    acc.deposit(13)
    assert acc.balance == 53

def test_withdraw():
    '''test update balance properly'''
    acc1 = Account ('me', 60)
    acc1.withdraw(60)
    assert acc1.balance == 0
    acc2 = Account('me', 60)
    acc2.withdraw(43)
    assert acc2.balance == 17

def test_deposit_negative_amount():
    '''can't deposit -ve or 0'''
    acc = Account('me')
    with pytest.raises(ValueError):
        acc.deposit(-20)
    with pytest.raises(ValueError):
        acc.deposit(0)
    assert acc.balance == 0 

def test_withdraw_more_than_balance():
    acc = Account('me', 100)
    with pytest.raises(ValueError):
        acc.withdraw(101)
    with pytest.raises(ValueError):
        acc.withdraw(100.00000000000001)
    assert acc.balance == 100

def test_withdraw_negative_amount():
    '''test can't non-positive amount'''
    acc3 = Account('me', 40)
    with pytest.raises(ValueError):
        acc3.withdraw(0)
    with pytest.raises(ValueError):
        acc3.withdraw(-5)
    assert acc3.balance == 40 #shouldn't change

