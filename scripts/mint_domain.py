from  scripts.deploy_domains import deploy_domain
from brownie import accounts, Domains
from scripts.helpful_scripts import get_account
def main():
    account = get_account()
    domain = Domains[-1]
    
    domain.register("iconic", {"from": account, "value":"0.5 ethers"})
    # print(domain.getAddress("iconic ace"))

    print(domain.tempoJSON())
    print("Congratulations buddy, you just minted a  domain")


#https://testnets.opensea.io/assets/mumbai/0x4ce43dd7958192f596ff6ab7e1becb137be60b00/0/