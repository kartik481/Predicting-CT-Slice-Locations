# Assessment 2 MLPR
import numpy as np
data = np.load('ct_data.npz')
X_train = data['X_train']; X_val = data['X_val']; X_test = data['X_test']
y_train = data['y_train']; y_val = data['y_val']; y_test = data['y_test']

# 1st question 
print("Mean of y_train:",np.mean(y_train))
print("Standard error for y_train (for 5785 entries):",np.std(y_train[:5785], ddof=1)/np.sqrt(len(y_train[:5785])))
print("Mean of y_val (for 5785 entries):",np.mean(y_val[:5785]))
print("Standard error for y_val (for 5785 entries):",np.std(y_val[:5785], ddof=1)/np.sqrt(len(y_val[:5785])))