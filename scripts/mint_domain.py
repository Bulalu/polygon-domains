from  scripts.deploy_domains import deploy_domain
from brownie import accounts

def main():
    account = accounts[0]
    domain = deploy_domain()
    
    domain.register("iconic", {"from": account, "value":"0.5 ethers"})
    # print(domain.getAddress("iconic ace"))

    print(domain.tempoJSON())
    print("Congratulations buddy, you just minted a  domain")