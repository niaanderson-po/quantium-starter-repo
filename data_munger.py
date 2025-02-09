import os   
import glob
import pandas as pd 

class MorselDataProcessor:
    def __init__(self):
        self.data = []

    def load_csv(self):
        #file path location
        file_path = "/Users/niaapple/Desktop/VSCode/quantium-starter-repo/data"
        #sets the current working directory of this python process to the csv file path
        os.chdir(file_path)
        #stores all file paths that contains a string matching 'csv' from the current working directory
        csv_files = glob.glob('*.{}'.format('csv'))

        #combine the 3 csv files, ignoring original individual index labels and assigning a new continous index
        self.data = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)

        return self.data

    def filter_data(self, product = None):
        #filters data by product if a specified product is provided, else returns non-filtered original data
        if product:
            self.filtered_df = self.data[self.data['product'] == product].copy()
        else:
            self.filtered_df = self.data.copy()
        
        return self.filtered_df

    def compute_sales(self, use_filter = True):
        #uses filtered data as data source for computation if filter applied, else uses non-filtered original data
        data_source = self.filtered_df.copy() if use_filter else self.data
        self.sales_data = data_source.copy()

        #turn price values into an interger capable of mathimatical operations
        self.sales_data['price'] = self.sales_data['price'].str.replace('$', '').astype(float).astype(int)
        # multiply price of product by quantity sold to get sales amount
        self.sales_data['sales'] = self.sales_data.price.mul(self.sales_data.quantity)

        return self.sales_data

    def save_output(self):
        self.final_data = self.sales_data.copy()

        #sets product as index, (keeping to confirm table is displaying correct data for desired product type)
        self.final_data.set_index('product', inplace=True)
        #sets column names for final df, (can create seperate method in future if dynamic colomn names are wanted)
        self.final_data = self.final_data[['sales', 'date', 'region']]
        #sorts the dates in increasing order
        self.final_data = self.final_data.sort_values(by='date')
        
        #save pandas df as a csv in main directory
        self.final_data.to_csv('/Users/niaapple/Desktop/VSCode/quantium-starter-repo/formatted_data.csv')

if __name__ == "__main__":
    MorselDataProcessor = MorselDataProcessor()
    MorselDataProcessor.load_csv()
    MorselDataProcessor.filter_data("pink morsel")
    MorselDataProcessor.compute_sales()
    MorselDataProcessor.save_output()
