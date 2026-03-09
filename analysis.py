import pandas as pd
import matplotlib.pyplot as plt

class DataAnalysis:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def visualize_data(self):
        plt.plot(self.data['column1'], self.data['column2'])
        plt.title('Data Visualization')
        plt.show()

if __name__ == '__main__':
    analysis = DataAnalysis('data.csv')
    analysis.visualize_data()
