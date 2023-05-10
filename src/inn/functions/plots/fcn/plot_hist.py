import matplotlib.pyplot as plt

def plot_hist(data,labels=None):
    nvars = data["parameters"].shape[1]
    for i in range(nvars):
        plt.subplot(1,nvars,i+1)
        plt.hist(data["parameters"][:,i],bins=50)
        if labels is not None:
            plt.title(labels[i])
        # xtikcs 2 decimals in scientific notation
        #plt.xticks([round(x,2) for x in plt.xticks()[0]])
        # ticks labels
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        # plot lint in limits
        plt.axvline(data["limits"][i][0],color='red',linestyle='--')
        plt.axvline(data["limits"][i][1],color='red',linestyle='--')
        plt.grid()
        # xlims 10% of the limits
        plt.xlim([data["limits"][i][0]-0.1*(data["limits"][i][1]-data["limits"][i][0]),data["limits"][i][1]+0.1*(data["limits"][i][1]-data["limits"][i][0])])
