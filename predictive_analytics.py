# -*- coding: utf-8 -*-
"""Predictive_analytics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CLjYfcfoF2EXtV7uY36sd-o7wZ4zhroa

## Import Library yang Diperlukan
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import chi2_contingency

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

"""## Data Loading"""

# Upload kaggle.json
from google.colab import files
files.upload()

"""membuat direktori kaggle untuk menyimpan dataset"""

!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

"""Download dataset dari Kaggle"""

!kaggle datasets download -d mahdimashayekhi/mental-health -p /kaggle

"""unzip file"""

!unzip /kaggle/mental-health.zip -d /kaggle

"""membuat dataframe dari dta csv"""

student_df = pd.read_csv('/kaggle/mental_health_dataset.csv')
student_df

"""insight
- terdapat 10.000 baris data dalam dataset
- terdapat 14 kolom data yaitu : age, gender, employment_status,	work_environment,	mental_health_history,	seeks_treatment,	stress_level,	sleep_hours,	physical_activity_days,	depression_score,	anxiety_score	social_support_score,	productivity_score,	mental_health_risk.

## Exploratory Data Analysis

### Deskripsi Variabel

deskripsi variabel
"""

student_df.info()

"""Insight
- terdapat 6 kolom kategorikal dengan tipe data object yaitu kolom gender, emplotment_status, work_environtment, mental_health_history, seeks_treatment, dan mental_health_risk.
- terdapat 6 kolom numerik dengan tipe data int64 yaitu : age, stress_level, physical_activity_days, depression_score, anxiety_score, dan social_support_score.
- terdapat 2 kolom numerik dengan tipe data float, yaitu: sleep_hours productivity_score

melihat presebaran data
"""

student_df.describe()

"""### Meneriksa dan menangani missing value

memeriksa missing value
"""

missing_values = student_df.isnull().sum()
print(missing_values[missing_values > 0])

"""insight
- tidak ditemukan missing value di dalam dataset

### Memeriksa dan menangani Outliers
"""

# mengambil semua kolom yang bertipe numerik
cols = student_df.select_dtypes(include='number').columns

# membuat matriks visualisasi 8x2
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 12))
axes = axes.flatten()

# membuat visualisasi boxplot untuk setiap kolom
for i, col in enumerate(cols):
  sns.boxplot(x=student_df[col], ax=axes[i], color='pink')
  axes[i].set_title(f'Visualisasi boxplot kolom {col}')
  axes[i].set_xlabel(col)

plt.tight_layout()
plt.show()

"""insight
- tidak ditemukan data dengan outliers

### Univariate Analysis
"""

# memisahkan kolom tipe numerik dan kategori
numerical_features = student_df.select_dtypes(include='number').columns
categorical_features = student_df.select_dtypes(include='object').columns

# print kolom numerik
print('kolom numerik : ')
for col in numerical_features:
  print(f"-{col}")

# print kolom kategori
print('\nkolom kategori : ')
for col in categorical_features:
  print(f"-{col}")

"""melakukan univariate analysis pada data categorical"""

for col in categorical_features:
    count = student_df[col].value_counts()
    percent = 100 * student_df[col].value_counts(normalize=True)
    df = pd.DataFrame({'Jumlah sampel': count, 'Persentase (%)': percent.round(1)})

    print(f"\n{col}:\n", df)

    # Buat plot baru untuk setiap fitur
    plt.figure(figsize=(6, 4))
    count.plot(kind='bar', color='pink')
    plt.title(col, fontsize=14)
    plt.ylabel("Jumlah", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()

"""insight
- Terdapat 4 kategori dalam fitur gender yang didominasi dengan kategori Male dan Female dengan perbandingan yang cukup seimbang.
- Terdapat 4 kategori dalam fitur employment, secara berurutan dari yang paling banyak adalah employed, kemudian diikuti student, self emoployed, dan yang paling sedikit adalah unemployed.
- terdapat 3 kategori dalam fitur work_environtment. secara berurutan dari yang paling banyak adalah onsite, Remote, dan Hybrid.
- terdapat 2 kategori dalam fitur mental_health_history. dengan hampir 70% data memiliki value no yang berarti sebagian besar tidak memiliki riwayat penyakit mental.
terdapat 2 kategori dalam fitur seeks_treatment, yaitu yes dan no. dengan hampir 60% data menyatakan no yang artinya belum pernah mencari bantuan professional dalam masalah kesehatan mental.
- terdapat 3 kategori dalam fitur mental_health_risk. Secara berurutan dari yang terbesar adalah medium sebesar 58,9%m high sebesar 23,7%, dan low sebesar 17,4%.

melakukan univariate data analysis pada fitur numerik
"""

# membuat matriks visualisasi 8x2
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 12))
axes = axes.flatten()

