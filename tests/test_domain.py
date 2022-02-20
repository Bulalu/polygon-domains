from brownie import Domains, accounts
import brownie
def deploy_domain():
    account = accounts[0]
    _domain = Domains.deploy({"from": account})
    return _domain


def test_register():
    owner = accounts[0]
    domain = deploy_domain()
    name = "iconic ace"
    domain.register(name, {"from":owner})
    assert domain.getAddress(name) == owner.address
    with brownie.reverts():
        domain.register(name, {"from": owner})

def test_setRecords():
    owner = accounts[0]
    domain = deploy_domain()
    name = "iconic ace"
    record = "Upcoming millionaire and he's still very young and has a promissing future"
    domain.register(name, {"from":owner})
    with brownie.reverts():
        domain.setRecords("FAKE", record, {"from": owner})
    domain.setRecords(name, record, {"from": owner})
    assert domain.getRecord(name) == record