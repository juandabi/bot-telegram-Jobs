#%%
import os
import re as re
import numpy as np
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

def rename_columns(df):
    df.rename(columns={'Organisation Name': 'organisation', 'Town/City':'city','County':'county','Type & Rating':'type','Route':'route'}, inplace=True)

def filter_route_rating_organisations(df):
    """
    Filter the dataframe with the route and type & rating
    input: dataframe
    return: dataframe with skilled worker as route and A-rating in type & rating
    """
    df1 = df[df['route'] == 'Skilled Worker']
    df2 = df1[(df1['type'] != "Worker (B rating)") & (
        df1['type'] != "Worker (Probationary Sponsor)")]
    return df2

def organisation_name_column(df):
    """
    Clean the dataframe in the organisation name column
    input: dataframe
    return: dataframe with clean organisation name column
    """
    df.replace({'organisation': ','}, {
               'organisation': '-'}, inplace=True)
    df.replace({'organisation': ';'}, {
               'organisation': '-'}, inplace=True)

def county_column(df):
    """
    clean the dataframe in the county column
    input: dataframe
    return: dataframe with clean county column
    """
    # Convert everything in tittle case
    df['county'] = df['county'].str.title()

    # Clean data with specific value in county column with nan values
    df.replace(
        {'county': '-'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Uk'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Gl'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Wy'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': '120'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Yes'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Gb'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Gla'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Eng'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Twr'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Rct'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': 'Mdx'}, {'county': np.nan}, inplace=True)
    df.replace(
        {'county': '3545'}, {'county': np.nan}, inplace=True)

    # Clean data with specific value in county column with specific values
    df.replace(
        {'county': 'Lnd'}, {'county': 'London'}, inplace=True)
    df.replace(
        {'county': 'Lodnon'}, {'county': 'London'}, inplace=True)
    df.replace({'county': 'Greater Londlon'}, {
        'county': 'London'}, inplace=True)
    df.replace({'county': 'Not In List'}, {
        'county': 'London'}, inplace=True)
    df.replace({'county': '245278394'}, {
        'county': 'London'}, inplace=True)
    df.replace(
        {'county': '1-4992855410'}, {'county': 'Derby'}, inplace=True)
    df.replace({'county': 'Westmisnter'}, {
        'county': 'Westminster'}, inplace=True)
    df.replace(
        {'county': '-Middlesex'}, {'county': 'Middlesex'}, inplace=True)
    df.replace(
        {'county': 'Middx'}, {'county': 'Middlesex'}, inplace=True)
    df.replace({'county': 'Midddlesex'}, {
        'county': 'Middlesex'}, inplace=True)

    # Clean data with regular value in county column with nan values
    df.replace({'county': re.compile(
        '.*--.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*- -.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*select.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*none.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*England.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*ltd.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*wmd.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*mainland.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*Kingdom.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*Region.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*city*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*Nationwide.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*United.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*state.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*Applicable.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*Choose.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*Address.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*W1.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)
    df.replace({'county': re.compile(
        '.*Se1.*', re.IGNORECASE)}, {'county': np.nan}, inplace=True)

    # Clean data with regular value in county column with specific values
    df.replace({'county': re.compile(
        '.*london.*', re.IGNORECASE)}, {'county': 'London'}, inplace=True)
    df.replace({'county': re.compile(
        '.*county*', re.IGNORECASE)}, {'county': 'London'}, inplace=True)

def town_city_column(df):
    """
    Clean data in town/City column
    input: dataframe
    return: dataframe
    """
    # Convert everything in tittle case
    df['city'] = df['city'].str.title()
    # Clean data in Town/city Column
    df.replace({'city': 'Lodnon'}, {'city': 'London'}, inplace=True)
    df.replace({'city': 'Mk'},
               {'city': 'Milton Keynes'}, inplace=True)
    df.replace({'city': 'W'}, {'city': 'Wales'}, inplace=True)
    df.replace({'city': 'Greater London'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': ' London'}, {'city': 'London'}, inplace=True)
    df.replace({'city': 'London,'}, {'city': 'London'}, inplace=True)
    df.replace({'city': 'City Of London'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'London, England'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'City Of London'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'City Of London'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'Derry/Londonderry'},
               {'city': 'Londonderry'}, inplace=True)
    df.replace({'city': 'London Bridge'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'Cambridge, London'},
               {'city': 'Cambridge'}, inplace=True)
    df.replace({'city': 'London Ec3A 7Ag'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'London Heathrow Airport'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'London Uk'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'West London'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'London, United Kingdom'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'London.'}, {'city': 'London'}, inplace=True)
    df.replace({'city': 'Grater London'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'London N7'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'East London'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'London - Uk'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'London, Uk'},
               {'city': 'London'}, inplace=True)
    df.replace({'city': 'Lonond'}, {'city': 'London'}, inplace=True)

    # Copy Londonderry in county if city is Londonderry
    df.loc[df["city"] == "Londonderry", "county"] = "Londonderry"
    # Copy Town/city in county if says london in Town/city
    df['county'].mask((df['city'].str.contains('London', na=False, case=False)) & (
        df['city'] != 'London') & (df['city'] != 'Londonderry'), 'London', inplace=True)

def main(df):
    """
    Iterate over dataframe and clean data
    input: dataframe
    output: dataframe
    """

    df.drop_duplicates(inplace=True)
    rename_columns(df)
    df1 = filter_route_rating_organisations(df)
    organisation_name_column(df1)
    county_column(df1)
    town_city_column(df1)

    return df1

# %%
sponsors_raw = pd.read_csv(os.getenv('SPONSORS_URL'))

sponsors_clean = main(sponsors_raw)
