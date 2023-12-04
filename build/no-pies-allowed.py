import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters for plotting
base_colors = ["wheat", "mediumseagreen", 'lightpink', 'mediumpurple',
               'tan', 'orchid', 'lightslategray', 'lightgreen',
               'paleturquoise', 'olivedrab', 'navy', 'beige']
colorlist_ctrl = ['blueviolet'] + base_colors
colorlist_trmt= ['cornflowerblue','indianred'] + base_colors
colorlist_error = ['blueviolet', 'cornflowerblue'] + base_colors

data = pd.read_csv("./melted-results.csv")
conditions = data.iloc[:, 0:2].drop_duplicates().set_index('Breed')
# conditions = conditions[(conditions.index != "Golden Retriever" &  conditions.Condition != "Treatment")]
results = data.drop(columns=["Condition"]).fillna(0).set_index('Breed')

fig, axes = plt.subplots(6, 2, figsize=(35, 42), subplot_kw=dict(aspect="equal"))
sns.set_style("white")
fig.subplots_adjust(hspace=.35, wspace=0.1)
plt.rcParams["figure.dpi"] = 300
plt.rcParams["figure.autolayout"] = True
sns.set(font_scale=1.7)

# Assign each test to a position (column) in the final figure
col_assign = dict(zip(list(results.columns)[1:], range(0, len(results.columns) - 1)))

breed_num = [0, 0]
for breed_name in conditions.index.unique():
    print(breed_name)
    print(breed_num)
    breed_data = results.loc[results.index == breed_name, ].set_index('Breed_Hit')

    # Set colors based on whether this is a control or treatment case
    breed_cond = conditions.loc[breed_name].values[0]
    if breed_cond == 'Control':
        colors = colorlist_ctrl
        ax_col = 0
    else:
        colors = colorlist_trmt
        ax_col = 1
    # Analyze and plot results from each company in separate bar plots

    plot_data = breed_data.T
    plot_data.index.names = ["Company"]
    plot_data.reset_index(inplace=True)

    plot_data.plot(x='Company', kind='bar', stacked=True, color=colors,
                   ax=axes[breed_num[ax_col], ax_col],
                   xlabel='', title=breed_name,
                   grid=False)

    handles, labels = axes[breed_num[ax_col], ax_col].get_legend_handles_labels()
    axes[breed_num[ax_col], ax_col].legend(handles=handles, labels=labels)
    sns.move_legend(axes[breed_num[ax_col], ax_col], "lower center",
                    bbox_to_anchor=(.5, -1.35),
                    ncol=3)
    axes[breed_num[ax_col], ax_col].title.set_size(40)

    #axes[breed_num[ax_col], ax_col].legend(loc='lower left', bbox_to_anchor=(1, 0.5),
    #                                       ncol=len(plot_data.columns))
    y_axis =  axes[breed_num[ax_col], ax_col].yaxis
    y_axis.set_visible(False)

    breed_num[ax_col] += 1

    sns.despine(offset=10, trim=True, left=True)


    #axes[breed_num[ax_col], ax_col].tick_params(left=False, labelleft=False)
plt.savefig('stackedbars.png', bbox_inches='tight')


