fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(x=seattle_weather["MONTH"], y=seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])

# Add Austin temperature data in each month with error bars
ax.errorbar(x=austin_weather["MONTH"], y=austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])

# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()