# membuat visualisasi boxplot untuk setiap kolom
for i, col in enumerate(numerical_features):
  sns.histplot(x=student_df[col], ax=axes[i], color='pink', bins=30)
  axes[i].set_title(f'Visualisasi boxplot kolom {col}')
  axes[i].set_xlabel(col)

plt.tight_layout()
plt.show()

"""insight
- data pada kolom stress_level, age, physical_activity_days, anxiety_score, dan social_support_score cenderung memiliki presebaran yang merata
- terdapat peningkatan jumlah yang signifikan pada data fitur depression_rate dengan score 30.
- terdapat peningkatan jumlah yang signifikan pada data fitur productivity_score pada nilai maksimal (100)
- data sleep_hours cenderung terdistribusi normal

### Multivariate Analysis
"""

cat_features = ['gender', 'employment_status', 'work_environment', 'mental_health_history', 'seeks_treatment']

for col in cat_features:
    sns.catplot(x=col, hue='mental_health_risk', kind='count', height=4, aspect=3, data=student_df, palette='Set3')
    plt.title("Distribusi 'mental_health_risk' berdasarkan {}".format(col))
    plt.xticks(rotation=45)

"""insight
- pada fitur gender, resiko kesehatan mental cenderung merata di semua gender dengan mayoritas berada pada resiko sedang, tidak ada kategori tertentu yang cenderung memiliki resiko kesehatan mental high, medium, maupun low.
- pada fitur employment status, resiko kesehatan mental pada setiap kategori cenderung merata, tidak ada kategori tertentu yang cenderung memiliki resiko kesehatan mental high, medium, maupun low.
- pada fitur employment_environtment, resiko kesehatan mental pada setiap kategori juga cenderung merata, tidak ada kategori tertentu yang cenderung memiliki resiko kesehatan mental high, medium, maupun low.
- pada fitur mental_health_history, resiko kesehatan mental pada setiap kategori cenderung merata, tidak ada kategori tertentu yang cenderung memiliki resiko kesehatan mental high, medium, maupun low.  
- pada fitur seeks_treatment, tidak ada kategori tertentu yang cenderung memiliki resiko kesehatan mental high, medium, maupun low.

uji chi-square untuk menguji hubungan antara variabel kategorikal dengan variabel target yang merupakan kategorikal
"""

def chi_square_test(data, feature, target):
    table = pd.crosstab(data[feature], data[target])
    chi2, p, dof, expected = chi2_contingency(table)
    return p


for col in cat_features:
    p_value = chi_square_test(student_df, col, 'mental_health_risk')
    print(f"{col}: p-value = {p_value:.4f}")

"""insight
- fitur seeks_treatment menunjukkan hubungan yang signifikan secara statistik terhadap fitur mental_health_risk. Hal ini dapat diartikan bahwa kecenderungan individu untuk mencari bantuan atau perawatan memiliki pengaruh yang signifikan terhadap tingkat resiko kesehatan mental mereka.
- fitur lain seperti gender, employment_status, work_environtment, dan mental_health_history tidak menunjukkan hubungan statistik yang signifikan terhadap fitur mental_health_risk. Hal ini dapat diartikan bahwa faktor-faktor tersebut tidak cukup kuat untuk membedakan tingkat resiko kesehatan mental pada individu.

melakukan multivariate analysis untuk fitur numerik terhadap fitur target
"""

fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(14, 18))
axes = axes.flatten()

for i, col in enumerate(numerical_features):
    sns.boxplot(x='mental_health_risk', y=col, data=student_df, palette='Set2', ax=axes[i])
    axes[i].set_title(f'Boxplot {col} berdasarkan mental_health_risk')
    axes[i].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

