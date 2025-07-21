import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filename):
    df = pd.read_csv(filename)
    return df

def show_correlation_matrix(df):
    corr = df.corr()
    print("\nCorrelation matrix:\n", corr)
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Golf Stats')
    plt.show()

def plot_scatter(df, x_col, y_col, title, xlabel, ylabel, invert_y=False):
    plt.figure(figsize=(7,5))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue='Player', s=100)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if invert_y:
        plt.gca().invert_yaxis()
    plt.show()

def plot_bar(df, x_col, y_col, title, ylim=None):
    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x=x_col, y=y_col)
    plt.title(title)
    if ylim:
        plt.ylim(ylim)
    plt.show()

class Player:
    def __init__(self, name, driving, fairways, greens, putting, scoring):
        self.name = name
        self.driving = driving
        self.fairways = fairways
        self.greens = greens
        self.putting = putting
        self.scoring = scoring

    def summary(self):
        return (f"{self.name}: Driving {self.driving} yd, Fairways Hit {self.fairways}%, "
                f"Greens In Reg {self.greens}%, Putting Avg {self.putting}, Scoring Avg {self.scoring}")

def main():
    df = load_data('golf_stats.csv')
    print("Golf Players Stats:\n", df)

    show_correlation_matrix(df)

    plot_scatter(df, 'DrivingDistance', 'ScoringAverage', 
                 'Driving Distance vs Scoring Average', 
                 'Driving Distance (yards)', 'Scoring Average', invert_y=True)

    plot_scatter(df, 'PuttingAverage', 'ScoringAverage',
                 'Putting Average vs Scoring Average',
                 'Putting Average (putts per hole)', 'Scoring Average', invert_y=True)

    plot_bar(df, 'Player', 'FairwaysHit%', 'Fairways Hit Percentage by Player', ylim=(0, 100))

    # Create Player objects and print summaries
    players = []
    for _, row in df.iterrows():
        p = Player(row['Player'], row['DrivingDistance'], row['FairwaysHit%'],
                   row['GreensInReg%'], row['PuttingAverage'], row['ScoringAverage'])
        players.append(p)

    print("\nPlayer summaries:")
    for p in players:
        print(p.summary())

if __name__ == "__main__":
    main()
