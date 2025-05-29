# Laporan Proyek Pertama Kelas Machine Learning Terapan - Dwi Laras Setyadita
---
## Domain Proyek
Proyek *Machine Learning* ini mengangkat domain kesehatan. Proyek yang dibangun adalah  
*Prediksi Risiko Penyakit Mental* yang dikembangkan berdasarkan data.

## Latar Belakang
Masalah kesehatan mental dan regulasi emosi menjadi isu yang semakin memerlukan perhatian serius di berbagai kelompok 
usia. Berdasarkan Survei Kesehatan Indonesia 2023 yang dilakukan oleh Kementerian Kesehatan, prevalensi depresi nasional 
mencapai 1,4%, yang menunjukkan bahwa gangguan kesehatan mental bukanlah hal yang jarang terjadi[1]. Selain itu, survei 
dari *Indonesia National Adolescent Mental Health* 2022 mengungkap bahwa satu dari tiga individu mengalami masalah 
kesehatan mental, sementara satu dari dua puluh mengalami gangguan mental dalam 12 bulan terakhir[2]. Temuan ini 
mencerminkan bahwa permasalahan kesehatan mental bersifat lintas usia dan perlu penanganan menyeluruh yang melibatkan 
berbagai pendekatan, termasuk edukasi, dukungan sosial, serta inovasi teknologi dalam bidang kesehatan mental.

<br/>

Pemanfaatan teknologi digital, khususnya sistem pendukung berbasis kecerdasan buatan, berpotensi menjadi solusi inovatif 
untuk meningkatkan kesadaran serta deteksi dini risiko masalah kesehatan mental. Dengan kemampuan analisis data yang 
cepat dan akurat, teknologi ini dapat membantu mengidentifikasi pola perilaku dan gejala yang mengarah pada risiko 
penyakit mental. Selain itu, penggunaan aplikasi dan platform digital juga memungkinkan akses layanan kesehatan mental 
yang lebih luas dan mudah dijangkau oleh berbagai kelompok masyarakat, sehingga intervensi dapat dilakukan lebih cepat 
dan tepat sasaran.

## Business Understanding

## Problem Statements
Berdasarkan latar belakang yang telah disampaikan, terdapat beberapa rumusan masalah yang akan diselesaikan pada proyek ini:
1. Faktor apa saja yang memengaruhi tingkat risiko penyakit mental pada individu?
2. Bagaimana cara membangun model *machine learning* untuk melakukan klasifikasi tingkat risiko penyakit mental?
3. Bagaimana cara memilih model *machine learning* dengan akurasi, *precision*, *recall*, dan F1-score terbaik untuk 
masalah prediksi risiko penyakit mental?

### Goals
Proyek ini dibangun dengan tujuan:
1. Mengetahui variabel dan fitur yang berpengaruh terhadap tingkat risiko kesehatan mental individu.
2. Mengetahui cara membangun model *machine learning* untuk melakukan klasifikasi tingkat kesehatan mental individu 
berdasarkan data.
3. Menentukan model terbaik untuk memprediksi tingkat risiko kesehatan mental berdasarkan hasil perbandingan metrik 
evaluasi seperti akurasi, *precision*, *recall*, dan F1-score.

### Solution Statements
Untuk mencapai tujuan dalam studi kasus ini, dilakukan beberapa tahapan solusi sebagai berikut:
1. Melakukan eksplorasi dan analisis data untuk memahami karakteristik data dan mengidentifikasi fitur-fitur yang paling 
relevan terhadap tingkat risiko gangguan kesehatan mental. Analisis yang dilakukan mencakup pembersihan data, visualisasi, 
dan uji korelasi antarf fitur dalam data.
2. Membangun model *machine learning* klasifikasi untuk memprediksi tingkat risiko kesehatan mental individu. Beberapa 
model berikut dipilih berdasarkan kemampuannya dalam menangani kasus klasifikasi:
    - **K-Nearest Neighbors (KNN)**: Mengklasifikasikan data berdasarkan kemiripan dengan tetangga terdekat.
    - **Random Forest**: Menggabungkan banyak *decision tree* untuk meningkatkan stabilitas dan akurasi klasifikasi.
    - **Boosting**: Menggabungkan beberapa model sederhana secara berurutan untuk memperbaiki kesalahan prediksi dan 
   meningkatkan performa.
