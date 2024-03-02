#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Violation bit using Manchester BiPhase-L encoding
# Github: https://github.com/kourva/ViolationBit

# Standard library imports
import typing
import argparse

# Third-party library imports
import numpy as np
import matplotlib.pyplot as plt

# Local library imports
from manchester import Manchester


class ViolationBit:
    """
    Violation bit simulation using Manchester II
    """
    def __init__(self, 
                 min_v: int, 
                 max_v: int, 
                 data: str) -> typing.NoReturn:
        """
        Initialize method for violation bit

        Parameters:
            min_v (int): Minimum voltage
            max_v (int): Maximum voltage
            data (str): data to be encoded

        Returns:
            typing.NoReturn
        """
        # Initialize the data
        self.min_v: int = min_v
        self.max_v: int = max_v
        self.data: str = data


    def show_plot(self) -> typing.NoReturn:
        """
        Method to show plot for violation bit

        Parameters:
            None

        Returns:
            typing.NoReturn
        """
        # Initialize the x-axis && y-axis
        x: np.ndarray[typing.Any] = np.array([0])
        y: np.ndarray[typing.Any] = np.array([0])

        # Encode the input data using Manchester II
        pattern: typing.List[str] = Manchester().encode(
            data=self.data
        )

        # Duration of each item in the pattern (in seconds)
        duration: int = 1

        # Customize the plot
        plt.ion()

        # Make a figure
        fig: typing.ClassVar[typing.Any] = plt.figure()
        
        # Add subplot
        ax: typing.ClassVar[typing.Any] = fig.add_subplot(111)

        # Set axis limit for Time & Voltage
        ax.set_xlim(
            [0, len(pattern)]
        ) 
        ax.set_ylim(
            [self.min_v-2, self.max_v+2]
        )

        # Set title of plot
        fig.suptitle("Violation Bit - BiPhase-L", fontsize=18, fontweight="bold")
        ax.set_title(
            (
                f"{self.data}    "
                f"Min V: {self.min_v}    "
                f"Max V: {self.max_v}    "
                f"Frame: {len(self.data.split())}"
            ),
            fontsize=13, 
            color="green"
        )

        # Add line to plot for step
        line, = ax.step(x, y, where="post", color="purple")

        # Add column grid to separate steps
        plt.grid(visible=True, axis="x", which="major")

        # Add axis labels
        ax.yaxis.set_major_formatter("V {x:1.1f}")
        ax.xaxis.set_major_formatter("T {x:1.0f}")

        # Show the input data of each signal
        for i in range(0, len(pattern)):
            plt.annotate(
                self.data[i], 
                xy=(i, 1), 
                xytext=(i+0.35, self.max_v+0.3),
                size=25,
                color="gray"
            )
        # Show plot
        plt.show()

        # Update the plot
        for i in range(len(pattern)):
            # Update the x value
            x = np.append(
                x, [i, i + 0.5, i + 0.5, i + 1]
            )

            # Set voltage to 0
            if pattern[i] == "00":
                y = np.append(
                    y, 
                    [0, 0, 0, 0]
                )

            # Set voltage to max to min
            elif pattern[i] == "10":
                y = np.append(
                    y, 
                    [
                        self.max_v, self.max_v,
                        self.min_v, self.min_v
                    ]
                )

            # Set voltage to min to max
            else:
                y = np.append(
                    y, 
                    [
                        self.min_v, self.min_v,
                        self.max_v, self.max_v
                    ]
                )
                

            # Set updated data to plot and set delay
            line.set_data(x, y)
            plt.pause(0.5)

        # Keep the plot open
        plt.ioff()
        plt.show()


# Initialize arguments
parser: typing.ClassVar[typing.Any] = argparse.ArgumentParser(
    description="Violation Bit Simulation"
)
# Add minimum voltage
parser.add_argument(
    "-x", "--min-voltage", type=int, help="Minimum Voltage", metavar="-v"
)

# Add maximum voltage
parser.add_argument(
    "-n", "--max-voltage", type=int, help="Maximum Voltage", metavar="+v"
)

# Add data input
parser.add_argument(
    "-d", "--data", type=str, help="Digital Signal", metavar="data"
)
# Parse the arguments
args = parser.parse_args()


# Run the simulation
if __name__ == "__main__":
    ViolationBit(args.min_voltage, args.max_voltage, args.data).show_plot()