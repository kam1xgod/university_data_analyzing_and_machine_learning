import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy
from scipy import stats
from scipy.stats import kendalltau
from scipy.stats.mstats_basic import pearsonr, spearmanr


def print_task(number: int) -> None:
    print(f'\n\n\n--------------------------\n\t\t\t{number}\n--------------------------\n')


# task #1.
print_task(1)
csv = pd.read_csv("student-mat.csv")
studytime = csv["studytime"]
freetime = csv["freetime"]
failures = csv["failures"]
absences = csv["absences"]
print(csv)

# task #2.
print_task(2)
# Pierson
print("\n\n\nPierson's correlation:\n")
(studytime_on_failures_pearson_cor,
 studytime_on_failures_pearson_p) = pearsonr(studytime, failures)
(studytime_on_freetime_pearson_cor,
 studytime_on_freetime_pearson_p) = pearsonr(studytime, freetime)
(studytime_on_absences_pearson_cor,
 studytime_on_absences_pearson_p) = pearsonr(studytime, absences)
print("Study time and failures: ",
      studytime_on_failures_pearson_cor)
print("Study time and free time: ",
      studytime_on_freetime_pearson_cor)
print("Study time and absences: ",
      studytime_on_absences_pearson_cor)
print("\n\n\nKendall correlation:\n")
# Kendall
(studytime_on_failures_kendal_cor,
 studytime_on_failures_kendal_p) = kendalltau(studytime, failures)
(studytime_on_freetime_kendal_cor,
 studytime_on_freetime_kendal_p) = kendalltau(studytime, freetime)
(studytime_on_absences_kendal_cor,
 studytime_on_absences_kendal_p) = kendalltau(studytime, absences)
print("Study time and failures: ",
      studytime_on_failures_kendal_cor)
print("Study time and free time: ",
      studytime_on_freetime_kendal_cor)
print("Study time and absences: ",
      studytime_on_absences_kendal_cor)
print("\n\n\nSpearman correlation\n")
# Spearman
(studytime_on_failures_spearman_cor,
 studytime_on_failures_spearman_p) = spearmanr(studytime, failures)
(studytime_on_freetime_spearman_cor,
 studytime_on_freetime_spearman_p) = spearmanr(studytime, freetime)
(studytime_on_absences_spearman_cor,
 studytime_on_absences_spearman_p) = spearmanr(studytime, absences)
print("Study time and failures: ",
      studytime_on_failures_spearman_cor)
print("Study time and freetime: ",
      studytime_on_freetime_spearman_cor)
print("Study time and absences: ",
      studytime_on_absences_spearman_cor)

# task #3.
print_task(3)
# box plot:
fig, ax = plt.subplots()
ax.boxplot((freetime, failures, absences), vert=False, showmeans=True, meanline=True,
           labels=('freetime', 'failures', 'absences'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()

# hists:
hist, bin_edges1 = np.histogram(freetime, bins=10)
hist, bin_edges2 = np.histogram(failures, bins=10)
hist, bin_edges3 = np.histogram(absences, bins=10)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.hist(freetime, bin_edges1, cumulative=False)
ax1.set_xlabel('Freetime')
ax1.set_ylabel('Frequency')
ax2.hist(freetime, bin_edges2, cumulative=False)
ax2.set_xlabel('failures')
ax2.set_ylabel('Frequency')
ax3.hist(absences, bin_edges3, cumulative=False)
ax3.set_xlabel('absences')
ax3.set_ylabel('Frequency')
plt.show()

# plots:
slope, intercept, r, *__ = scipy.stats.linregress(studytime, freetime)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
slope2, intercept2, r2, *__ = scipy.stats.linregress(studytime, failures)
line2 = f'Regression line: y={intercept2:.2f}+{slope2:.2f}x, r={r2:.2f}'
slope3, intercept3, r3, *__ = scipy.stats.linregress(studytime, absences)
line3 = f'Regression line: y={intercept3:.2f}+{slope3:.2f}x, r={r3:.2f}'
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(studytime, freetime, linewidth=0,
         marker='s', label='Studytime vs freetime')
ax1.plot(studytime, intercept + slope * studytime, label=line)
ax2.plot(studytime, failures, linewidth=0,
         marker='s', label='Studytime vs failures')
ax2.plot(studytime, intercept2 + slope2 * studytime, label=line2)
ax3.plot(studytime, absences, linewidth=0,
         marker='s', label='Studytime vs absences')
ax3.plot(studytime, intercept3 + slope3 * studytime, label=line3)
plt.show()

# bars:
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.bar(studytime, freetime)
ax1.set_xlabel('Studytime')
ax1.set_ylabel('Freetime')
ax2.bar(studytime, failures)
ax2.set_xlabel('Studytime')
ax2.set_ylabel('Failures')
ax3.bar(studytime, absences)
ax3.set_xlabel('Studytime')
ax3.set_ylabel('Absences')
plt.show()

# heat maps:
matrix1 = np.corrcoef(studytime, freetime).round(decimals=2)
matrix2 = np.corrcoef(studytime, failures).round(decimals=2)
matrix3 = np.corrcoef(studytime, absences).round(decimals=2)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.imshow(matrix1)
ax1.grid(False)
ax1.xaxis.set(ticks=(0, 1), ticklabels=('studytime', 'freetime'))
ax1.yaxis.set(ticks=(0, 1), ticklabels=('studytime', 'freetime'))
ax1.set_ylim(1.5, -0.5)
ax2.imshow(matrix2)
ax2.grid(False)
ax2.xaxis.set(ticks=(0, 1), ticklabels=('studytime', 'failures'))
ax2.yaxis.set(ticks=(0, 1), ticklabels=('studytime', 'failures'))
ax2.set_ylim(1.5, -0.5)
ax3.imshow(matrix3)
ax3.grid(False)
ax3.xaxis.set(ticks=(0, 1), ticklabels=('studytime', 'absences'))
ax3.yaxis.set(ticks=(0, 1), ticklabels=('studytime', 'absences'))
ax3.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax1.text(j, i, matrix1[i, j], ha='center', va='center', color='w')
        ax2.text(j, i, matrix2[i, j], ha='center', va='center', color='w')
        ax3.text(j, i, matrix3[i, j], ha='center', va='center', color='w')
plt.show()

# Наиболее сильная линейная связь получилась в парах Studytime и failures. Если студент проводит больше времени за учёбой, количество несданных работ резко снижается.
