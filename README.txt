This is the code of the program "Traffic signal estimate and positioning based on GPS trajectory" in CIGIT, 2021 Summer.

To start from the very beginning, you should first guarantee the data and the code are in the right place, then run
'data_prepare.ipynb', 'alignment.ipynb', and 'training.ipynb' in sequence. 'data_prepare.ipynb' reads the original csv 
files, and split them into files with specific date, bus number, condition, and direction. 'alignment.ipynb' reads 
the splited files, and aggregate them as 'dn2up.csv' and 'up2dn.csv', which are 2 different bus routes. 'training.ipynb'
contains feature extracting, framing, ML training and testing. ML models involved: k-NN, SVM, RF, MLP, CNN.

You can also start just from the 'training.ipynb' as long as you have 'dn2up.csv', 'up2dn.csv', 'dn2up_stop&signal.csv',
'up2dn_stop&signal.csv' and guarantee they are in the right place.

To run the ML models, make sure that sklearn, Pytorch for GPU, and visdom are installed. A version 1.8.0 or higher for
Pytorch is recommended.

You can download the data from https://drive.google.com/file/d/15Vy83DdgOk7sEGHcbyEisCcDYXMr6BhM/view?usp=sharing.

The program is completed in August 6, 2021.

Junzhe Huang
E-mail: jhuang618@gatech.edu

Final editing date: August 8, 2021
