import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def build_competitor_graph(csv_path):
    df = pd.read_csv(csv_path)
    G = nx.Graph()
    for idx, row in df.iterrows():
        G.add_node(row['ticker'], label=row['sector'])
    for i, row1 in df.iterrows():
        for j, row2 in df.iterrows():
            if i < j and row1['sector'] == row2['sector']:
                G.add_edge(row1['ticker'], row2['ticker'])
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.savefig('competitor_map.png')

if __name__ == "__main__":
    build_competitor_graph('company_financials.csv')

