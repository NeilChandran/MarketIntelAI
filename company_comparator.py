import pandas as pd
import matplotlib.pyplot as plt

class CompanyComparator:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def compare_metric(self, metric):
        self.data = self.data.dropna(subset=[metric])
        plt.figure(figsize=(10,6))
        plt.bar(self.data['ticker'], self.data[metric])
        plt.title(f'{metric} Comparison')
        plt.xlabel('Company')
        plt.ylabel(metric)
        plt.savefig(f'{metric}_comparison.png')
        plt.close()

    def compare_all(self, metrics):
        for metric in metrics:
            self.compare_metric(metric)

    def generate_csv_summary(self, out_path):
        self.data.describe().to_csv(out_path)

if __name__ == "__main__":
    metrics = ['market_cap', 'pe_ratio', 'price']
    cc = CompanyComparator('company_financials.csv')
    cc.compare_all(metrics)
    cc.generate_csv_summary('financials_summary.csv')
