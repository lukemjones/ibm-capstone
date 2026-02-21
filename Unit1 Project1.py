#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:12:38 2024

@author: lukejones
"""


def greedy_cow_helper(cow_dict, shipment_limit):
    n = 0
    cow_list = list(cow_dict.keys(),)
    helper_list = []
    for cow in cow_list:
        if cow_dict[cow] <= shipment_limit:
            helper_list += [cow]
    if len(helper_list) == 1 and cow_dict[helper_list[n]] >= shipment_limit:
        biggest_cow = helper_list[0]
        return (biggest_cow, cow_dict[biggest_cow])
    elif len(helper_list) == 0 or (len(helper_list) == 1 and \
        cow_dict[helper_list[n]] < shipment_limit):
        return "null"
    else:
        biggest_cow = helper_list[n]
        if cow_dict[helper_list[n]] < cow_dict[helper_list[n + 1]]:
            biggest_cow = helper_list[n + 1]
        n += 1
        while n < len(cow_list) - 1:
            if cow_dict[biggest_cow] < cow_dict[cow_list[n + 1]]: 
                biggest_cow = cow_list[n + 1]
            n += 1
        return [biggest_cow, cow_dict[biggest_cow]]
    


def greedy_cow_transport(cow_dict, weight_limit):
    """
    receives dictionary of cows with weights, and weight limit of ship
    returns nexted lists of shipments
    """
    i = 0
    initial_count = len(cow_dict)
    all_shipments = []
    shipment = []
    shipment_limit = weight_limit
    current_cow = "not selected"
    while i < initial_count:
        current_cow = greedy_cow_helper(cow_dict, shipment_limit)
        if current_cow != "null":
            shipment_limit -= current_cow[1]
            shipment += [current_cow[0]]
            del cow_dict[current_cow[0]]
            print(shipment)
            print(cow_dict)
        else:
            print(all_shipments)
            print(cow_dict)
            all_shipments += shipment,
            shipment_limit = weight_limit
            shipment = []
        i += 1
    return all_shipments