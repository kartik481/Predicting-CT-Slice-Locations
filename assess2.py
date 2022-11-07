# Assessment 2 MLPR
import numpy as np
data = np.load('ct_data.npz')
X_train = data['X_train']; X_val = data['X_val']; X_test = data['X_test']
y_train = data['y_train']; y_val = data['y_val']; y_test = data['y_test']

len(y_val)

########################## 1st question ####################################### 
print("Mean of y_train:",np.mean(y_train))
print("Standard error for y_train (for 5785 entries):",np.std(y_train[:5785], ddof=1)/np.sqrt(len(y_train[:5785])))
print("Mean of y_val (for 5785 entries):",np.mean(y_val))
print("Standard error for y_val (for 5785 entries):",np.std(y_val, ddof=1)/np.sqrt(len(y_val)))


#for i in range(len(X_train)):
    #print(X_train[i])


########################## 1st question b part ###############################
rm_idx0=[]    

for i in range(len(X_train[1])):
    col=X_train[:,i]
    if all(col[0]==col):
        rm_idx0.append(i)
        
print("                                   ")
##print("Removed column indices are(constants):",rm_idx0)

X_train = np.delete(X_train,rm_idx0,axis=1)
print("Modified shape of X_train:",X_train.shape)

X_val = np.delete(X_val,rm_idx0,axis=1)
print("Modified shape of X_val:",X_val.shape)

X_test = np.delete(X_test,rm_idx0,axis=1)
print("Modified shape of X_test:",X_test.shape)



indices= np.unique(X_train,return_index=True,axis=1)[1]
np.sort(indices)
rm_idx=list(set(range(indices[0],indices[-1]+1))-set(indices))

print("                                          ")
print("Removed column indices are:",rm_idx0+rm_idx)


X_train = np.delete(X_train,rm_idx,axis=1)
print("Modified shape of X_train:",X_train.shape)

X_val = np.delete(X_val,rm_idx,axis=1)
print("Modified shape of X_val:",X_val.shape)

X_test = np.delete(X_test,rm_idx,axis=1)
print("Modified shape of X_test:",X_test.shape)


