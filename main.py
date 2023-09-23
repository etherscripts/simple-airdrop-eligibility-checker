# Coded by: https://t.me/CryptoResearchLab

import requests
import csv
import re

airdrop_lists_links = {
    "Optimism #1": "https://raw.githubusercontent.com/ethereum-optimism/op-analytics/main/reference_data/address_lists/op_airdrop1_addresses_detailed_list.csv",
    "Optimism #2": "https://raw.githubusercontent.com/ethereum-optimism/op-analytics/main/reference_data/address_lists/op_airdrop2_simple_list.csv",
    "Optimism #3": "https://raw.githubusercontent.com/ethereum-optimism/op-analytics/main/reference_data/address_lists/op_airdrop_3_simple_list.csv",
    "Connext": "https://raw.githubusercontent.com/connext/airdrop-contracts/main/airdrop-1-allocations.csv",
    "Uniswap": "https://raw.githubusercontent.com/banteg/uniswap-distribution/master/uniswap-distribution.csv",
    "Safe": "https://raw.githubusercontent.com/safe-global/safe-token/main/user-allocations/safes_tokens.csv",
    "1inch": "https://gist.githubusercontent.com/banteg/12708815fb63239d9f28dec5df8641f9/raw/28a9dffe9d5681ef5f75b0ab6c39fe5ea0064712/1inch.csv",
    "Badger": "https://gist.githubusercontent.com/banteg/9ad5fdd2e169a03cc5d93478ece10a38/raw/9b14f2fd933d8a817ff6773e4d4854832b02c4b8/badger.csv",
    "Hop": "https://raw.githubusercontent.com/hop-protocol/hop-airdrop/master/src/data/finalDistribution.csv",
    "Curve": "https://gist.githubusercontent.com/nicholashc/f4a34c138087195237556077ea6490d7/raw/bfdf0a9886747dfe3465a2e8ea1bfb02ae0386ac/curve.csv",
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
        elif airdrop_name == "Hop":
            for address, _, _, _, _, amount in csv.reader(requests.get(airdrop_list_link).text.splitlines()):
                if address.lower() in wallet_addresses:
                    ether_amount = int(amount) / 10 ** 18
                    print(f"{airdrop_name} | {address} | {ether_amount}")
        else:
            for address, amount, *_ in csv.reader(requests.get(airdrop_list_link).text.splitlines()):
                if address.lower() in wallet_addresses:
                    print(f"{airdrop_name} | {address} | {amount}")


if __name__ == '__main__':
    check_airdrop_eligibility()