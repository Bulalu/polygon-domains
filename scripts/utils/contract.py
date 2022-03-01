from .contract_address import CONTRACTS
from brownie import Domains, network


def get_domain():
    domain_address = CONTRACTS[network.show_active()]["domain_contract"]
    return Domains.at(domain_address)