3. Melakukan evaluasi dan memilih model terbaik dengan membandingkan hasil akurasi, *precision*, *recall*, dan F1-score 
untuk menentukan model yang paling optimal.

## Data Understanding
Dataset yang digunakan pada proyek ini diambil dari 
<br/>
https://www.kaggle.com/datasets/mahdimashayekhi/mental-health
<br/>
### EDA - Deskripsi Variabel
## Deskripsi Dataset
Dataset yang digunakan terdiri dari **10.000 baris data** dan **14 kolom**, yang merepresentasikan berbagai informasi 
terkait kondisi kesehatan mental individu. Berikut adalah penjelasan masing-masing kolom:
- **age**: Usia responden dalam tahun.
- **gender**: Jenis kelamin responden (Male, Female, Non-binary, dan Prefer not to say).
- **employment_status**: Status pekerjaan responden (Employed, Student, Self-employed, dan Unemployed).
- **work_environment**: Kondisi lingkungan kerja responden (Onsite, Online, dan Hybrid).
- **mental_health_history**: Riwayat kesehatan mental sebelumnya (Yes/No).
- **seeks_treatment**: Apakah responden pernah mencari perawatan kesehatan mental (Yes/No).
- **stress_level**: Tingkat stres yang dialami responden, dengan rentang nilai 1–10.
- **sleep_hours**: Jumlah rata-rata jam tidur per hari, dengan rentang nilai 1–10.
- **physical_activity_days**: Jumlah hari dalam seminggu di mana responden melakukan aktivitas fisik, dengan rentang 1–7.
- **depression_score**: Skor tingkat depresi yang dialami responden, dengan rentang 1–30.
- **anxiety_score**: Skor tingkat kecemasan yang dialami responden, dengan rentang 1–21.
- **social_support_score**: Skor tingkat dukungan sosial yang diterima responden, dengan rentang 1–100.
- **productivity_score**: Skor tingkat produktivitas responden, dengan rentang 1–100.
- **mental_health_risk**: Kategori risiko kesehatan mental hasil dari analisis data (High, Medium, Low).

### Variable - variable pada dataset
- Data Integer = age, stress_level, physical_activity_days, depression_score, anxiety_score, social_support_score.  
- Data Float = sleep_hours, productivity_score.  
- Data Object = gender, employment_status, work_environment, mental_health_history, seeks_treatment, mental_health_risk.

### Missing Value, Data Duplikat dan Outlier
- Tidak ditemukan missing value di dalam dataset.  
- Tidak ditemukan outlier di dalam dataset.  
- Tidak ditemukan data duplikat di dalam dataset.

### EDA - Univariate Analysis
Analisis univariat dilakukan untuk memahami distribusi masing-masing variabel secara individual. Beberapa temuan awal:

##### Kolom Categorical 
![Grafik Univariate Numeric Data](./gambar/univariate_categorical.png)
- Terdapat 4 kategori dalam fitur gender yang didominasi dengan kategori Male dan Female dengan perbandingan yang cukup seimbang. 
- Terdapat 4 kategori dalam fitur employment, secara berurutan dari yang paling banyak adalah employed, kemudian diikuti student, self emoployed, dan yang paling sedikit adalah unemployed.
- Terdapat 3 kategori dalam fitur work_environtment. secara berurutan dari yang paling banyak adalah onsite, Remote, dan Hybrid.
- Terdapat 2 kategori dalam fitur mental_health_history. dengan hampir 70% data memiliki value no yang berarti sebagian besar tidak memiliki riwayat penyakit mental.
- Terdapat 2 kategori dalam fitur seeks_treatment, yaitu yes dan no. dengan hampir 60% data menyatakan no yang artinya belum pernah mencari bantuan professional dalam masalah kesehatan mental.
- Terdapat 3 kategori dalam fitur mental_health_risk. Secara berurutan dari yang terbesar adalah medium sebesar 58,9% high sebesar 23,7%, dan low sebesar 17,4%.

##### Kolom Numerik
![Grafik Univariate Numeric Data](./gambar/univariate_numeric.png)
- Data pada kolom stress_level, age, physical_activity_days, anxiety_score, dan social_support_score cenderung memiliki persebaran yang merata.  
- Terdapat peningkatan jumlah yang signifikan pada data fitur depression_score pada nilai maksimal (30).  
- Terdapat peningkatan jumlah yang signifikan pada data fitur productivity_score pada nilai maksimal (100).  
- Data sleep_hours cenderung terdistribusi normal.

