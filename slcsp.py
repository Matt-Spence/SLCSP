import pandas as pd

# Function to find the SLCSP rate for a given rate area
def find_slcsp_rate(rate_area_plans: pd.DataFrame):
    silver_plans = rate_area_plans[rate_area_plans['metal_level'] == 'Silver']
    sorted_silver_plans = silver_plans['rate'].sort_values().unique()
    if len(sorted_silver_plans) > 1:
        return sorted_silver_plans[1]
    else:
        return None

# Function to find SLCSP rate for a given set of zip codes
def process_zip_codes(zips_df: pd.DataFrame, plans_df: pd.DataFrame, slcsp_df: pd.DataFrame):
    # Iterate through zip codes
    for index, row in slcsp_df.iterrows():
        zip_code = row['zipcode']
        zip_info = zips_df[zips_df['zipcode'] == zip_code]
        
        # Check if zip code is in a single rate area
        if len(zip_info) == 1:
            rate_area = zip_info['rate_area'].iloc[0]
            state = zip_info['state'].iloc[0]
            rate_area_plans = plans_df[(plans_df['rate_area'] == rate_area) & (plans_df['state'] == state)]
            slcsp_rate = find_slcsp_rate(rate_area_plans)
            slcsp_df.loc[index, 'rate'] = slcsp_rate if slcsp_rate is not None else ''
        else:
            slcsp_df = slcsp_df.astype({'rate': str})   # setting incompatible dtypes will be deprecated in the future, so convert to compatible dtype first
            slcsp_df.loc[index, 'rate'] = ''

    # Return resultant DF
    return slcsp_df

if __name__ == "__main__":
    # Load CSV files
    plans_df = pd.read_csv('data/plans.csv')
    zips_df = pd.read_csv('data/zips.csv')
    slcsp_df = pd.read_csv('data/slcsp.csv')

    # Process zip codes
    result_df = process_zip_codes(zips_df, plans_df, slcsp_df)

    # Print zip codes with SLCSP rate
    print(result_df.to_csv(index=False))


