from brownie import Domains, accounts


def deploy_domain():
    account = accounts[0]
    domain = Domains.deploy({"from": account})
    
    domain.register("iconic ace", {"from": account})
    print(domain.getAddress("iconic ace"))

def main():
    deploy_domain()