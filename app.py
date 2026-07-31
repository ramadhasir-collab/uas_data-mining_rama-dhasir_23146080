import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split

# ====================================================
# CONFIG HALAMAN
# ====================================================
st.set_page_config(page_title="Proyek Data Mining", layout="wide")

# ====================================================
# SIDEBAR
# ====================================================
st.sidebar.title("📌 Menu Navigasi")
page = st.sidebar.radio(
    "Pilih Halaman Proyek:",
    [
        "1. Prediksi Diabetes (Klasifikasi)",
        "2. Clustering Gerai Kopi (K-Means)"
    ]
)

# ====================================================
# HALAMAN 1 : KLASIFIKASI DIABETES
# ====================================================
if page == "1. Prediksi Diabetes (Klasifikasi)":

    st.title("🩺 Prediksi Risiko Diabetes Berdasarkan Data Pasien")
    st.write(
        "Aplikasi ini memprediksi status risiko diabetes pasien menggunakan "
        "tiga algoritma Machine Learning."
    )

    st.markdown("---")

    df_diab = pd.read_csv("diabetes.csv")

    target_col = None
    for col in df_diab.columns:
        if col.lower().strip() in ["outcome", "target", "class", "diabetes"]:
            target_col = col
            break

    if target_col is None:
        target_col = df_diab.columns[-1]

    X = df_diab.drop(target_col, axis=1)
    y = df_diab[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    knn = joblib.load("model_knn.pkl")
    nb = joblib.load("model_nb.pkl")
    dt = joblib.load("model_dt.pkl")

    models = {
        "KNN": knn,
        "Naïve Bayes": nb,
        "Decision Tree": dt
    }

    # ===============================
    # METRIK
    # ===============================
    st.subheader("📊 Metrik Evaluasi Model")

    hasil = []

    for nama, model in models.items():

        pred = model.predict(X_test)

        hasil.append({
            "Algoritma": nama,
            "Akurasi": f"{accuracy_score(y_test,pred):.2f}",
            "Precision": f"{precision_score(y_test,pred):.2f}",
            "Recall": f"{recall_score(y_test,pred):.2f}",
            "F1-Score": f"{f1_score(y_test,pred):.2f}"
        })

    st.table(pd.DataFrame(hasil))

    # ===============================
    # CONFUSION MATRIX
    # ===============================
    st.subheader("🧩 Confusion Matrix")

    pilih = st.selectbox(
        "Pilih Model",
        list(models.keys())
    )

    cm = confusion_matrix(
        y_test,
        models[pilih].predict(X_test)
    )

    fig, ax = plt.subplots(figsize=(5,4))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        ax=ax
    )

    ax.set_xlabel("Prediksi")
    ax.set_ylabel("Aktual")

    st.pyplot(fig)

    st.markdown("---")

    # ===============================
    # INPUT PASIEN
    # ===============================
    st.subheader("📝 Input Data Pasien")

    model_prediksi = st.selectbox(
        "Pilih Algoritma",
        list(models.keys())
    )

    col1, col2 = st.columns(2)

    fitur = X.columns.tolist()

    nilai = []

    for i, nama in enumerate(fitur):

        default = float(X[nama].median())

        minimum = float(X[nama].min())

        maksimum = float(X[nama].max())

        with col1 if i % 2 == 0 else col2:

            x = st.number_input(
                f"Masukkan {nama}",
                value=default,
                min_value=minimum,
                max_value=maksimum
            )

            nilai.append(x)

    if st.button("🔴 Jalankan Prediksi"):

        hasil = models[model_prediksi].predict([nilai])[0]

        if hasil == 1:

            st.error(
                "⚠️ PASIEN DIPREDIKSI MENGIDAP DIABETES"
            )

        else:

            st.success(
                "✅ PASIEN DIPREDIKSI TIDAK MENGIDAP DIABETES"
            )

# ====================================================
# HALAMAN 2 : KMEANS
# ====================================================
elif page == "2. Clustering Gerai Kopi (K-Means)":

    st.title("☕ Analisis Klaster Lokasi Gerai Kopi & Deteksi Zona Sepi")

    st.write(
        "Mengelompokkan lokasi gerai kopi menggunakan algoritma "
        "K-Means untuk mengetahui potensi zona ramai dan zona sepi."
    )

    st.markdown("---")

    df_kopi = pd.read_csv("lokasi_gerai_kopi_clean.csv")

    kmeans = joblib.load("model_kmeans.pkl")

    # ===============================
    # MENCARI NAMA KOLOM
    # ===============================
    col_lat = [
        c for c in df_kopi.columns
        if any(k in c.lower() for k in ["lat","y","lintang"])
    ][0]

    col_lon = [
        c for c in df_kopi.columns
        if any(k in c.lower() for k in ["lon","lng","long","x","bujur"])
    ][0]

    X_kopi = df_kopi[[col_lat, col_lon]]

    df_kopi["Cluster"] = kmeans.labels_

    # ===============================
    # JUMLAH DATA CLUSTER
    # ===============================
    cluster_count = df_kopi["Cluster"].value_counts().sort_index()

    zona_sepi = cluster_count.idxmin()

    # ===============================
    # VISUALISASI
    # ===============================
    st.subheader("📍 Scatter Plot Sebaran Klaster Gerai")

    fig, ax = plt.subplots(figsize=(8,5))

    sns.scatterplot(
        data=df_kopi,
        x=col_lon,
        y=col_lat,
        hue="Cluster",
        palette="Set1",
        s=70,
        ax=ax
    )

    # Centroid
    centers = kmeans.cluster_centers_

    ax.scatter(
        centers[:,1],
        centers[:,0],
        c="black",
        marker="X",
        s=250,
        label="Centroid"
    )

    ax.legend()

    st.pyplot(fig)

    st.markdown("---")

    # ===============================
    # TABEL CLUSTER
    # ===============================
    st.subheader("📊 Jumlah Gerai pada Tiap Cluster")

    tabel_cluster = cluster_count.reset_index()

    tabel_cluster.columns = [
        "Cluster",
        "Jumlah Gerai"
    ]

    st.table(tabel_cluster)

    st.info(
        f"Cluster {zona_sepi} memiliki jumlah gerai paling sedikit "
        "sehingga dikategorikan sebagai Zona Sepi."
    )

    st.markdown("---")

    # ===============================
    # INPUT LOKASI BARU
    # ===============================
    st.subheader("📌 Prediksi Lokasi Baru")

    c1, c2 = st.columns(2)

    with c1:

        in_lat = st.number_input(
            f"Masukkan {col_lat}",
            value=float(X_kopi[col_lat].mean())
        )

    with c2:

        in_lon = st.number_input(
            f"Masukkan {col_lon}",
            value=float(X_kopi[col_lon].mean())
        )

    if st.button("🔍 Cek Klaster & Status Zona"):

        pred_cluster = kmeans.predict([[in_lat, in_lon]])[0]

        st.info(
            f"Lokasi tersebut termasuk ke dalam Cluster {pred_cluster}"
        )

        if pred_cluster == zona_sepi:

            st.warning(
                "⚠️ Status : ZONA SEPI\n\n"
                "Lokasi ini berada pada cluster dengan jumlah gerai paling sedikit."
            )

        else:

            st.success(
                "✅ Status : ZONA RAMAI\n\n"
                "Lokasi ini berada pada cluster dengan kepadatan gerai lebih tinggi."
            )
