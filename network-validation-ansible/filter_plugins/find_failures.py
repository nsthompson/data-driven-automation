#
# Ansible Filter Plugin to parse test results and return failed tests
#
# Copyright (C) 2025 World Wide Technology
# All Rights Reserved
#
# Written by Nick Thompson (github/@nsthompson)
#

from __future__ import annotations

DOCUMENTATION = r"""
    name: find_failures
    short_description: find failed test results from provided result data
    description:
        - Find failed test results from provided result data
    positional: _input
    options:
        _input:
            description: Input data
            type: dict
            required: true
"""

RETURN = r"""
    _value:
        description:
            - A list of dictionaries containing the failed test details,
                including device and the ansible role called to run the test
    type: list
"""


def parse_data(data):
    """parse_data

    Args:
        data (dict): Provided Test Results Dictionary

    Returns:
        list: Returns list of dictionaries containing failed test results.
    """

    def parse_results(obj, results, current_path=None):
        if current_path is None:
            current_path = []

        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = current_path + [key]
                if key == "fail" and isinstance(value, list) and value:
                    for item in value:
                        test_result = (
                            item.copy() if isinstance(item, dict) else {"value": item}
                        )
                        test_result["device"] = new_path[0]
                        test_result["ansible_role"] = new_path[1]
                        test_result["test"] = new_path[2]
                        results.append(test_result)
                else:
                    parse_results(value, results, new_path)
        elif isinstance(obj, list):
            for item in obj:
                parse_results(item, results)

    all_results = []
    parse_results(data, all_results)

    return all_results


# ---- Ansible filters ----
class FilterModule(object):
    """Ansible Filter Module to parse test results"""

    def filters(self):
        """function to filter provided data"""
        return {"find_failures": parse_data}
