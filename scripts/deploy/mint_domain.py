from scripts.deploy.deploy_domains import deploy_domain
from brownie import accounts, Domains
from scripts.helpful_scripts import get_account
from scripts.utils.contract import get_domain

def mint_domain():
    account = get_account()
    domain = Domains[-1]
    print("Contract address", domain)
    # domain.register("iconic", {"from": account, "value":"0.5 ethers"})
    # # print(domain.getAddress("iconic ace"))

    # print(domain.tempoJSON())
    # print("Congratulations buddy, you just minted a  domain")

def get_all_names():
    account = get_account()
    domain = get_domain()
    names = domain.getAllNames({"from": account})
    print("All Names", names)
    return names



def main():
    get_all_names()
    


#https://testnets.opensea.io/assets/mumbai/0x4ce43dd7958192f596ff6ab7e1becb137be60b00/0/