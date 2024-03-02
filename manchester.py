#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library imports
import typing


class Manchester:
    """
    Manchester encoding using G. E. Thomas convention method
    Manchester II (BiPhase-L)
    """

    def __init__(self) -> typing.NoReturn:
        pass

    def encode(self, data: str) -> typing.List[str]:
        """
        Encoding data to Manchester encoded data
        0 -> Low To High: "01"
        1 -> High To Low: "10"
        S -> Space (no voltage): "00"

        e.g. Input: 01011 10  
        ->  ["01", "10", "01", "10", "10", "00", "10", "01"]

        Parameters:
            data (str): data to be encoded

        Returns:
            typing.List[str]: encoded data in list
        """

        # Set output variable
        output: typing.List[str] = list()

        # Encode each digit of data
        for digit in data:
            output.append(
                "01" if digit == "0" else "10" 
                    if digit == "1" else "00"
                        if digit == " " else "x" 
            )

        # Validate output and return error on invalid input
        try:
            assert len(output) == len(data) and not "x" in output
        except AssertionError:
            raise SystemExit("Invalid input provided")

        # Return data
        return output
