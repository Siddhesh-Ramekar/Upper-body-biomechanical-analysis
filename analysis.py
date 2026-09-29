import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("data/xsens datasheet_5.xlsx")


col = "Right Shoulder q2"


y = pd.to_numeric(df[col], errors="coerce").dropna()


print("Average of", col, "=", y.mean())


smooth = y.rolling(window=30).mean()


plt.figure(figsize=(12, 5))
plt.plot(y.index, y, alpha=0.4, label="raw")
plt.plot(smooth.index, smooth, color="red", label="moving average (30 frames)")
plt.axhline(y.mean(), color="green", linestyle="--", label="overall average")
plt.xlabel("Frame")
plt.ylabel(col)
plt.title(col)
plt.legend()
plt.savefig("output/right_plot.png", dpi=150)
plt.show()



col = "Left Shoulder q2"


y = pd.to_numeric(df[col], errors="coerce").dropna()


print("Average of", col, "=", y.mean())


smooth = y.rolling(window=30).mean()


plt.figure(figsize=(12, 5))
plt.plot(y.index, y, alpha=0.4, label="raw")
plt.plot(smooth.index, smooth, color="red", label="moving average (30 frames)")
plt.axhline(y.mean(), color="green", linestyle="--", label="overall average")
plt.xlabel("Frame")
plt.ylabel(col)
plt.title(col)
plt.legend()
plt.savefig("output/left_plot.png", dpi=150)
plt.show()