### EDA - Multivariate Analysis

##### Kolom Categorical
![Grafik Multivariate Categorical Data](./gambar/multivariate_categorical.png)

- Pada fitur gender, risiko kesehatan mental cenderung merata di semua gender dengan mayoritas berada pada risiko sedang.  
  Tidak ada kategori tertentu yang cenderung memiliki risiko kesehatan mental tinggi, sedang, maupun rendah.  
- Pada fitur employment_status, risiko kesehatan mental pada setiap kategori cenderung merata.  
  Tidak ada kategori tertentu yang cenderung memiliki risiko kesehatan mental tinggi, sedang, maupun rendah.  
- Pada fitur work_environment, risiko kesehatan mental pada setiap kategori juga cenderung merata.  
  Tidak ada kategori tertentu yang cenderung memiliki risiko kesehatan mental tinggi, sedang, maupun rendah.  
- Pada fitur mental_health_history, risiko kesehatan mental pada setiap kategori cenderung merata.  
  Tidak ada kategori tertentu yang cenderung memiliki risiko kesehatan mental tinggi, sedang, maupun rendah.  
- Pada fitur seeks_treatment, tidak ada kategori tertentu yang cenderung memiliki risiko kesehatan mental tinggi, sedang, maupun rendah.  

<br/>

- Fitur seeks_treatment menunjukkan hubungan yang signifikan secara statistik terhadap fitur mental_health_risk.  
  Hal ini dapat diartikan bahwa kecenderungan individu untuk mencari bantuan atau perawatan memiliki pengaruh yang signifikan  
  terhadap tingkat risiko kesehatan mental mereka.  
- Fitur lain seperti gender, employment_status, work_environment, dan mental_health_history tidak menunjukkan hubungan  
  statistik yang signifikan terhadap fitur mental_health_risk.  
  Hal ini dapat diartikan bahwa faktor-faktor tersebut tidak cukup kuat untuk membedakan tingkat risiko kesehatan mental pada individu.

##### Kolom Numerik
![Grafik Multivariate Categorical Data](./gambar/multivariate_numeric.png)
- Pada fitur age, tidak terdapat kalangan umur tertentu yang memiliki kecenderungan risiko kesehatan mental kategori high,  
  medium, maupun low.  
- Pada fitur stress_level, variasi stres pada setiap individu di dalam kategori mental_health_risk cenderung mirip,  
  namun tingkat stres secara umum (berdasarkan median) pada fitur mental_health_risk kategori low cenderung memiliki  
  tingkat stres yang lebih rendah.  
- Pada fitur sleep_hours, tidak terdapat waktu tidur tertentu yang memiliki kecenderungan kesehatan mental kategori  
  high, medium, maupun low.  
- Pada fitur physical_activity_days, individu dengan risiko kesehatan mental kategori high menunjukkan kecenderungan  
  memiliki tingkat aktivitas fisik yang lebih tinggi dibandingkan kategori lainnya. Individu dengan risiko kesehatan mental  
  high dan low memiliki median aktivitas fisik mingguan yang sama, yaitu sekitar 4 hari. Sementara itu, individu dengan  
  risiko kategori medium memiliki median aktivitas fisik yang lebih rendah, yaitu sekitar 3 hari.  
- Pada fitur depression_score, menunjukkan bahwa semakin tinggi risiko kesehatan mental seseorang, semakin tinggi pula  
  skor depresi yang dimilikinya. Ini menunjukkan bahwa kolom depression_score memiliki korelasi yang tinggi dengan  
  kolom mental_health_risk.  
- Pada fitur anxiety_score, menunjukkan bahwa semakin tinggi risiko kesehatan mental seseorang, semakin tinggi pula  
  anxiety_score yang dimilikinya. Ini menunjukkan bahwa kolom anxiety_score memiliki korelasi yang cukup tinggi dengan  
  kolom mental_health_risk.  
- Distribusi nilai pada fitur social_support terlihat relatif merata di setiap kategori mental_health_risk, tanpa adanya  
  perbedaan yang mencolok di antara kategori tersebut.  