"""insight
- pada fitur age, tidak terdapat kalangan umur tertentu yang memiliki kecenderungan resiko kesehatan mental kategori high, medium, maupun low.
- pada fitur stress_level, variasi stress pada setiap individu di dalam kategori mental_health_risk cenderung mirip, namun tingkat stress secara umum (berdasarkan median) pada fitur mental_health_risk kategori low cenderung memiliki tingkat stress yang lebih rendah.
- pada fitur sleep_hours, tidak terdapat waktu tidur tertentu yang memiliki kecenderungan kesehatan mental kategori high, medium, maupun low.
- pada fitur physical_activity_days, individu dengan resiko kesehatan mental kategori high menunjukkan kecenderungan memiliki tingkat akivitas fisik yang lebih tinggi dibandingkan kategori lainnya. Individu dengan resiko kesehatan mental high dan low memiliki median aktivitas fisik mingguan yang sama, yaitu sekitar 4 hari. Sementara itu, individu dengan resiko kategori Medium memiliki median aktivitas fisik yang lebih rendah yaitu sekitar 3 hari.
- pada fitur depression_score, menunjukkan bahwa semakin tinggi resiko kesehatan mental seseorang, semakin tinggi pula skor depresi yang dimilikinya. ini menunjukkan bahwa kolom depression_score menunjukkan korelasi yang tinggi dengan kolom mental_health_risk.
- pada fitur anxiety_score, menunjukkan bahwa semakin tinggi resiko kesehatan mental seseorang, semakin tinggi pula anxiety_score yang dimilikinya. ini menunjukkan bahwa kolom anxiety_score memiliki korelasi yang cukup tinggi dengan kolom mental_health_risk.
- Distribusi nilai pada fitur social_support terlihat relatif merata di setiap kategori mental_health_risk, tanpa adanya perbedaan yang mencolok di antara kategori tersebut.
- pada fitur productivity_score menunjukkan korelasi yang kuat dengan fitur mental_health_risk. Dimana resiko kesehatan mental individu dengan kategori low memiliki tingkat produktifitas tertinggi dengan nilai median sekitar 95, kemudian individu dengan resiko kesehatan mental kategori medium memiliki nilai median tingkat produktifitas yang lebih rendah yaitu sekitar 80, dan yang terakihr adalah individu dengan tingkat resiko kesehatan mental kategori hight memiliki tingkat produktivitas terendan dengan median sekitar 60-an.

### Menghapus kolom yang tidak diperlukan

Berdasarkan Exploratory Data Analysis yang dilakukan sebelumnya didapatkan informasi mengenai beberapa kolom yang memiliki korelasi rendah terhadap fitur target 'mental_health_risk'. Beberapa kolom tersebut adalah 'gender', 'employment_status', 'work_environment', 'mental_health_history', 'age', 'stress_level', 'sleep_hours', dan 'social_support_score'.

Dalam membangun model machine learning analytics predictive, fitur-fitur ini akan dihapus.
"""

student_df.drop(columns=['gender', 'employment_status', 'work_environment', 'mental_health_history', 'age', 'stress_level', 'sleep_hours', 'social_support_score'], inplace=True)

"""memeriksa apakah kolom berhasil dihapus"""

student_df.info()

"""## Data Preparation

### Encoding kolom kategorikal
"""

le = LabelEncoder()

# encoder kolom seeks_treatment dengan label encoder karena hanya berisi 2 kategori
student_df['seeks_treatment'] = le.fit_transform(student_df['seeks_treatment'])
student_df.head()

# encoder kolom mental_health_risk dengan label encoder karena termasuk data ordinal
student_df['mental_health_risk'] = le.fit_transform(student_df['mental_health_risk'])

"""memeriksa apakah encoding berhasil"""

student_df.head()

"""### PCA"""

sns.pairplot(student_df[['physical_activity_days', 'depression_score', 'anxiety_score', 'productivity_score']], plot_kws={"s": 3});

"""insight
- berdasarkan visualisasi data tersebut tidak perlu dilakukan PCA

### Spliting Data
"""

