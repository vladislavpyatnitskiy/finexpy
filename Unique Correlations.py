import pandas as pd
import numpy as np

def pairs_column(x, details=False):
    
    cor_matrix = x.corr() # Calculate correlation matrix

    # Extract unique pairs and their correlations
    cor_pairs = np.triu_indices_from(cor_matrix, k=1)
    unique_pairs = pd.DataFrame({
        "Security 1": cor_matrix.index[cor_pairs[0]],
        "Security 2": cor_matrix.columns[cor_pairs[1]],
        'Correlation': cor_matrix.values[cor_pairs]
    })
    # Filter out pairs with correlation equal to 1
    filtered_pairs = unique_pairs[unique_pairs['Correlation'] != 1]

    if not details:
        filtered_pairs.reset_index(drop=True, inplace=True)
        
        return filtered_pairs
    else:
        # Descriptive Statistics
        d = pd.DataFrame({
            'Summary': [
                filtered_pairs['Correlation'].min(),
                filtered_pairs['Correlation'].median(),
                filtered_pairs['Correlation'].max(),
                filtered_pairs['Correlation'].mean()
            ]
        }, index=["Min", "Median 50%", "Max", "Mean"])

        return d

print(pairs_column(stock_data, details=False)) # Test