- Pada fitur productivity_score menunjukkan korelasi yang kuat dengan fitur mental_health_risk, dimana risiko kesehatan  
  mental individu dengan kategori low memiliki tingkat produktivitas tertinggi dengan nilai median sekitar 95, kemudian  
  individu dengan risiko kesehatan mental kategori medium memiliki nilai median tingkat produktivitas yang lebih rendah  
  yaitu sekitar 80, dan yang terakhir adalah individu dengan tingkat risiko kesehatan mental kategori high memiliki  
  tingkat produktivitas terendah dengan median sekitar 60-an.


## Data Preparation
- Menghapus kolom yang tidak relevan. Beberapa kolom tersebut adalah 'gender', 'employment_status', 'work_environment', 'mental_health_history', 'age', 'stress_level', 'sleep_hours', dan 'social_support_score' dihapus karena tidak memiliki pengaruh yang signifikan terhadap tingkat resiko kesehatan mental (variabel target).
- Melakukan Label Encoding untuk seeks_treatment (data kategorikal non ordinal dengan 2 label memungkinkan untuk dilakukan label encoding) dan mental_health_risk adalah data ordinal sehingga encoder dilakukan dengan metode labeling.
- Melakukan spliting pada dataset dengan rasio pembagian 90% untuk data training dan 10% untuk data testing. Berdasarkan data yang berjumlah 10.000, rasio ini sudaha baik karena model memiliki cukup data untuk training dan cukup data untuk melakukan testing.
- Melakukan Scalling dengan StandardScaller untuk membuat data numerik berada pada rentang nilai yang sama. Hal ini dilakukan agar algoritma tidak bias, kecenderungan model seperti KNN menganggap kolom dengan rentang nilai yang tinggi adalah kolom yang penting. 

## Modeling
- KNN (K-Nearest Neighbor) adalah model machine learning yang bekerja dengan cara membandingkan jarak dari suatu sampel  
  ke sampel pelatihan yang lain dengan memilih sejumlah (k) tetangga terdekat. Dalam studi kasus ini,  
  model K-Nearest Neighbors (KNN) digunakan untuk mengklasifikasikan risiko kesehatan mental dengan parameter  
  n_neighbors=10, yang berarti setiap prediksi didasarkan pada 10 tetangga terdekat dalam data latih. KNN adalah  
  algoritma yang sederhana dan mudah dipahami, namun memiliki kelemahan seperti kurang efektif pada data berdimensi  
  tinggi (curse of dimensionality), sensitif terhadap outlier, dan performa yang menurun jika data tidak seimbang.  
  Selain itu, waktu prediksi bisa menjadi lambat pada dataset besar karena perlu menghitung jarak ke seluruh data latih.

- Random Forest adalah algoritma machine learning yang digunakan untuk menyelesaikan masalah klasifikasi dan regresi.  
  Random Forest adalah kumpulan dari beberapa model decision tree yang masing-masing memiliki hyperparameter berbeda dan  
  dilatih pada beberapa bagian data yang berbeda. Dengan melakukan beberapa keputusan sekaligus melalui beberapa pohon,  
  algoritma Random Forest sangat cocok digunakan pada kasus klasifikasi.  
  Random Forest merupakan metode ensemble yang menggabungkan hasil dari banyak pohon keputusan untuk meningkatkan  
  akurasi dan mengurangi risiko overfitting. Dalam studi kasus ini, model yang dibangun menggunakan n_estimators=50,  
  artinya 50 pohon dibangun, serta max_depth=16 yang membatasi kedalaman maksimal tiap pohon untuk mengontrol kompleksitas model.  
  Parameter random_state=55 digunakan agar hasil pelatihan konsisten dan dapat direproduksi. Sementara itu, n_jobs=-1  
  memungkinkan model memanfaatkan seluruh inti CPU yang tersedia untuk mempercepat proses pelatihan. Random Forest sangat kuat  
  dalam menangani data kompleks dan tahan terhadap noise, tetapi model ini sulit diinterpretasikan dan membutuhkan sumber daya  
  komputasi yang lebih besar.

