from dataset_import import dataloading
from Data_Clean import Basics_Search, describe, Missvalues,DropDuplicates
from expoert_data_clean import correct
from MinMaxScaler_Normalizer import Standard_Scaler, MinMax_Values, Normalizer_values
from Quant import salary_outliers, experience_outliers, ai_exposure_outliers
from Statitics import Descrip
from Basic_vasualise import line_plot, Bar_plot, hist_plot
from advanced_visual import Pair_plot, Heat_plot, Heat_cov, Violin_plot
from dashboard import Dash_board
from Probability_Analysis import range, hist_rang
from knn import knn_modeling
from k_means import KMeans_clustering

data = dataloading()
Basics_Search(data)
describe(data)
Missvalues(data)
DropDuplicates(data)
Standard_Scaler(data)
MinMax_Values(data)
Normalizer_values(data)
salary_outliers(data)
experience_outliers(data) 
ai_exposure_outliers(data)
Descrip(data)
correct(data)
line_plot(data)
Bar_plot(data)
hist_plot(data)
Pair_plot(data)
Heat_plot(data)
Heat_cov(data)
Violin_plot(data)
Dash_board(data)
range(data)
hist_rang(data)
knn_modeling(data)
KMeans_clustering(data)