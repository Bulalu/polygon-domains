// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;

import { StringUtils } from "force/node_modules/solidity-string-utils/StringUtils.sol";
contract Domains{

    // A mapping data type to store their names
    mapping(string => address) public domains;

    mapping(string => string) public records;
    constructor() {
        
    }

    function register(string calldata name) public {
        // Check that domain is unregistered
        require(domains[name] == address(0));
        domains[name] = msg.sender;
    }

    function getAddress(string calldata name) public view returns(address) {
        return domains[name];
    }

    function setRecords(string calldata name, string calldata record) public {
        require(domains[name] == msg.sender);
        records[name] = record;
    }

    function getRecord(string calldata name) public view returns(string memory) {
        return records[name];
    }
}
