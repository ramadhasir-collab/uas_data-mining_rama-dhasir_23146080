# Proyek Data Mining

# Implementasi Supervised dan Unsupervised Learning Menggunakan Streamlit

**Nama:** Rama Dhasir
**NIM:** 23146080
**Mata Kuliah:** Data Mining (SIF304)
**Program Studi:** Sistem Informasi
**Universitas:** Universitas Abulyatama Aceh
**Tahun Ajaran:** Genap 2025/2026

---

# Deskripsi Proyek

Proyek ini merupakan implementasi metode **Supervised Learning** dan **Unsupervised Learning** dalam sebuah aplikasi berbasis **Streamlit** sebagai pemenuhan tugas Ujian Akhir Semester (UAS) pada mata kuliah Data Mining.

Aplikasi ini menggabungkan dua metode utama dalam data mining, yaitu klasifikasi risiko diabetes menggunakan beberapa algoritma machine learning dan analisis clustering lokasi gerai kopi menggunakan algoritma K-Means.

Seluruh proses mulai dari pemrosesan data, implementasi model, evaluasi, hingga visualisasi hasil analisis dikembangkan dalam satu aplikasi web interaktif sehingga pengguna dapat melakukan prediksi maupun eksplorasi data secara langsung.

---

# Fitur Aplikasi

## 1. Prediksi Risiko Diabetes (Supervised Learning)

Fitur ini digunakan untuk melakukan prediksi risiko diabetes berdasarkan data medis yang dimasukkan oleh pengguna.

### Algoritma yang Digunakan

* K-Nearest Neighbor (KNN)
* Naïve Bayes
* Decision Tree

### Fitur yang Tersedia

* Input data pasien untuk prediksi diabetes
* Perbandingan hasil prediksi dari tiga algoritma
* Menampilkan nilai Accuracy
* Menampilkan Precision
* Menampilkan Recall
* Menampilkan F1-Score
* Menampilkan Confusion Matrix
* Prediksi status risiko diabetes berdasarkan data pengguna

---

## 2. Analisis Klaster Lokasi Gerai Kopi (Unsupervised Learning)

Fitur ini digunakan untuk melakukan pengelompokan lokasi gerai kopi berdasarkan koordinat geografis menggunakan algoritma K-Means.

### Fitur yang Tersedia

* Visualisasi hasil clustering menggunakan Scatter Plot
* Menampilkan posisi centroid setiap cluster
* Menampilkan jumlah anggota pada setiap cluster
* Mengidentifikasi cluster dengan anggota paling sedikit sebagai Zona Sepi
* Melakukan prediksi cluster untuk lokasi baru
* Menentukan status lokasi berdasarkan hasil clustering:

  * Zona Ramai
  * Zona Sepi

---

# Dataset

Dataset yang digunakan dalam proyek ini terdiri dari dua jenis, yaitu:

## 1. Pima Indians Diabetes Dataset

Dataset ini digunakan untuk membangun model klasifikasi diabetes.

Atribut yang digunakan meliputi data medis seperti:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

## 2. Dataset Lokasi Gerai Kopi

Dataset ini digunakan untuk melakukan analisis clustering lokasi menggunakan algoritma K-Means berdasarkan koordinat geografis.

---

# Teknologi yang Digunakan

Proyek ini dikembangkan menggunakan beberapa teknologi berikut:

* **Python** sebagai bahasa pemrograman utama
* **Streamlit** sebagai framework pembuatan aplikasi web interaktif
* **Pandas** untuk pengolahan data
* **Scikit-learn** untuk implementasi algoritma machine learning
* **Joblib** untuk penyimpanan dan pemanggilan model
* **Matplotlib** untuk visualisasi data
* **Seaborn** untuk visualisasi statistik

---

# Struktur Project

```
.
├── app.py
├── diabetes.csv
├── lokasi_gerai_kopi_clean.csv
├── model_knn.pkl
├── model_nb.pkl
├── model_dt.pkl
├── model_kmeans.pkl
├── requirements.txt
└── README.md
```

---

# Cara Menjalankan Aplikasi

## 1. Clone Repository

```bash
git clone https://github.com/ramadhasir-collab/uas_data-mining_rama-dhasir_23146080.git
```

## 2. Masuk ke Folder Project

```bash
cd uas_data-mining_rama-dhasir_23146080
```

## 3. Install Library yang Dibutuhkan

```bash
pip install -r requirements.txt
```

## 4. Jalankan Aplikasi Streamlit

```bash
streamlit run app.py
```

---

# Link Repository GitHub

Repository project dapat diakses melalui:

https://github.com/ramadhasir-collab/uas_data-mining_rama-dhasir_23146080

---

# Link Aplikasi Streamlit

Aplikasi yang telah berhasil di-deploy dapat diakses melalui:

https://uasdata-miningrama-dhasir23146080-vtgtqzfnf344ggqqw6zfu4.streamlit.app/

---

# Hasil Implementasi

Aplikasi berhasil mengimplementasikan dua pendekatan utama dalam data mining, yaitu **Supervised Learning** dan **Unsupervised Learning** dalam satu sistem berbasis web.

Pada bagian klasifikasi diabetes, pengguna dapat melakukan prediksi risiko diabetes menggunakan tiga algoritma machine learning, yaitu KNN, Naïve Bayes, dan Decision Tree. Selain melakukan prediksi, aplikasi juga menyediakan evaluasi performa model menggunakan beberapa metrik seperti Accuracy, Precision, Recall, F1-Score, serta Confusion Matrix.

Pada bagian clustering lokasi gerai kopi, pengguna dapat melihat hasil pengelompokan lokasi berdasarkan algoritma K-Means melalui visualisasi grafik. Sistem juga mampu melakukan prediksi terhadap lokasi baru dan menentukan apakah lokasi tersebut termasuk dalam kategori Zona Ramai atau Zona Sepi berdasarkan hasil analisis cluster.

Dengan adanya aplikasi ini, metode data mining dapat diterapkan secara langsung untuk membantu proses prediksi, analisis pola data, dan pengambilan keputusan berbasis data.

---

# Penulis

**Rama Dhasir**
NIM: **23146080**

Program Studi Sistem Informasi
Universitas Abulyatama Aceh
