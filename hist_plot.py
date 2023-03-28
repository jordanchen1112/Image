import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd  
from scipy.stats import norm
import os

class Flow_plot:

	def __init__(self, path, log = 1, fl = 'FL1-H', mode = 0, cutoff = 3):
		self.path = path
		self.log = log
		self.fl = fl
		self.cutoff = cutoff 
		if mode == 0:
			self.mode = 'dose-dependent'
		elif mode == 1:
			self.mode = 'WT-Mutant'
		else:
			print('模式錯誤')

	def FI_list(self, csv_name): #1=TRUE, 0 =FALSE
		sample_csv = pd.read_csv(self.path + csv_name)
		fi_list = []
		i1 = 0
		i2 = 0
		for i in range(len(sample_csv[self.fl])):
			if not 0 < sample_csv["FSC-A"][i] < 3500000:
				continue
			# if not 0 <sample_csv["SSC-A"][i] < 420000:
			# 	continue
			if sample_csv[self.fl][i] == 0:
				continue

			if self.log == 1:
				fluorecense = round(np.log10(sample_csv[self.fl][i]),15) #log10 後取小數點後兩位
			elif self.log == 0:
				fluorecense =  1 * ((sample_csv[self.fl][i]) // 1) #log10 後取小數點後兩位

			fi_list.append(fluorecense)
			
			if fluorecense >= self.cutoff:
				i2 += 1
			i1 += 1
		self.V1_R = round(i2 / i1 * 100, 2)

		print(f'最大值: {max(fi_list)}')

		return fi_list

	def plot_his(self, alpha =0.5, bins = 500, color = "black", edgecolor="black", histtype ='stepfilled'):		
		print(f"正在繪製圖表...\n模式: {self.mode}\n")
		allFileList = os.listdir(self.path)
		for n in allFileList:
			if 'csv' not in n:
				allFileList.remove(n)
		if self.mode == 'dose-dependent':			
			allFileList.sort(key=lambda x:int(x[0:-4]))
			fig, axes = plt.subplots(len(allFileList), 1, figsize=(9, 40),sharex=True)
		elif self.mode == 'WT-Mutant':
			allFileList.sort(reverse = True)
			fig, axes = plt.subplots(int(len(allFileList) / 2), 1, figsize=(9, 40),sharex=True)
		if self.log == 0:
			norm_sd = 1
		elif self.log == 1:
			norm_sd = 0.1

		n_ = 0
		for csv_name in allFileList:
			print(f'繪製{csv_name}中')
			data = self.FI_list(csv_name) 
			x_d = np.linspace(0, 6, len(data))
			density = sum(norm(xi, norm_sd).pdf(x_d) for xi in data)
			density = density / max(density) * 450
			if self.mode == 'dose-dependent':
				n = n_
				axes[n].fill_between(x_d, density, alpha = 1 - 0.15 * n, color = color,edgecolor="k")				
			elif self.mode == 'WT-Mutant':
				n = n_ // 2
				axes[n].fill_between(x_d, density, alpha = 0.8 - 0.3 * (n_ % 2), color = color,edgecolor="k")

			# 加入V1 
			n = n_
			axes[n].axvline(ymax = 480 ,x = self.cutoff, lw = 1.5, color="red")
			#設定text: V1-R = () %
			font={'family':'Times New Roman',
     			'style':'normal',
                'weight':'normal',
      			'color':'red',
      			'size': 10
				}
			axes[n].text(5, 250, f'V1-R\n{self.V1_R} %', fontdict = font)

			#避免X,Y軸不相交
			axes[n].axis([0, 6, 0, 500]) 
			print(f'----完成 {n_ + 1} / {len(allFileList)}')			
			n_ += 1
			
		# axes[n].set_ylabel('Cell counts')
		axes[n].set_xlabel(self.fl)	
		plt.show()

		return plt

def main():
	# path = "C:/Users/Jordan Chen/Desktop/要的/實驗室/data/2022 data/PM potential/多濃度WT/"
	lab_data_path = "C:/Users/Jordan Chen/Desktop/要的/實驗室/data/2022 data/"
	data_path = r'Caclcium\fluo3-AM\new_csv/'
	calcium = Flow_plot(lab_data_path + data_path, log = 1, fl = 'FL1-H', mode = 0, cutoff = 3.15)
	calcium.plot_his()

	# path2 = "C:/Users/Jordan Chen/Desktop/要的/實驗室/data/2022 data/Caclcium/mitochodria_calicum/csv/"
	# mito_clacium = Flow_plot(path2, log = 1, fl = 'FL2-H', mode = 1)
	# mito_clacium.plot_his()
	


if __name__ == '__main__':
	main()
	


