# Proyek Data Mining

## Implementasi Supervised dan Unsupervised Learning Menggunakan Streamlit

**Nama:** Rama Dhasir  
**NIM:** 23146080  
**Mata Kuliah:** Data Mining (SIF304)  
**Program Studi:** Sistem Informasi  
**Universitas:** Universitas Abulyatama Aceh  
**Tahun Ajaran:** Genap 2025/2026

---

## Deskripsi Proyek

Proyek ini merupakan implementasi metode **Supervised Learning** dan **Unsupervised Learning** dalam satu aplikasi berbasis **Streamlit**. Aplikasi dikembangkan sebagai tugas Ujian Akhir Semester (UAS) Mata Kuliah Data Mining.

Aplikasi terdiri dari dua bagian utama, yaitu klasifikasi diabetes menggunakan tiga algoritma machine learning dan clustering lokasi gerai kopi menggunakan algoritma K-Means. Seluruh model diimplementasikan dalam satu aplikasi web yang dapat digunakan untuk melakukan prediksi maupun analisis data secara interaktif.

---

# Fitur Aplikasi

## 1. Prediksi Risiko Diabetes (Klasifikasi)

Halaman ini digunakan untuk memprediksi apakah seorang pasien berisiko mengidap diabetes berdasarkan data medis yang dimasukkan oleh pengguna.

### Algoritma yang digunakan

- K-Nearest Neighbor (KNN)
- Naïve Bayes
- Decision Tree

### Fitur

- Menampilkan metrik Accuracy
- Menampilkan Precision
- Menampilkan Recall
- Menampilkan F1-Score
- Menampilkan Confusion Matrix
- Prediksi status diabetes pasien berdasarkan data input

---

## 2. Analisis Klaster Lokasi Gerai Kopi (K-Means)

Halaman ini digunakan untuk mengelompokkan lokasi gerai kopi berdasarkan koordinat geografis menggunakan algoritma K-Means.

### Fitur

- Visualisasi Scatter Plot
- Visualisasi Centroid K-Means
- Menampilkan jumlah anggota setiap cluster
- Menentukan cluster dengan jumlah anggota paling sedikit sebagai Zona Sepi
- Prediksi cluster lokasi baru
- Menampilkan status Zona Ramai atau Zona Sepi

---

# Dataset

Dataset yang digunakan dalam proyek ini terdiri dari:

1. **Pima Indians Diabetes Dataset**
   - Digunakan untuk membangun model klasifikasi diabetes.

2. **Dataset Lokasi Gerai Kopi**
   - Digunakan untuk melakukan analisis clustering menggunakan algoritma K-Means.

---

# Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Matplotlib
- Seaborn

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
git clone https://github.com/RamaDhasir/UAS_Data-Mining_Rama-Dhasir_23146080.git
```

## 2. Masuk ke Folder Project

```bash
cd UAS_Data-Mining_Rama-Dhasir_23146080
```

## 3. Install Library

```bash
pip install -r requirements.txt
```

## 4. Jalankan Streamlit

```bash
streamlit run app.py
```

---

# Link GitHub Repository

https://github.com/RamaDhasir/UAS_Data-Mining_Rama-Dhasir_23146080.

---

# Link Aplikasi Streamlit

https://uasdata-miningrama-dhasir23146080-w2a9bwblvlwsxeqht4j9h3.streamlit.app/

---

# Hasil Implementasi

Aplikasi berhasil mengimplementasikan dua pendekatan data mining dalam satu sistem berbasis web. Pada bagian klasifikasi, pengguna dapat membandingkan hasil prediksi menggunakan tiga algoritma machine learning serta melihat metrik evaluasi model. Pada bagian clustering, pengguna dapat melakukan analisis persebaran lokasi gerai kopi, melihat visualisasi hasil clustering, serta memprediksi apakah suatu lokasi baru termasuk ke dalam zona ramai atau zona sepi berdasarkan hasil analisis K-Means.

---

# Penulis

**Rama Dhasir**  
NIM: **23146080**  
Program Studi Sistem Informasi  
Universitas Abulyatama Aceh
