# Importing modules
import matplotlib.pyplot as plo
import pandas as pd

#Import data and preparation of proportion_deaths column
yearly = pd.read_csv("datasets/yearly_deaths_by_clinic.csv")
yearly["proportion_deaths"] = yearly["deaths"] / yearly["births"]

# Extract Clinic 1 data into clinic_1 and Clinic 2 data into clinic_2
clinic_1 = yearly[yearly["clinic"] == "clinic 1"]
clinic_2 = yearly[yearly["clinic"] == "clinic 2"]

# Plot yearly proportion of deaths at the two clinics
ax = clinic_1.plot(x="year", y="proportion_deaths", label="Clinic 1", c = 'r')
clinic_2.plot(x="year", y="proportion_deaths", label="Clinic 2", ax=ax, ylabel="Proportion deaths", c = 'blue')
plo.title("Yearly proportion of deaths at the two clinics")

#Read monthly data
monthly = pd.read_csv("datasets/monthly_deaths.csv", parse_dates=["date"])
monthly["proportion_deaths"] = monthly["deaths"] / monthly["births"]
print(monthly.head())
ax1 = monthly.plot( x = "date", y = "proportion_deaths", label = "Proportion of deaths", ylabel = "Proportion deaths")
plo.title("Monthly data")

#Data prepared to compare.
handwashing_start = pd.to_datetime('1847-06-01')
before_washing = monthly[monthly["date"] < handwashing_start]
after_washing = monthly[monthly["date"] >= handwashing_start]

# Plot monthly proportion of deaths before and after handwashing
ax2 = before_washing.plot(x="date", y="proportion_deaths", label = "Before washing")
after_washing.plot(x="date", y="proportion_deaths", label="After washing", ax=ax2, ylabel= "Proportion deaths")
x = after_washing.mean()

# Difference in mean monthly proportion of deaths due to handwashing
before_proportion = before_washing["proportion_deaths"]
after_proportion = after_washing["proportion_deaths"]
mean_diff = after_proportion.mean() - before_proportion.mean()

# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac = 1, replace=True)
    boot_after = after_proportion.sample(frac = 1, replace=True)
    boot_mean_diff.append( boot_after.mean() - boot_before.mean())

# Calculating a 95% confidence interval from boot_mean_diff
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
print(confidence_interval)
#plo.show()
print("Conclusion : Doctors should wash their hands ")