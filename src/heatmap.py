# Pickup Heatmap
df['day'] = df['Date/Time'].dt.day

pivot = df.pivot_table(index='day', columns='hour', aggfunc='size')

sns.heatmap(pivot, cmap='coolwarm')
plt.title("Uber Pickup Heatmap")
plt.show()
