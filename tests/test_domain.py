from scripts.helpful_scripts import get_account
from brownie import Domains, accounts
import brownie
from scripts.deploy.deploy_domains import deploy_domain
from web3 import Web3
# def deploy_domain():
#     account = get_account()
#     _domain = Domains.deploy("ace",{"from": account})
#     return _domain

amount = Web3.toWei(2, "ether")
print(amount)
def test_register():
    owner = get_account()
    domain = deploy_domain()
    name = "iconic"

    with brownie.reverts():
        domain.register(name, {"from":owner, "value": 0})

    domain.register(name, {"from":owner, "value": amount})
    assert domain.getAddress(name) == owner.address
    assert name in domain.getAllNames()


def test_setRecords():
    owner = get_account()
    domain = deploy_domain()
    name = "iconic ace"
    record = "Upcoming millionaire and he's still very young and has a promissing future"
    domain.register(name, {"from":owner, "value": amount})
    with brownie.reverts():
        domain.setRecords("FAKE", record, {"from": owner})
    domain.setRecords(name, record, {"from": owner})
    assert domain.getRecord(name) == record

def test_withdraw():
    owner = get_account()
    domain = deploy_domain()
    bob = accounts[3]
   
    with brownie.reverts():
        domain.withdraw({"from": bob})

    print("Now withdrawing from the contract and go by self a mac")
    domain.withdraw({"from": owner})