X = student_df.drop(['mental_health_risk'], axis=1)
y = student_df['mental_health_risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""### Standarization"""

numeric_features = ['physical_activity_days', 'depression_score', 'anxiety_score', 'productivity_score']
scaler = StandardScaler()
scaler.fit(X_train[numeric_features])
X_train[numeric_features] = scaler.transform(X_train.loc[:, numeric_features])
X_train[numeric_features].head()

"""memeriksa data fitur train"""

X_train[numeric_features].describe().round(4)

"""## Modeling

membuat dataframe untuk menyimpan akurasi
"""

models = pd.DataFrame(index=['train_accuracy', 'test_accuracy'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

"""### KNN

membangun model knn
"""

# Inisialisasi model KNN klasifikasi dengan 10 tetangga
model_knn = KNeighborsClassifier(n_neighbors=10)
model_knn.fit(X_train, y_train)

# Prediksi pada data train
y_train_pred = model_knn.predict(X_train)

# Hitung akurasi pada data train
train_accuracy = accuracy_score(y_train, y_train_pred)

# Simpan hasil akurasi di DataFrame models (misal models sudah ada)
models.loc['train_accuracy', 'KNN'] = train_accuracy
models.loc['test_accuracy', 'KNN'] = accuracy_score(y_test, model_knn.predict(X_test))

"""### Random Forest

membangun model random forest
"""

model_RF = RandomForestClassifier(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
model_RF.fit(X_train, y_train)

models.loc['train_accuracy', 'RandomForest'] = accuracy_score(y_train, model_RF.predict(X_train))
models.loc['test_accuracy', 'RandomForest'] = accuracy_score(y_test, model_RF.predict(X_test))

"""### Bosting Algorithm

membangun model Boosting Algorithm
"""

# Inisialisasi model AdaBoost untuk klasifikasi
model_boosting = AdaBoostClassifier(learning_rate=0.05, random_state=55)
model_boosting.fit(X_train, y_train)

# Prediksi pada data train
y_train_pred = model_boosting.predict(X_train)

# Hitung akurasi pada data train
train_accuracy = accuracy_score(y_train, y_train_pred)

# Simpan hasil akurasi ke DataFrame models (misal models sudah ada)
models.loc['train_accuracy', 'Boosting'] = train_accuracy
models.loc['test_accuracy', 'Boosting'] = accuracy_score(y_test, model_boosting.predict(X_test))

"""## Evaluasi

evaluasi
"""

X_test[numeric_features] = pd.DataFrame(
    scaler.transform(X_test[numeric_features]),
    index=X_test.index,
    columns=numeric_features
)

model_dict = {
    'KNN': model_knn,
    'RF': model_RF,
    'Boosting': model_boosting
}

"""memeriksa akurasi model knn"""

y_test_pred = model_knn.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print("Accuracy:", test_accuracy)

"""memeriksa akurasi model random forest"""

y_pred = model_RF.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""memeriksa akurasi model boosting Algorithm"""

y_test_pred = model_boosting.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
models.loc['test_accuracy', 'Boosting'] = test_accuracy
print("Accuracy:", test_accuracy)

"""visualisasi akurasi"""

model_names = models.columns.tolist()

# Ambil nilai akurasi dan ubah ke float
train_accuracies = models.loc['train_accuracy'].astype(float).values
test_accuracies = models.loc['test_accuracy'].astype(float).values

# Tentukan posisi sumbu x
x = np.arange(len(model_names))
width = 0.35  # lebar masing-masing bar

# Buat plot
plt.figure(figsize=(10, 6))
plt.bar(x - width/2, train_accuracies, width, label='Train Accuracy', color='lightblue')
plt.bar(x + width/2, test_accuracies, width, label='Test Accuracy', color='salmon')

# Tambahkan label dan judul
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.title('Train vs Test Accuracy per Model')
plt.xticks(x, model_names)
plt.ylim(0, 1)
plt.tight_layout()

# Tampilkan grafik
plt.show()

"""mencoba prediksi"""

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true': y_test[:1].values}

for name, model in model_dict.items():
    pred_dict['prediksi_' + name] = model.predict(prediksi)

pd.DataFrame(pred_dict)

"""Model terbaik adalah model Random Forest yang menghasilkan tingkat akurasi tertinggi jika dibandingkan dengan model Boosting dan KNN."""