from brownie import Domains, accounts, config, network
from scripts.helpful_scripts import get_account

def deploy_domain():
    account = get_account()
    tld = "ace"
    domain = Domains.deploy(tld, {"from": account}, publish_source=config["networks"][network.show_active()]["verify"])
    return domain
    
def main():
    deploy_domain()