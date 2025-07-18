import pandas as pd
import matplotlib.pyplot as plt

class SectorTrendsVisualizer:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def plot_sector_counts(self):
        plt.figure(figsize=(10,6))
        count_data = self.data['sector'].value_counts()
        count_data.plot(kind='bar')
        plt.title('Company Count by Sector')
        plt.xlabel('Sector')
        plt.ylabel('Number of Companies')
        plt.savefig('sector_counts.png')
        plt.close()

    def funding_by_sector(self):
        if 'market_cap' not in self.data.columns or 'sector' not in self.data.columns:
            print("market_cap or sector column missing.")
            return
        grouped = self.data.groupby('sector')['market_cap'].sum()
        grouped.plot(kind='bar', figsize=(10,6))
        plt.title('Total Market Cap by Sector')
        plt.xlabel('Sector')
        plt.ylabel('Total Market Cap')
        plt.savefig('sector_funding.png')
        plt.close()

if __name__ == "__main__":
    vis = SectorTrendsVisualizer('company_financials.csv')
    vis.plot_sector_counts()
    vis.funding_by_sector()

