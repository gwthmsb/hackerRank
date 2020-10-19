#!/bin/python

import re

input = list()

input.append("riya riya@gmail.com")
input.append("julia julia@julia.me")
input.append("julia sjulia@gmail.com")
input.append("julia julia@gmail.com")
input.append("samantha samantha@gmail.com")
input.append("tanya tanya@gmail.com")
input.append("riya ariya@gmail.com")
input.append("julia bjulia@julia.me")
input.append("julia csjulia@gmail.com")
input.append("julia djulia@gmail.com")
input.append("samantha esamantha@gmail.com")
input.append("tanya ftanya@gmail.com")
input.append("riya riya@live.com")
input.append("julia julia@live.com")
input.append("julia sjulia@live.com")
input.append("julia julia@live.com")
input.append("samantha samantha@live.com")
input.append("tanya tanya@live.com")
input.append("riya ariya@live.com")
input.append("julia bjulia@live.com")
input.append("julia csjulia@live.com")
input.append("julia djulia@live.com")
input.append("samantha esamantha@live.com")
input.append("tanya ftanya@live.com")
input.append("riya gmail@riya.com")
input.append("priya priya@gmail.com")
input.append("preeti preeti@gmail.com")
input.append("alice alice@alicegmail.com")
input.append("alice alice@gmail.com")
input.append("alice gmail.alice@gmail.cominput.append")


if __name__ == '__main__':
    reg = "[a-z\.]+\@gmail\.com$"
    output = list()
    for N_itr in input:
        firstNameEmailID = N_itr.split(" ", 2)

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.match(reg, emailID):
            output.append(firstName)

    ordered_output = sorted(output)

    for name in ordered_output:
        print(name)

