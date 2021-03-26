"""Stock screener. This pulls my stock screen from ADVFN and parses the data. It will provide a strength indicator, weighted to the various metrics identified in the Sather 7 Steps, and a shortlist of stocks to consider."""
import sys
import requests
import pandas as pd
import csv


# Download the data
def download():
    url = 'https://uk.advfn.com/p.php?pid=filterx&pg=2&show=1_53_,1_49_,1_1_,1_2_,1_4_,1_11_,2_10_,2_9_,1_5_,2_27_,1_8_,1_13_,1_23_,2_11_,3_30_,3_31_,3_32_,1_12_,2_77_,2_78_,2_79_,2_80_,1_14_,2_45_,2_44_,2_48_,2_43_,3_28_,1_24_,3_14_,3_21_,3_25_&sort=1_1_D&cnstr=1_4_1_20,1_4_2_0.1&cnstr_idm=232bfbb9e07422778188b06bf7e8f3b6'
    # Need to actually save the file somewhere so that it can be accessed by pandarise func.

# Create Dataframe


def pandarise(csv):
    df = pd.read_csv
    return df


def main():
    """Main entry point for the script."""
    # csv = download()


if __name__ == '__main__':
    main()
    # sys.exit(main÷())
