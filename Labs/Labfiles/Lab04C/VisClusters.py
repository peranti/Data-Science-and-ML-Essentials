def azureml_main(frame1):
# Set graphics backend    
    import matplotlib
    matplotlib.use('agg')   
    import matplotlib.pyplot as plt 
    import sklearn.decomposition as de
    import pandas as pd
    
    Azure = True
    
    
## Compute and plot the clusters by first two principal components 
    num_cols = ['FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'area'] 
    pca = de.PCA(n_components = 2)
    pca.fit(frame1[num_cols].as_matrix())
    pca_frame = pd.DataFrame(pca.transform(frame1[num_cols].as_matrix()))
    pca_frame['Assignments'] = frame1.Assignments
    
    temp0 = pca_frame.ix[pca_frame['Assignments'] == 0, :]    
    temp1 = pca_frame.ix[pca_frame['Assignments'] == 1, :] 
    temp0.columns = ['PC1', 'PC2', 'Assignments']
    temp1.columns = ['PC1', 'PC2', 'Assignments']
    
    fig = plt.figure(figsize = (12,6))
    fig.clf() 
    ax = fig.gca()
    temp0.plot(kind = 'scatter', x = 'PC1', y = 'PC2', color='DarkBlue', label='Group 0', alpha = 0.3, ax = ax)
    temp1.plot(kind = 'scatter', x = 'PC1', y = 'PC2', color='Red', label='Group 1', alpha = 0.3, ax = ax)
    ax.set_title('Clusters by principal component projections')
    ax.set_xlabel('First principal component')
    ax.set_ylabel('Second principal component')
    if(Azure == True): fig.savefig('PCA.png')

    
## Create data frames for each cluster   
    temp0 = frame1.ix[frame1['Assignments'] == 0, :]    
    temp1 = frame1.ix[frame1['Assignments'] == 1, :]    
    

## Scatter plots of area vs other numeric variables
    num_cols = ['FFMC', 'DC', 'ISI', 'temp', 'RH', 'rain']    
    fig = plt.figure(figsize = (12, 24))
    fig.clf()
    i = 1
    for col in num_cols:
        ax = fig.add_subplot(6, 1, i)
        title = 'Scatter plot of ' + col + ' vs. fire area'
        temp0.plot(kind = 'scatter', x = col, y = 'area', color='DarkBlue', label='Group 0', alpha = 0.3, ax = ax)
        temp1.plot(kind = 'scatter', x = col, y = 'area', color='Red', label='Group 1', alpha = 0.3, ax = ax)
        ax.set_title(title)
        ax.set_xlabel('')
        i += 1
    if(Azure == True): fig.savefig('Scatter_vs_area.png') 
    
## Scatter plots of FFMC vs the other numeric variables.    
    num_cols = ['DC', 'ISI', 'temp', 'RH', 'rain', 'area']    
    fig = plt.figure(figsize = (12, 24))
    fig.clf()
    i = 1
    for col in num_cols:
        ax = fig.add_subplot(6, 1, i)
        title = 'Scatter plot of ' + col + ' vs. FFMC'
        temp0.plot(kind = 'scatter', x = col, y = 'FFMC', color='DarkBlue', label='Group 0', alpha = 0.3, ax = ax)
        temp1.plot(kind = 'scatter', x = col, y = 'FFMC', color='Red', label='Group 1', alpha = 0.3, ax = ax)
        ax.set_title(title)
        ax.set_xlabel('')
        i += 1
    if(Azure == True): fig.savefig('Scatter_vs_FFMC.png')   
    
    return frame1
