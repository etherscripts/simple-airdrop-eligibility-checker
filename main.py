# Coded by: https://t.me/CryptoResearchLab

import requests
import csv
import re

airdrop_lists_links = {
    "Optimism #1": "https://raw.githubusercontent.com/ethereum-optimism/op-analytics/main/reference_data/address_lists/op_airdrop1_addresses_detailed_list.csv",
    "Optimism #2": "https://raw.githubusercontent.com/ethereum-optimism/op-analytics/main/reference_data/address_lists/op_airdrop2_simple_list.csv",
    "Optimism #3": "https://raw.githubusercontent.com/ethereum-optimism/op-analytics/main/reference_data/address_lists/op_airdrop_3_simple_list.csv",
    "Connext": "https://raw.githubusercontent.com/connext/airdrop-contracts/main/airdrop-1-allocations.csv"
}

wallet_addresses = [addr.lower() for addr in re.findall(r"0x\w{40}", open("addresses.txt").read())]


def check_airdrop_eligibility():
    for airdrop_name, airdrop_list_link in airdrop_lists_links.items():
        if airdrop_name == "Connext":
            for amount, address, in csv.reader(requests.get(airdrop_list_link).text.splitlines()):
                if address.lower() in wallet_addresses:
                    print(f"{airdrop_name} | {address} | {amount}")
        elif airdrop_name == "Optimism #1":
            for address, _, _, _, _, _, _, _, _, amount in csv.reader(requests.get(airdrop_list_link).text.splitlines()):
                if address.lower() in wallet_addresses:
                    ether_amount = int(amount) / 10**18
                    print(f"{airdrop_name} | {address} | {ether_amount}")
        else:
            for address, amount, *_ in csv.reader(requests.get(airdrop_list_link).text.splitlines()):
                if address.lower() in wallet_addresses:
                    print(f"{airdrop_name} | {address} | {amount}")


if __name__ == '__main__':
    check_airdrop_eligibility()