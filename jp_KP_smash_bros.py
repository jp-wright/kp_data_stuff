import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_scatter(df, x, y):
    x_name, y_name = x, y
    x = df[x]
    y = df[y]
    # x = (df[x] - df[x].mean())
    # y = (df[y] - df[y].mean())
    hue_data = x-y


    # xm = df[x].mean()
    # print(xm)
    # ym = df[y].mean()

    fig = plt.figure(figsize=(13,10))
    ax = fig.add_subplot(1,1,1)
    plt.suptitle("KP & JP Smash")
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    ax.axhline(x.mean(), color='k', alpha=.5, linestyle='--', lw=1.3, zorder=0)
    ax.axvline(y.mean(), color='k', alpha=.5, linestyle='--', lw=1.3, zorder=0)
    ax.grid(True, zorder=0)

    # ax.set_xlim([np.min(x)-5, np.max(x)+10])
    # ax.set_ylim([np.min(y)-5, np.max(y)+5])
    # sq = 30
    # ax.set_xlim([-sq, sq])
    # ax.set_ylim([-sq, sq])

    # Plot diagonal line
    diag = np.array([num for num in range(int(min(min(x), min(y)) - 10), int(max(max(x), max(y)) + 10))])
    ax3 = ax.plot(diag, diag, c='grey', alpha=.3, zorder=0)
    ax1 = ax.scatter(x, y, s=500, c=hue_data, cmap='jet', alpha = .78, zorder=10)

    offset = 2
    for i in range(len(x)):
        ax.text(x[i], y[i] + 2.5, '{ply} {val}'.format(ply=df.index[i], val=round(x[i]-y[i], 1)), ha='center', va='bottom', size=11, color='k',zorder=11)

    f = plt.gcf()
    f.subplots_adjust(bottom=0.06, left=0.06, right=.99, top=0.95)
    plt.show()



if __name__ == '__main__':
    df = pd.read_excel('/Users/jpw/Desktop/JP_KP_Smash_Bros.xlsx', header=0)
    df = df.groupby('Player').mean()
    plot_scatter(df, 'Dmg Give', 'Dmg Take')
