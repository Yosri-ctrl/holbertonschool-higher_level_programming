#!/usr/bin/python3
def element_at(my_list, idx):
	if idx < 0 and idx > len(my_list):
		return (None)
	for i in range(len(my_list)):
		if i == idx:
			return int(my_list[i])