- Boosting adalah metode klasifikasi yang menggabungkan banyak model sederhana secara bertahap untuk meningkatkan  
  akurasi dengan fokus memperbaiki kesalahan prediksi sebelumnya. Dalam studi kasus ini, AdaBoostClassifier digunakan  
  sebagai metode boosting, dengan learning_rate=0.05, yang menentukan seberapa besar kontribusi setiap model lemah dalam pembelajaran bertahap.  
  Model ini juga menggunakan random_state=55 untuk memastikan hasil yang konsisten. Boosting bekerja dengan memperbaiki  
  kesalahan model sebelumnya secara iteratif, sehingga meningkatkan performa keseluruhan. Namun, AdaBoost dapat menjadi  
  sensitif terhadap outlier dan noise, serta memiliki waktu pelatihan yang lebih lambat dibandingkan beberapa metode lain  
  karena proses pembelajarannya yang bertahap.

## Evaluasi
![Grafik Akurasi Model](./gambar/accuracy2.png)

Evaluasi model dilakukan menggunakan metric accuracy, precision, Recall, dan F1-score untuk mengukur performa dari 
masing-masing model yang digunakan yaitu KNN, Random Forest, dan Boosting Algorithm. 
Berdasarkan hasil akurasi didapatkan informasi sebagai berikut:
- Model terbaik model dengan algoritma random forest yang menghasilkan akurasi, precision, f1-score, dan recall tertinggi, 
yaitu seluruhnya sebesar 99,4%.

- Model kedua terbaik adalah KNN yang menghasilkan akurasi, precision, f1-score, dan recall tidak berbeda jauh dengan random 
forest yaitu semuanya sebesar 97,6%.

- Model terburuk untuk studi kasus ini adalah model yang dibangun dengan algoritma Boosting yang menghasilkan akurasi, 
precision, f1-score dan recall yang cukup rendah, yaitu secara berturut-turut 59,3%; 35,1%; 44,1%; dan 59,3%.

### Penyelesaian permasalahan
1. Setelah melakukan proses EDA, berhasil dilakukan identifikasi fitur-fitur penting dalam klasifikasi resiko kesehatan 
mental yaitu: seeks_treatment, physical_activity_days,	depression_score,	anxiety_score, dan	productivity_score
2. Didalam proyek ini telah dibangun  3 algoritma klasifikasi untuk melakukan prediksi klasifikasi resiko kesehatan mental.
3 model yang dibangun adalah : KNN, Random Forest, dan Boosting Algorithm. Penggunaan parameter seperti n_neighbors, 
n_estimators, dan learning_rate juga sudah dioptimalkan sesuai kebutuhan.
3. Dari evaluasi yang dilakukan, Random Forest terbukti sebagai model paling optimal, karena memiliki nilai tertinggi untuk semua 
metrik dibandingkan model lain. Meskipun KNN mencapai metrik yang hampir sama dengan Random Forest, semua metrik evaluasi 
yang dihasilkan masih lebih rendah. 

### Kesimpulan 
Berdasarkan hasil evaluasi, model Random Forest adalah model terbaik yang dapat dijadikan model utama untuk prediksi klasifikasi 
resiko kesehatan mental dalam studi kasus ini. 
<br/>
Model Random Forest meskipun memiliki metrik akurasi, recall, precision 
dan f1-score yang lebih rendah daripada model Random Forest, model ini juga dapat dipertimbangkan untuk digunakan dalam 
studi kasus ini dikarenakan selisih yang tidak terlalu besar. 
Dengan tujuan yang telah dicapai, diharapkan proyek ini dapat memberikan prediksi risiko kesehatan mental lebih dini
dan dapat meningkatkan kesadaran pengguna untuk segera mencari pertolongan apabila terdapat indikasi resiko kesehatan metal yang dialami. 
![Grafik Akurasi Model](./gambar/accuracy.png)
## Referensi

[1]: Kementerian Kesehatan Republik Indonesia, *Laporan Tematik Survei Kesehatan Indonesia Tahun 2023: Potret Indonesia Sehat*, Jakarta: Kementerian Kesehatan RI, 2024. Diterbitkan oleh Kementerian Kesehatan RI dan dikeluarkan oleh Badan Kebijakan Pembangunan Kesehatan. [Online]. Available: https://drive.google.com/file/d/1AnuDQgQufa5JSXEJWpBSv4r7v6d5YZm7/view. [Accessed: May 24, 2025].

[2]: Universitas Gadjah Mada, Universitas Sumatera Utara, Universitas Hasanuddin, The University of 
Queensland Australia, Johns Hopkins Bloomberg School of Public Health, and Kementerian Kesehatan Republik 
Indonesia, *I-NAMHS: Indonesia-National Adolescent Mental Health Survey*, 2022.
