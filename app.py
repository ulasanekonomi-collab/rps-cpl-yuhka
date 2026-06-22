import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Generator RPS PSEP", page_icon="🎓", layout="wide")

# --- HEADER ---
st.title("🎓 Generator RPS")
st.subheader("Program Studi Ekonomi Pembangunan - Universitas Islam Bandung")
st.markdown("Aplikasi ini membantu dosen merumuskan indikator sikap (CPL S1 & S2) secara otomatis berdasarkan Rumpun Bahan Kajian Kurikulum 2026.")
st.markdown("Yuhka Sundaya")

# --- DATABASE ROUTING (Berdasarkan Buku Pedoman) ---
ROUTING_DB = {
    "BK 2 & 8: Analisis Data, Kuantitatif & AI": {
        "channel": "Channel 1: Analytical & Computational",
        "sikap": "S1.A - Mujahid Persona (Integritas)",
        "indikator": "Menunjukkan ketangguhan (fighting spirit) dalam mengurai kompleksitas teknis, memaparkan algoritma berpikir secara transparan, dan menjunjung kejujuran mutlak (zero plagiarism).",
        "metode": "Logbook/Pengecekan Source Code & Transparansi Kalkulasi",
        "rubrik_5": "Sangat mandiri, alur logis transparan, jujur mengakui error, dan tidak ada indikasi manipulasi data."
    },
    "BK 1: Fondasi Teori Ekonomi Pembangunan": {
        "channel": "Channel 2: Epistemological & Theoretical",
        "sikap": "S1.B - Mujtahid Persona (Validasi & Skeptisisme Asumsi)",
        "indikator": "Menunjukkan nalar kritis (organized skepticism) dalam menguji validitas asumsi teori konvensional dan objektivitas menilai mazhab.",
        "metode": "Esai Analisis Kritis (Paragraf Deduktif)",
        "rubrik_5": "Secara tajam membongkar kelemahan asumsi dasar teori dan membandingkannya menggunakan literatur yang sahih tanpa bias."
    },
    "BK 3, 4, 5, 6, 7: Kebijakan, Lingkungan & Sosial": {
        "channel": "Channel 3: Applied, Policy, & Ethical",
        "sikap": "S1.C & S2 - The Mujaddid & Nasionalisme",
        "indikator": "Mampu merumuskan gagasan pembaharuan (tajdid) yang berorientasi pada kemaslahatan umat, kelestarian alam, dan kedaulatan bangsa.",
        "metode": "Case-Based Method (Policy Brief / Rancangan Solusi)",
        "rubrik_5": "Solusi sangat inovatif, menginternalisasi dampak sosial/ekologi, dan menunjukkan semangat kolaborasi tim yang tinggi."
    }
}

# --- FORM INPUT DOSEN ---
with st.container():
    st.markdown("### 📝 Masukkan Data Mata Kuliah Mingguan")
    col1, col2 = st.columns(2)
    
    with col1:
        nama_mk = st.text_input("Nama Mata Kuliah", placeholder="Contoh: Matematika Ekonomi")
        minggu_ke = st.number_input("Pertemuan Minggu Ke-", min_value=1, max_value=16, value=1)
        
    with col2:
        rumpun_bk = st.selectbox("Pilih Rumpun Bahan Kajian", list(ROUTING_DB.keys()))
        materi = st.text_area("Materi Substantif Mingguan", placeholder="Contoh: Optimasi Dinamis dan Sistem Hamiltonian...")

# --- TOMBOL GENERATE ---
if st.button("🚀 Generate Petak RPS", type="primary"):
    if nama_mk and materi:
        st.success("Berhasil diproses! Berikut adalah rekomendasi pengisian RPS Anda:")
        
        # Ambil data dari routing dictionary
        data_pilihan = ROUTING_DB[rumpun_bk]
        
        # --- HASIL OUTPUT ---
        st.markdown("---")
        st.markdown(f"### 📋 Hasil *Routing* untuk MK: **{nama_mk}** (Minggu {minggu_ke})")
        
        col_res1, col_res2 = st.columns([1, 2])
        
        with col_res1:
            st.info(f"**Saluran Penilaian:**\n\n{data_pilihan['channel']}")
            st.warning(f"**Target Sikap (CPL):**\n\n{data_pilihan['sikap']}")
            
        with col_res2:
            with st.expander("📌 Salin Teks Ini ke Kolom CPMK & Indikator RPS", expanded=True):
                st.write(f"**Materi:** {materi}")
                st.write(f"**Indikator Sikap:** {data_pilihan['indikator']}")
                st.write(f"**Metode & Bukti Evaluasi:** {data_pilihan['metode']}")
                
            with st.expander("📊 Salin Teks Ini ke Rubrik Penilaian (Skala 1-5)", expanded=True):
                st.write("**Skor 5 (Excellent):**")
                st.write(data_pilihan['rubrik_5'])
                st.write("**Skor 3 (Standar):** Menyelesaikan tugas dengan jujur, namun analisis sikap kritis/nasionalisme masih di permukaan.")
                st.write("**Skor 1 (Sangat Kurang):** Plagiarisme, fabrikasi data, atau pasif dalam kelompok.")
    else:
        st.error("Mohon lengkapi Nama Mata Kuliah dan Materi Substantif terlebih dahulu!")
